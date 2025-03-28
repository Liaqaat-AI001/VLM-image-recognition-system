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

## To use the code follow the following pattern 

## Required Dependencies
python 3.10

Flask

torch 2.3.1 

transformers

Pillow


If Cloning repository not working the please follow the procedure below.

## Download files
Download the following three files.
1. app.py
2. batch.py
3. index.html
   
## Folder Setup


1. You have to make one folder and inside the folder make two sub folders named **templates**' and "**test_images"**
2. Put app.py and batch.py files in the main folder
   
3. put the **index.html** file  inside **"templates"**
 
4. Place your test dataset in the folder "**test_images**"
   
. 
For Example

   
**VLM-image-recognition-system** is main folder

├── app.py

├── batch.py

├── templates/
│   └── index.html

├── test_images/          ← You place your test images here

## Run files

Now all three files, app.py, batch.py and index.html, open in VS Code

## app.py 
1. First run the app.py file through bash

  python3 app.py
  
The model will auto-download from HuggingFace when `app.py` runs for the first time.

Keep it running 
## batch.py
2. Add another terminal and run batch.py through bash
   
   python3 batch.py

when you run this, it will ask you to open 
http://localhost:5000

When you click on the link, you will see the results.









