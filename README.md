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

## Required Dependencies
python 3.10
Flask
torch 2.3.1 
transformers
Pillow
## Folder Setup
Ensure the project folder has the following structure:
and put the following files in the folders accordingly.
VLM-image-recognition-system/
├── app.py

├── batch.py

├── templates/
│   └── index.html

├── static/
│   └── images/           ← System saves analyzed images here

├── temp_uploads/         ← Uploads are temporarily stored here

├── test_images/          ← You place your test images here

├── uploaded_images/      




