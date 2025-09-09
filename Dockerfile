# Base 
FROM python:3.10-slim

# Install required tools
RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*

# set dir
WORKDIR /app

# Copy 
COPY miner.py /app/miner.py

# Run scripts
CMD ["python", "mine.py"]
