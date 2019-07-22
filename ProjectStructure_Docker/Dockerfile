# Dockerfile defines what goes on in the environment inside your container, it must be in the top most level of the project.

# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the container working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Any other commands can be typed here, starting with a RUN keyword

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME mydockerenv

# Run this when the container launches - [application, filename]
CMD ["python", "app.py"]
