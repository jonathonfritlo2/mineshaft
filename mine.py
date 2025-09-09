import os
import subprocess
import time
import signal
import multiprocessing

# =======================
# CONFIGURATION
# =======================
POOL = "pool.supportxmr.com:3333"   # Monero pool
WALLET = "YOUR_MONERO_WALLET"      # <-- Replace with your wallet
WORKER = "render-free"             # Worker name for pool stats
DONATE = "1"                       # Default XMRig donate level (1%)

def download_xmrig():
    if not os.path.exists("xmrig"):
        print("[*] Downloading XMRig release...")
        os.system(
            "curl -L https://github.com/xmrig/xmrig/releases/download/v6.21.3/"
            "xmrig-6.21.3-linux-x64.tar.gz -o xmrig.tar.gz"
        )
        os.system("tar -xvzf xmrig.tar.gz")
        os.rename("xmrig-6.21.3/xmrig", "xmrig")
        os.system("chmod +x xmrig")
        print("[*] XMRig ready.")

def start_miner():
    # Auto-detect CPU threads
    cpu_threads = multiprocessing.cpu_count()
    print(f"[*] Detected {cpu_threads} CPU thread(s). Optimizing miner...")

    cmd = [
        "./xmrig",
        "-o", POOL,
        "-u", WALLET,
        "-p", WORKER,
        "--donate-level", DONATE,
        "--cpu-priority", "5",       # higher priority
        "--randomx-1gb-pages",       # enable large pages if supported
        "--threads", str(cpu_threads)
    ]

    print(f"[*] Launching miner: {' '.join(cmd)}")
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    download_xmrig()
    proc = start_miner()

    try:
        while True:
            if proc.poll() is not None:
                print("[!] Miner crashed, restarting...")
                proc = start_miner()
            time.sleep(10)
    except KeyboardInterrupt:
        print("[*] Exiting...")
        proc.send_signal(signal.SIGINT)
        proc.wait()

if __name__ == "__main__":
    main()
