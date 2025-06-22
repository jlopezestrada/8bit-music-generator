FROM python:3.13

# system dependencies required for sounddevice library
RUN apt-get update && apt-get install -y \
    libportaudio2 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]