from models import Utente, Servizio, Abbonamento, db

def run():
    try:
        with db:
            # Crea la tabella se non esiste (IF NOT EXISTS è integrato)
            db.create_tables([Utente, Servizio, Abbonamento], safe=True)
            
        print("Tabelle verificate/create con successo!")

    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    run()