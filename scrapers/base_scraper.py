import json
import os
import requests
from datetime import datetime

class BaseJailScraper:
    def __init__(self, state_name, state_code):
        self.state_name = state_name
        self.state_code = state_code
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        })

    def check_link_status(self, url):
        """HEAD yerine stream=True GET isteği kullanarak linki hızlı ve engelsiz doğrular"""
        try:
            # Sadece ilk baytları okur, tüm sayfayı indirip vakit kaybetmez
            response = self.session.get(url, timeout=12, stream=True, allow_redirects=True, verify=False)
            # 403 (Cloudflare/Bot engeli) alsa bile site yayındadır:
            if response.status_code < 400 or response.status_code in [401, 403]:
                return "active"
            return "broken"
        except Exception:
            return "unreachable"

    def save_data(self, counties_data):
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", f"{self.state_name.lower().replace(' ', '_')}.json")
        
        output = {
            "state": self.state_name,
            "state_code": self.state_code,
            "last_updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
            "total_counties": len(counties_data),
            "counties": counties_data
        }
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
            
        print(f"[✓] {self.state_name} verisi basariyla kaydedildi: {file_path}")