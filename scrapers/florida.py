from scrapers.base_scraper import BaseJailScraper

class FloridaScraper(BaseJailScraper):
    def __init__(self):
        super().__init__(state_name="Florida", state_code="FL")

    def run(self):
        print(f"[*] {self.state_name} ilceleri taraniyor ve linkler dogrulaniyor...")
        
        florida_counties = [
            {
                "county_name": "Miami-Dade County",
                "slug": "miami-dade",
                "facility_name": "Miami-Dade County Corrections & Rehabilitation",
                "phone": "(786) 263-7000",
                "address": "2525 NW 62nd St, Miami, FL 33147",
                "official_website": "https://www.miamidade.gov/global/corrections/home.page",
                "roster_url": "https://www.miamidade.gov/technology/inmate-search.asp"
            },
            {
                "county_name": "Orange County",
                "slug": "orange",
                "facility_name": "Orange County Corrections Department",
                "phone": "(407) 836-4000",
                "address": "3723 Vision Blvd, Orlando, FL 32839",
                "official_website": "https://www.ocfl.net/",
                "roster_url": "https://netapps.ocfl.net/InmateLookup/"
            },
            {
                "county_name": "Hillsborough County",
                "slug": "hillsborough",
                "facility_name": "Hillsborough County Sheriff's Office Jail",
                "phone": "(813) 247-8300",
                "address": "520 N Falkenburg Rd, Tampa, FL 33619",
                "official_website": "https://www.teamhcso.com/",
                "roster_url": "https://members.teamhcso.com/ArrestInquiry/"
            }
        ]

        for county in florida_counties:
            print(f"  -> {county['county_name']} linki kontrol ediliyor...")
            county["status"] = self.check_link_status(county["roster_url"])

        self.save_data(florida_counties)