# Use official Python 3.11 slim base image for smaller size
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first (leverage Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variable to disable Flask debug mode in production
ENV FLASK_ENV=production

# Run the Flask application
CMD ["python", "app.py"]
