"""
Uploading files with a POST method.
"""

import os

from flask import Flask, request

# Tool that add security checking if the file can be dangerous
from werkzeug import secure_filename

app = Flask(__name__)

# Set the folder where to updload to file
up_folder = ''  # If empty, will upload the file to the script working directory
app.config['UPLOAD_FOLDER'] = up_folder

# Specifies maximum size of file to be uploaded – in bytes
app.config['MAX_CONTENT_PATH'] = 10 * 1024 * 1024  # 10MB

# It's a good practice to check file's extension before uploading
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    # Check allowed file's extension
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return 'Go to /upload'


@app.route('/upload')
def upload_temp():
    return """
    <html>
       <body>
       
          <form action="http://localhost:5000/uploader" method="POST" enctype="multipart/form-data">
             <input type="file" name="file">
             <input type="submit">
          </form>
          
       </body>
    </html>
    """


@app.route('/uploader', methods=['POST'])
def upload_file():
    file = request.files['file']  # Keyword name will depen on the application that making the request

    # To get the filename
    print(file.filename)

    # To get the size of the file
    print(file.content_length)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully to {}'.format(up_folder)


if __name__ == '__main__':
   app.run()
