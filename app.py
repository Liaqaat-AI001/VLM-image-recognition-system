from flask import Flask, request, render_template
from PIL import Image
import torch
import json
import re
import os
from datetime import datetime
from transformers import AutoModelForCausalLM

app = Flask(__name__)

# Directories
UPLOAD_FOLDER = "temp_uploads"
STATIC_IMAGE_FOLDER = os.path.join("static", "images")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_IMAGE_FOLDER, exist_ok=True)

# In-memory result storage
inference_results = []

#VLM model
print(f"[{datetime.now()}] Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    "AIDC-AI/Ovis2-4B",
    torch_dtype=torch.bfloat16,
    multimodal_max_length=32768,
    trust_remote_code=True
).cuda()
text_tokenizer = model.get_text_tokenizer()
visual_tokenizer = model.get_visual_tokenizer()
print(f"[{datetime.now()}] Model loaded.")

# Prompt 
prompt = """<image>
<image>
Carefully analyze the safety risks in the image and return the result in structured JSON format. Evaluate both environmental hazards and personnel safety using the following logic:

1. If there is visible fire, smoke, chemical leak, explosion, or structural damage, mark the "environment" as "Unsafe".
2. If a person is present but not visibly injured, trapped, or unconscious, mark "personnel_status" as "Safe". Only mark "Unsafe" if the person appears injured, stuck, or harmed.
3. If a person is walking toward or standing near a hazard but appears uninjured, note that under "personnel_issues", not "personnel_status".
4. Mention environment issues clearly (e.g., "fire on left side", "dense smoke blocking exit", "collapsed ceiling").
5. Mention personnel issues like proximity to danger, lack of gear, or risky behavior.
6. Include actionable alerts only if immediate attention or evacuation is required.

Return JSON with these keys:
- "environment": "Safe" or "Unsafe"
- "personnel_status": "Safe" or "Unsafe"
- "environment_issues": List of specific hazards
- "personnel_issues": List of any safety concerns related to personnel
- "alerts": List of urgent safety warnings if needed
."""

@app.route('/')
def index():
    return render_template('index.html', results=inference_results)

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image_file = request.files['image']
    filename = image_file.filename
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    image_file.save(upload_path)

    print(f"[{datetime.now()}] Received image: {filename}")

    try:
        image = Image.open(upload_path).convert("RGB")
    except Exception as e:
        return f"Error opening image: {e}", 500

    try:
        # VLM Inference
        query = prompt
        images = [image]
        prompt, input_ids, pixel_values = model.preprocess_inputs(query, images, max_partition=9)
        attention_mask = torch.ne(input_ids, text_tokenizer.pad_token_id)
        input_ids = input_ids.unsqueeze(0).to(device=model.device)
        attention_mask = attention_mask.unsqueeze(0).to(device=model.device)

        if pixel_values is not None:
            pixel_values = pixel_values.to(dtype=visual_tokenizer.dtype, device=visual_tokenizer.device)
        pixel_values = [pixel_values]

        with torch.inference_mode():
            output_ids = model.generate(
                input_ids,
                pixel_values=pixel_values,
                attention_mask=attention_mask,
                max_new_tokens=1024,
                do_sample=False,
                eos_token_id=model.generation_config.eos_token_id,
                pad_token_id=text_tokenizer.pad_token_id,
                use_cache=True
            )[0]

        output_text = text_tokenizer.decode(output_ids, skip_special_tokens=True)
        print(f"[{datetime.now()}] Model output for {filename}:\n{output_text[:800]}...\n")

        # parse JSON
        json_match = re.search(r'\{.*\}', output_text, re.DOTALL)
        if json_match:
            try:
                result_json = json.loads(json_match.group(0))
            except json.JSONDecodeError:
                result_json = {"raw_output": output_text[:800]}  # limit size
        else:
            result_json = {"raw_output": output_text[:500]}

    except Exception as e:
        return f"Error during inference: {e}", 500

    # Save image for frontend
    static_path = os.path.join(STATIC_IMAGE_FOLDER, filename)
    image.save(static_path)

    # Store result
    entry = {
        "image_path": f"/static/images/{filename}",
        "result": result_json
    }
    inference_results.append(entry)

    print(f"[{datetime.now()}] Inference done for {filename}.")

    return render_template("index.html", results=inference_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
