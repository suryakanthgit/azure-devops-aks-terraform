import urllib.request
import json
from datetime import datetime

APP_URL = "http://localhost:5000"

def check_health():
    try:
        url = f"{APP_URL}/health"
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read())
        print(f"[{datetime.now()}] Status: {data['status']} ✅")
        return True
    except Exception as e:
        print(f"[{datetime.now()}] Health check FAILED ❌: {e}")
        return False

if __name__ == '__main__':
    print("Starting Azure Monitor health check...")
    check_health()