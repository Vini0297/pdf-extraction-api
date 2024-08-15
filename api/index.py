from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

@app.route('/extract-pdf', methods=['POST'])
def extract_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF file provided"}), 400
    
    pdf_file = request.files['pdf']
    pdf_file.save('temp.pdf')

    extracted_text = extract_text_from_pdf('temp.pdf')

    return jsonify({"extracted_text": extracted_text})

if __name__ == '__main__':
    app.run(debug=True)
