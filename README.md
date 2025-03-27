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
1. You have to make a folder
2. put app.py, and batch.py file in the folder
3. you have to make a another folder insie it and named it "templates" and put the index.html file in this folder
4. make another folder named "test_images" and put all the images which you want to test through this system
   e.g
VLM-image-recognition-system/
├── app.py

├── batch.py

├── templates/
│   └── index.html

├── test_images/          ← You place your test images here

## Run 
Now all three files app.py, batch.py and index.html open in VS code

1.first run the app.py file through bash

  python3 app.py

Keep it running 

2. Add another terminal and run batch.py through bash
   
   python3 batch.py

when you run this, it will ask you to open 
http://localhost:5000

When you click on the link, you will see the results.









