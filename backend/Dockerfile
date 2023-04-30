# Base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

RUN apt-get update && apt-get -y install python3-pip python3-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port (optional)
EXPOSE 8000

# Start the app
CMD ["python", "app.py"]
