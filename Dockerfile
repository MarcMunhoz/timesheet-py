# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script file to the working directory in the container
COPY timesheet.py .

# Set the command to run the Python script
CMD ["python", "timesheet.py"]
