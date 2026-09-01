import os
import importlib
import inspect
import argparse

def discover_scrapers():
    """scrapers/ klasöründeki tüm eyalet dosyalarını otomatik bulur ve yükler."""
    scrapers = {}
    scrapers_dir = os.path.join(os.path.dirname(__file__), "scrapers")

    for filename in os.listdir(scrapers_dir):
        if filename.endswith(".py") and filename not in ["__init__.py", "base_scraper.py"]:
            module_name = f"scrapers.{filename[:-3]}"
            module = importlib.import_module(module_name)
            
            # Modül içindeki Scraper sınıfını bul
            for name, cls in inspect.getmembers(module, inspect.isclass):
                if name.endswith("Scraper") and name != "BaseJailScraper":
                    state_key = filename[:-3].lower()  # örn: oklahoma, florida, texas
                    scrapers[state_key] = cls
    return scrapers

def main():
    available_scrapers = discover_scrapers()
    
    parser = argparse.ArgumentParser(description="Otomatik Jail Roster Scraper")
    parser.add_argument("--state", type=str, default="all", help="Çalıştırılacak eyalet adı veya 'all'")
    args = parser.parse_args()

    target = args.state.lower()

    if target == "all":
        print(f"[*] Toplam {len(available_scrapers)} eyalet çalıştırılıyor...")
        for state_name, scraper_cls in available_scrapers.items():
            scraper = scraper_cls()
            scraper.run()
    elif target in available_scrapers:
        scraper = available_scrapers[target]()
        scraper.run()
    else:
        print(f"[!] Hata: '{target}' bulunamadı. Mevcut eyaletler: {list(available_scrapers.keys())}")

if __name__ == "__main__":
    main()
