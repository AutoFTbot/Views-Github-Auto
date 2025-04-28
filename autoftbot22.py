import requests
import time
import re

url = "https://profile-counter.glitch.me/AutoFTbot/count.svg"

start_time = time.time()

def get_count():
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            svg_content = response.text
            matches = re.findall(r'<tspan[^>]*>(\d+)<\/tspan>', svg_content)
            if matches:
                return ''.join(matches)
    except Exception as e:
        print(f"Error: {e}")
    return None

# Menyimpan hasil ke file log
with open("output_log.txt", "w") as f:
    while True:
        elapsed_minutes = (time.time() - start_time) / 60
        count = get_count()
        
        # Format output untuk log
        log = f"[⏳] Waktu jalan: {elapsed_minutes:.2f} menit\n"
        
        if count is not None:
            log += f"[🔥] Jumlah count sekarang: {count}\n"
        else:
            log += "[❌] Gagal mengambil count.\n"
        
        f.write(log)  # Menyimpan log ke file

        time.sleep(5)
