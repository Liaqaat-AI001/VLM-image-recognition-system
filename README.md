# VLM-image-recognition-system

This project is a demo system using a Vision-Language Model (VLM) to identify potential safety hazards in images of industrial or workplace environments. The system analyzes images, generates a JSON summary of safety issues, and displays the results on a user-friendly web interface.

---

## 🚀 Features

- ✅ Vision-Language Model (Ovis2-4B) for multi-modal reasoning
- 🧠 Prompt-engineered for hazard detection and personnel assessment
- 🔥 Detects smoke, fire, gear violations, structural damage, and risky behavior
- 👷 Classifies "environment" and "personnel" safety independently
- 🧾 Outputs structured JSON (alerts, issues, risk conditions)
- 🖼 Frontend displays image + inference neatly
- ⚙️ CLI-based batch uploader (`batch.py`) to analyze multiple images
- 💡 Designed for expansion into real-time camera feeds or dashboards

---

## To use the code we have to follow the following pattern 

we have to make folder and place the files inside the folder as under.

vlm-safety-detection/

├── app.py                 # Flask backend + VLM inference

├── batch.py               # CLI tool to upload test images

├── templates/index.html   # HTML template for web frontend

├── static/images/         # Folder to store uploaded display images

├── temp_uploads/          # Temporary holding folder for incoming images

├── test_images/           # image dataset 

