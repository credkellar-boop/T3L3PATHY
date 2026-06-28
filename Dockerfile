# Use an official runtime as a parent image (adjust as needed)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your mono-repo code into the container
COPY . .

# Specify the command to run your application
CMD ["python", "main.py"]
