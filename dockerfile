# Lulimi Translation API Deployment Dockerfile
# Base image for Python applications
FROM python:3.10-slim

# Set environment variables for non-interactive mode and Python unbuffered output
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Create the working directory and move into it
WORKDIR $APP_HOME

# Install system dependencies needed for some Python packages (e.g., building wheels)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies first (leverages Docker cache)
# We assume requirements.txt is in the project root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the trained models and the API code
# IMPORTANT: This assumes the following structure in your local project root:
# /backend/api.py
# /backend/models/ (containing the 6 trained model directories)

# Copy the backend code
COPY backend/api.py $APP_HOME/api.py

# Copy the models directory. This is crucial for inference.
# Ensure you are using Git LFS for this folder if models are large!
COPY backend/models/ $APP_HOME/models/

# Expose the port where FastAPI will run (default for Uvicorn)
EXPOSE 8000

# Command to run the application using Uvicorn
# The --host 0.0.0.0 is essential for containerized environments
# --workers 4 sets the number of processes (adjust based on CPU/RAM)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
