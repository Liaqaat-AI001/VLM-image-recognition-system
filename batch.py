import os
import requests


IMAGE_FOLDER = "test_images" # Test images


API_URL = "http://localhost:5000/analyze" #flask backend link


ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png')

def send_image_to_server(image_path):
    with open(image_path, 'rb') as img_file:
        files = {'image': img_file}
        try:
            response = requests.post(API_URL, files=files)
            if response.status_code == 200:
                print(f"[✓] Uploaded: {os.path.basename(image_path)}")
            else:
                print(f"[!] Failed to upload {os.path.basename(image_path)} - Status Code: {response.status_code}")
        except Exception as e:
            print(f"[!] Error uploading {image_path}: {e}")

def main():
    if not os.path.exists(IMAGE_FOLDER):
        print(f"[!] Folder '{IMAGE_FOLDER}' not found. Please create it and add test images.")
        return

    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(ALLOWED_EXTENSIONS)]

    if not image_files:
        print(f"[!] No images found in '{IMAGE_FOLDER}'")
        return

    print(f"[~] Found {len(image_files)} image(s). Starting upload...\n")

    for filename in image_files:
        full_path = os.path.join(IMAGE_FOLDER, filename)
        send_image_to_server(full_path)

    print("\n[✓] All done! Visit http://localhost:5000 to view results.")

if __name__ == "__main__":
    main()
