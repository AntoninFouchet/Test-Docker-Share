from datetime import datetime
import time
print("Le docker fonctionne")

data_path = "/app/data/test_volume.txt"


time.sleep(1000)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(data_path, "a") as f:
    f.write(f"Passage de app.py le {now}\n")


