# Use an official Python runtime
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
#EXPOSE 5000

ENV PORT=8080
ENV PYTHONUNBUFFERED=TRUE

#CMD exec gunicorn --bind :$PORT main:app --workers 1 --threads 1 --timeout 0
CMD python main.py