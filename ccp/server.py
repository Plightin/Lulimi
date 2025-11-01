import os
from flask import Flask, send_file
from waitress import serve

app = Flask(__name__)

# This is the main route that serves your HTML file
@app.route("/", methods=["GET"])
def index():
    # Serves the file located at /app/index.html (where the Dockerfile copies it)
    return send_file("/app/index.html")

if __name__ == "__main__":
    # Get the port number from the environment variable set by Cloud Run
    port = int(os.environ.get("PORT", 8080))
    
    # Use Waitress to serve the app
    print(f"Serving CCP app on port {port}...")
    serve(app, host="0.0.0.0", port=port)
