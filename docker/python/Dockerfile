# Use a specific Python version
FROM python:3.12.3

# Set the working directory inside the container
WORKDIR /var/www/demo

# Copy requirements.txt first to leverage Docker caching
COPY demo/requirements.txt requirements.txt

# Install system dependencies (e.g., for bcc)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*  

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary
RUN pip install djangorestframework
# Copy project files
COPY demo .

# Set Python environment variables
ENV PYTHONPATH=/usr/bin/python3

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
