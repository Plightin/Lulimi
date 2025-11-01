# Use a lightweight base image with Python for simplicity
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install a simple, production-ready HTTP server (Waitress)
RUN pip install waitress

# --- CRITICAL FIX ---
# Copy the HTML file from the 'ccp/' subdirectory (relative to the build context root)
COPY ccp/lulimi_ccp_interface.html /app/index.html

# The port Cloud Run will listen on
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Command to run the Waitress server using a minimal Flask app
# This creates and runs a tiny server to serve the static index.html
CMD [ "sh", "-c", "echo 'from flask import Flask, send_file\napp = Flask(__name__)\n@app.route(\"/\", methods=[\"GET\"])\ndef index():\n return send_file(\"/app/index.html\")\nif __name__ == \"__main__\":\n from waitress import serve\n serve(app, host=\"0.0.0.0\", port=8080)' > server.py && python server.py" ]
