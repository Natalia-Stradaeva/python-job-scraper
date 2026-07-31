# Importiamo le librerie necessarie per scaricare e leggere la pagina web
import requests
from bs4 import BeautifulSoup

# L'indirizzo del sito Web che vogliamo analizzare (usiamo un sito di prova sicuro)
url = 'https://quotes.toscrape.com/'

print("Scaricamento della pagina in corso...")
# Scarichiamo il codice HTML della pagina
response = requests.get(url)

# Controlliamo se la connessione è riuscita (il codice 200 significa OK)
if response.status_code == 200:
    print("Pagina scaricata con successo! Estrazione dei dati...")
    
    # Analizziamo l'HTML della pagina
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Troviamo tutte le citazioni presenti nella pagina
    quotes = soup.find_all('span', class_='text')
    
    # Apriamo un file di testo in scrittura e salviamo i risultati
    with open('risultati.txt', 'w', encoding='utf-8') as f:
        for i, quote in enumerate(quotes, 1):
            text = f"{i}. {quote.text}\n"
            f.write(text)
            print(text.strip())
            
    print("\nFatto! I dati sono stati salvati nel file 'risultati.txt'.")
else:
    print(f"Errore durante il download della pagina: {response.status_code}")