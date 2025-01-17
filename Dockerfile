# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your code into the container
COPY . /app

# Install Python dependencies (if any)
# Uncomment and modify the following line if you have a requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run Python scripts
CMD ["python3"]
