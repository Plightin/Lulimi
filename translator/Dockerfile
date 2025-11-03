# Use a lightweight base image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install the Python web servers
RUN pip install waitress flask

# --- Copy the translator app files ---
# Assumes the build context is the repo root
COPY translator/lulimi_translator.html /app/index.html
COPY translator/server.py /app/server.py

# Environment variable for Cloud Run
ENV PORT 8080

# Expose the port
EXPOSE 8080

# Run the web server
CMD [ "python", "server.py" ]
