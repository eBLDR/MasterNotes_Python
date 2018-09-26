from flask import Flask

# Taking __name__ is correct if using a single module,
# alternatives are a custom name or __name__.split('.')[0] if the file is in a folder
app = Flask(__name__, template_folder='templates')

# @template_folder refers to the folder that contains the templates that should be used
# by the application. Defaults to 'templates' folder in the root path of the app

# Import at at the bottom to avoid circular imports
from app import routes
