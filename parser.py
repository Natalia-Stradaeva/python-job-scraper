# Importiamo le librerie necessarie per scaricare e leggere la pagina web
import requests
from bs4 import BeautifulSoup

# --- CONFIGURAZIONE DEI FILTRI (Parametri stabiliti) ---
MIN_SALARY = 1200  # Stipendio minimo netto mensile 
ALLOWED_LOCATION_TYPES = ["remoto", "ibrido", "smart working", "campania", "lazio", "roma"]
STOP_WORDS = ["stage", "tirocinio", "rimborso spese", "apprendistato"]
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

# Località accettabili per ufficio (vicino a Villa Literna: Aversa, Caserta, Napoli, Roma)
PREFERRED_LOCATIONS = ["napoli", "caserta", "aversa", "roma", "campania", "lazio", "remoto", "smart working"]

# --- LOGICA DEL PARSER PER LE OFFERTE DI LAVORO ---
# Iteriamo (passiamo in rassegna) tutti i siti presenti nel nostro dizionario JOB_SITES
for site_name, site_url in JOB_SITES.items():
    print(f"\nAnalisi del sito: {site_name.upper()} ({site_url})")
    
    try:
        # Inviamo una richiesta HTTP al sito
        response = requests.get(site_url, timeout=10)
        
        # Controlliamo se la connessione è riuscita
        if response.status_code == 200:
            print(f"[{site_name}] Pagina scaricata con successo! Analisi in corso...")
            
            # Analizziamo l'HTML con BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # [Qui nei prossimi passaggi aggiungeremo la ricerca specifica delle offerte]
            
        else:
            print(f"[{site_name}] Attenzione: errore di connessione (Codice: {response.status_code})")
            
    except Exception as e:
        print(f"[{site_name}] Si è verificato un errore durante la connessione: {e}")

print("\nFatto! Scansione dei siti completata.")