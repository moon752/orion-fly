FROM python:3.10-slim

# Install Ollama or required dependencies (adjust if needed)
RUN pip install ollama

# Expose port 8000 for Ollama API
EXPOSE 8000

# Start Ollama server on 0.0.0.0:8000 (adjust this command if different)
CMD ["ollama", "serve", "--host", "0.0.0.0", "--port", "8000"]
