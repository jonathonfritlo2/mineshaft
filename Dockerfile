
FROM python:3.10-slim

# Install 
RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# d
COPY miner.py /app/miner.py

# d
CMD ["python", "mine.py"]
