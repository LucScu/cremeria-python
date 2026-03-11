from models import Utente, db
from faker import Faker

def inserisci_utente_random():
    print("--- Generazione nuovo utente ---")
    
    try:
        fake = Faker('it_IT')
        
        # Transazione e rollback gestita da peewee
        with db.atomic(): 
            utente: Utente = Utente.create(
                nome=fake.first_name(),
                cognome=fake.last_name()
            )
        
        print(f"Inserito nuovo utente: {utente.nome} {utente.cognome} (ID: {utente.id})")

    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")

if __name__ == "__main__":
    #inserisci_utente_random()
    # Crea n utenti in un colpo solo
    for _ in range(100): 
        inserisci_utente_random()