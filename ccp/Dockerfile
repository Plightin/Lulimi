# Use a lightweight base image with Python
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install Flask (which we now need for server.py) and Waitress
RUN pip install waitress flask

# --- CRITICAL FIX ---
# Copy the HTML file from the 'ccp/' subdirectory
COPY ccp/lulimi_ccp_interface.html /app/index.html

# --- NEW STEP ---
# Copy the new robust server file
COPY ccp/server.py /app/server.py

# The port Cloud Run will listen on
ENV PORT 8080

# Expose the port
EXPOSE 8080

# --- NEW CMD ---
# Run the server.py file directly. This is simple and robust.
CMD [ "python", "server.py" ]
