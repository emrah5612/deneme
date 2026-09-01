import argparse
from scrapers.florida import FloridaScraper

# Sisteme yeni eyaletler ekledikçe buraya tanımlayacağız:
AVAILABLE_STATES = {
    "florida": FloridaScraper,
}

def main():
    parser = argparse.ArgumentParser(description="Jail Roster Directory Scraper")
    parser.add_argument("--state", type=str, default="all", help="Çalıştırılacak eyalet adı (örn: florida) veya 'all'")
    args = parser.parse_args()

    target_state = args.state.lower()

    if target_state == "all":
        for name, scraper_class in AVAILABLE_STATES.items():
            scraper = scraper_class()
            scraper.run()
    elif target_state in AVAILABLE_STATES:
        scraper = AVAILABLE_STATES[target_state]()
        scraper.run()
    else:
        print(f"[!] Hata: '{target_state}' adında bir eyalet scraper'ı bulunamadı.")
        print(f"Mevcut eyaletler: {list(AVAILABLE_STATES.keys())}")

if __name__ == "__main__":
    main()