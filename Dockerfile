
# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file into the container
COPY requirements.txt .

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Allow access to port 5000
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
