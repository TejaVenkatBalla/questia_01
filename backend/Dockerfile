# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask and Google API
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV GOOGLE_API_KEY=AIzaSyD28q1xpukVhjDYcLlV8fQOqw11fnvN_lk

# Expose the port Flask will run on
EXPOSE 8080

# Run the application
CMD ["flask", "run"]
