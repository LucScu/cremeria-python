from models import Utente, db
from faker import Faker

def inserisci_utente_random():
    print("--- Generazione nuove cliente ---")
    
    try:
        fake = Faker('it_IT')
        
        # Transazione e rollback gestita da peewee
        with db.atomic(): 
            utente = Utente.create(
                nome=fake.first_name(),
                cognome=fake.last_name()
            )
        
        print(f"Inserito utente: {utente.nome} {utente.cognome} (ID: {utente.id})")

    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")

if __name__ == "__main__":
    inserisci_utente_random()
    # Crea 10 utenti in un colpo solo
    #for _ in range(10): 
        #inserisci_utente_random()