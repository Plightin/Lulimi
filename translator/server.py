# This is a simple Flask server to serve your static HTML file.
# It's identical to the CCP's server.py.

from flask import Flask, send_file
from waitress import serve
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Serves the main translator interface."""
    return send_file('/app/index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    serve(app, host='0.0.0.0', port=port)
