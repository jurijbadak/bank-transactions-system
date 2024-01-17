# Verwenden Sie ein Basis-Image, z.B. Python
FROM python:3.8

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die Python-Abhängigkeiten und installieren Sie sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren Sie den Rest des Codes in den Container
COPY . .

# Kommando zum Ausführen des Services
CMD ["python", "./producer.py"]