import requests
import time
import re

url = "https://profile-counter.glitch.me/AutoFTbot/count.svg"

start_time = time.time()

def ambil_count():
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            svg_content = response.text
            matches = re.findall(r'<tspan[^>]*>(\d+)<\/tspan>', svg_content)
            if matches:
                return ''.join(matches)
    except Exception as e:
        print(f"Kasalahan: {e}")
    return None

while True:
    elapsed_minutes = (time.time() - start_time) / 60
    count = ambil_count()
    print("\033c", end="")
    print(f"[⏳] Waktos jalan: {elapsed_minutes:.2f} menit")
    
    if count is not None:
        print(f"[🔥] Jumlah count ayeuna: {count}")
    else:
        print("[❌] Gagal ngambil count.")
    time.sleep(5)
