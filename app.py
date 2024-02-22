from flask import Flask, request
from flask_cors import CORS
from utilities import extract_text_from_pdf
import os, json
from openai import OpenAI
client = OpenAI(
    api_key="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"
)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def home():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename.endswith('.pdf'):
        # Save the file
        file_path = os.path.join('', file.filename)
        file.save(file_path)

        # Send the file path to the parser
        text = extract_text_from_pdf(file_path)
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You must summarize the text into concise points to help the user understand the main points."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        message_content = chat_completion.choices[0].message.content
        print(message_content)
        return json.dumps({"summary": message_content}), 200
    else:
        return 'Invalid File', 400

if __name__ == '__main__':
    app.run()