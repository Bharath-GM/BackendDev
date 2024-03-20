FROM python:3.10

WORKDIR /zywa-card-apis

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to specify where the application should be accessible
ENV FLASK_APP=app.py

# Run gunicorn with 4 workers on port 8000 and bind to 0.0.0.0
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]