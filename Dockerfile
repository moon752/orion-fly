FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl wget unzip gnupg ca-certificates libatk1.0-0 libatk-bridge2.0-0 \
        libcups2 libdbus-1-3 libdrm2 libnspr4 libnss3 libxcomposite1 \
        libxdamage1 libxfixes3 libxrandr2 libu2f-udev libvulkan1 libgbm1 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && python -m playwright install chromium --with-deps
COPY . .
CMD ["python", "-m", "orion_phase8_core"]
