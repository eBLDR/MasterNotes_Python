"""
Uploading files with a POST method.
"""
import os

from flask import Flask, request, send_file

# Tool that adds security checking if the file can be dangerous
from werkzeug import secure_filename

app = Flask(__name__)

# Set the folder where to upload to file
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
    return 'Go to /upload or /download'


# Upload management
@app.route('/upload')
def upload_temp():
    # Set form action equal to the endpoint
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
    file = request.files['file']  # Keyword name will depend on the application that is making the request

    # To get the filename
    print(file.filename)

    # To get the size of the file
    print(file.content_length)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully to {}'.format(up_folder)


# Download management
@app.route('/download')
def download_temp():
    # Set a href equal to the endpoint
    return """
    <html>
        <body>
            <div align="left">
                <a href="/downloader" target="blank"><button class='btn btn-default'>Download!</button></a>
            </div>
        </body>
    </html>
    """


@app.route('/downloader')
def down_file():
    file_path = 'python_icon.jpeg'
    try:
        # send_file(@file_path, @attachment_filename=name_of_file_when_downloaded
        return send_file(file_path, attachment_filename='python.jpeg')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
