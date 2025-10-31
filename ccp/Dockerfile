# Use a lightweight base image with Python for simplicity (Flask/SimpleHTTPServer is tiny)
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install a simple, production-ready HTTP server (Waitress)
RUN pip install waitress

# Copy the HTML file into the container
# Assumes lulimi_ccp_interface.html is in the same directory as this Dockerfile when built
# If you are building from the root of the repo, adjust this path:
# COPY ccp/lulimi_ccp_interface.html /app/index.html
COPY lulimi_ccp_interface.html /app/index.html

# The port Cloud Run will listen on
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Command to run the Waitress server, serving the static index.html
# We use a small flask app for robust static file serving
# This requires a tiny server.py file, which we can simulate directly in the run command:
CMD [ "sh", "-c", "echo 'from flask import Flask, send_file\napp = Flask(__name__)\n@app.route(\"/\", methods=[\"GET\"])\ndef index():\n return send_file(\"/app/index.html\")\nif __name__ == \"__main__\":\n from waitress import serve\n serve(app, host=\"0.0.0.0\", port=8080)' > server.py && python server.py" ]
