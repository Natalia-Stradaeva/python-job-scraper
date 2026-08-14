# Importiamo le librerie necessarie per scaricare e leggere la pagina web
import requests
from bs4 import BeautifulSoup

# Заголовки, чтобы сайт думал, что мы - обычный браузер
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# --- CONFIGURAZIONE DEI FILTRI (Parametri stabiliti) ---
MIN_SALARY = 1200  # Stipendio minimo netto mensile 
ALLOWED_LOCATION_TYPES = ["remoto", "ibrido", "smart working", "campania", "lazio", "roma"]
STOP_WORDS = ["stage", "tirocinio", "rimborso spese", "apprendistato", "senior", "lead", "manager", 
              "skip to", "sign in", "ai-powered", "resume builder", "cookie", "privacy"]git add 
KEYWORDS = ["python", "sql", "docker", "cloud", "ai", "machine learning", "distributed systems"]

# --- LISTA DEI SITI WEB TARGET PER IL LAVORO ---
# Elenco completo delle piattaforme: regionali, italiane, europee e globali
JOB_SITES = {
    "regione_campania": "https://lavoro.regione.campania.it",
    "indeed_italia": "https://it.indeed.com/jobs?q=python+junior&l=Campania",
    "subito_lavoro": "https://www.subito.it/annunci-campania/offerta-lavoro/napoli/napoli/python",
    "linkedin_italia": "https://www.linkedin.com/jobs/search/?keywords=Python%20Junior&location=Campania%2C%20Italia",
    "infojobs": "https://www.infojobs.it/lavoro-python-junior.isc",
    "glassdoor": "https://www.glassdoor.it/Lavoro/italia-junior-python-developer-lavoro-SRCH_KO0,25_IL.9,15_IN216.htm",
    "talent_italia": "https://it.talent.com/jobs?k=python&l=campania",
    "monster_italia": "https://www.monster.it/lavoro/ricerca/?q=python&where=campania",
    "wellfound": "https://wellfound.com/role/l/python-engineer",
    "remoteok": "https://remoteok.com/remote-python-jobs",
    "weworkremotely": "https://weworkremotely.com/remote-jobs/search?term=python",
    "startup_jobs": "https://startup.jobs/remote-python-developer-jobs"
}

# --- LOGICA DEL PARSER PER LE OFFERTE DI LAVORO ---
all_found_jobs = []

# Località accettabili per ufficio (vicino a Villa Literna: Aversa, Caserta, Napoli, Roma)
PREFERRED_LOCATIONS = ["napoli", "caserta", "aversa", "roma", "campania", "lazio", "remoto", "smart working"]

# --- LOGICA DEL PARSER PER LE OFFERTE DI LAVORO ---
# Iteriamo (passiamo in rassegna) tutti i siti presenti nel nostro dizionario JOB_SITES
for site_name, site_url in JOB_SITES.items():
    print(f"\nAnalisi del sito: {site_name.upper()}")
    
    try:
        response = requests.get(site_url, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Cerchiamo tutti i possibili tag che contengono testi di offerte
            job_elements = soup.find_all(['h2', 'h3', 'a', 'p'])
            
            site_matches = 0
            for element in job_elements:
                job_text = element.get_text().strip().lower()
                
                # Controlliamo le parole chiave e le stop-words
                has_keyword = any(kw in job_text for kw in KEYWORDS)
                has_stop_word = any(sw in job_text for sw in STOP_WORDS)
                
                if has_keyword and not has_stop_word and 15 < len(job_text) < 150:
                    if job_text not in all_found_jobs:
                        all_found_jobs.append(f"[{site_name.upper()}] {element.get_text().strip()}")
                        site_matches += 1
            
            print(f"[{site_name}] Trovati {site_matches} potenziali match.")
            
        else:
            print(f"[{site_name}] Attenzione: errore di connessione (Codice: {response.status_code})")
            
    except Exception as e:
        print(f"[{site_name}] Errore: {e}")

# --- SALVATAGGIO DEI RISULTATI NEL FILE ---
with open("risultati.txt", "w", encoding="utf-8") as file:
    if all_found_jobs:
        file.write(f"Trovate {len(all_found_jobs)} offerte potenziali:\n\n")
        for job in all_found_jobs:
            file.write(job + "\n---\n")
    else:
        file.write("Nessuna offerta trovata in questa sessione.\n")

print(f"\nFatto! Scansione completata. Trovati {len(all_found_jobs)} risultati totali salvati in 'risultati.txt'.")