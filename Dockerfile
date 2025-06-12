FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget unzip xvfb libxi6 libgconf-2-4 \
    libnss3 libxss1 libasound2 fonts-liberation \
    libappindicator3-1 libatk-bridge2.0-0 \
    libxrandr2 xdg-utils

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "orion/brain/orion_auto.py"]
