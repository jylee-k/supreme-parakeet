# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Fix for libsndfile import error, see https://github.com/PaddlePaddle/PaddleSpeech/issues/440
RUN apt update && \
    apt upgrade -y && \
    apt install -y libsndfile1 && \ 
    apt install -y ffmpeg

# Copy the Python script into the container
COPY asr_api.py .

# Run the Python script
CMD ["python", "asr_api.py"]
