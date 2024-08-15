from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)

@app.route('/api/extract-pdf', methods=['POST'])
def extract_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['pdf']
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in pdf_document:
        text += page.get_text()
    
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run()
