from models import Utente, Servizio, Abbonamento, db

def inserisci_abbonamento():
    print("--- Registrazione nuovo abbonamento ---")

    # 1. Chiediamo gli ID (input() restituisce stringhe, quindi convertiamo in int)
    id_utente = int(input("Inserisci l'ID dell'utente: "))
    id_servizio = int(input("Inserisci l'ID del servizio: "))

    # Controllo: input vuoti
    if not id_utente or not id_servizio:
        print("Errore: Entrambi gli ID sono obbligatori.")
        return
    
    try:
        with db.atomic():
            # 2. Verifichiamo che esistano (Peewee solleva DoesNotExist se non li trova)
            utente = Utente.get_by_id(id_utente)
            servizio = Servizio.get_by_id(id_servizio)
            abbonamento, created = Abbonamento.get_or_create(
                utente=utente,
                servizio=servizio
            )

        if created:
            print(f"Inserito abbonamento per utente '{utente.nome} {utente.cognome}' e servizio '{servizio.nome}' (ID: {abbonamento.id})")
        else:
            print(f"Abbonamento già presente per utente '{utente.nome} {utente.cognome}' e servizio '{servizio.nome}' (ID: {abbonamento.id})")

    except Utente.DoesNotExist:
        print(f"Errore: L'utente con ID {id_utente} non esiste.")
    except Servizio.DoesNotExist:
        print(f"Errore: Il servizio con ID {id_servizio} non esiste.")
    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")

if __name__ == "__main__":
    inserisci_abbonamento()