import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://127.0.0.1:5000/ocr"
FILES = ["image.png", "image1.png", "image4.jpg", "image4.webp"]

def send_file(filename):
    with open(filename, "rb") as f:
        files = {"file": (filename, f)}
        resp = requests.post(URL, files=files)
        try:
            return resp.json()
        except Exception:
            return {"error": "Invalid response"}

def main():
    # Use a pool of workers to send multiple requests at once
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(send_file, fname) for fname in FILES]

        for i, fut in enumerate(futures):
            print(f"Response for {FILES[i]}: {fut.result()}")

if __name__ == "__main__":
    main()