# Job Parser 🐍

A lightweight Python script designed to scrape and filter junior developer job offers (focused on Python, SQL, Docker, and AI/Cloud technologies) targeting specific locations in Italy (primarily Campania and Lazio).

## 🚀 Features
- **Multi-site Scraping:** Automatically checks regional portals, job boards, and remote platforms.
- **Smart Filtering:** Filters listings based on predefined keywords, minimum salary thresholds, and exclusion stop-words (e.g., internships, senior positions).
- **Location Priority:** Prioritizes local areas (Naples, Caserta, Aversa, Rome) before broader regions.
- **Clean Output:** Generates a structured report with direct links to job postings.

## 🛠️ Technologies Used
- Python 3.x
- Requests
- BeautifulSoup4

## 📦 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/Natalia-Stradaeva/python-job-scraper.git](https://github.com/Natalia-Stradaeva/python-job-scraper.git)
   
Install dependencies:
pip install requests beautifulsoup4

Run the script:
python parser.py
