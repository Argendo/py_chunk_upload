from flask import Flask, request, render_template
from flask_dropzone import Dropzone
import os

app = Flask(__name__)

# Flask-Dropzone
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*,application/pdf'
app.config['DROPZONE_MAX_FILE_SIZE'] = 3
app.config['DROPZONE_MAX_FILES'] = 30
app.config['DROPZONE_TIMEOUT'] = 5 * 60 * 1000  # 5 минут

# chunked files folder
app.config['UPLOAD_FOLDER'] = 'uploads'

dropzone = Dropzone(app)

@app.route('/')
def index():
    return render_template('index_chunked.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files.get('file')

    if not uploaded_file:
        return 'No file uploaded', 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
    uploaded_file.save(file_path)

    return 'Chunk uploaded successfully', 200


if __name__ == '__main__':
    app.run(debug=True, port=5002)

