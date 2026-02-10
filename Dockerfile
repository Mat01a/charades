# Official Python image
FROM python:3.13-slim

# Create app dir
RUN mkdir /app

# Set app dir as working dir
WORKDIR /app

# Prevent python writing pyc files on disk
ENV PYTHONDONTWRITEBYTECODE=1

# Prevent Python from bufferint stdout and stderr
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN pip install --upgrade pip

# Copy Django project
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory to container
COPY . /app/

# Expose default or different Django port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
