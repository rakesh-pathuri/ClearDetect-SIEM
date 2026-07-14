# Use lightweight Python Alpine image
FROM python:3.11-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose Dashboard Port
EXPOSE 8080

# Run the Translator Engine
CMD ["python", "eai_translator.py"]
