
FROM python:3.10-slimFROM python:3.10-slim

RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY miner.py server.py /app/

RUN pip install flask

CMD ["python", "server.py"]
