FROM python:3.10-slim

# Install tools
RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Copy scripts
COPY mine.py server.py /app/

# Install Flask
RUN pip install flask

# Run 
CMD ["python", "server.py"]
