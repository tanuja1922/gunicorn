from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io
import time

app = Flask(__name__)

# For Windows: set explicit path if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    try:
        img = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(img)

        # Simulate heavy CPU work (to see concurrency clearly)
        time.sleep(2)

        return jsonify({
            "filename": file.filename,
            "extracted_text": text.strip()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)