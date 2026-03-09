from models import Servizio, db
from faker import Faker

def run():
    # 1. Chiediamo il nome del servizio in modo interattivo
    print("--- Configurazione nuovo servizio ---")

    # guarda impostazione python.analysis.typeCheckingMode e setta a "basic" per vedere la docs di strip()
    nome_input = input("Inserisci il nome del servizio (es. Netflix, Spotify): ").strip()

    # 2. Controllo base: se l'utente preme invio senza scrivere nulla
    if not nome_input:
        print("Errore: Il nome non può essere vuoto.")
        return
    
    try:
        with db:
            servizio, created = Servizio.get_or_create(nome=nome_input)

        # NOTA IMPORTANTE
        # nonostante abbiamo definito un indice unique uso il metodo get_or_create per evitare di avere duplicati e riportare messaggi differenti
        # si dice che il database è l'ultima linea di difesa, mentre il controllo nel codice è una questione di User Experience (UX).
        # Ecco perché non dovresti mai rinunciare all'indice unique nel database, anche se il tuo codice sembra "sicuro":
        # Perché l'indice unique a DB è obbligatorio?
        # - Integrità totale: Se un altro programma (o un altro script) si connette al database e prova a inserire un duplicato saltando il tuo codice Python, il database lo bloccherà comunque.
        # - Le "Race Conditions" (Concorrenza): Se due utenti premono "Invio" nello stesso identico istante, il tuo codice Python potrebbe fare il controllo select per entrambi, vedere che il nome non esiste, e provare a fare due insert. Senza il vincolo nel database, ti ritroveresti con un duplicato. Il database, essendo atomico, ne accetterà uno e rifiuterà l'altro.
        # - Velocità: L'indice unique crea una struttura (chiamata B-Tree) che permette al database di trovare i nomi istantaneamente. Senza indice, ogni volta che fai get_or_create, il database deve leggere tutta la tabella riga per riga.
        if created:
            print(f"Inserito nuovo servizio: '{servizio.nome}' (ID: {servizio.id})")
        else:
            print(f"Servizio '{servizio.nome}' già presente nel database con ID {servizio.id}).")

    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")

def inserisci_servizio_random():
    # 1. Chiediamo il nome del servizio in modo interattivo
    print("--- Configurazione nuovo servizio ---")
    
    try:
        fake = Faker('it_IT')

        with db.atomic():
            servizio: Servizio = Servizio.create(
                nome=fake.domain_name()
            )

        print(f"Inserito nuovo servizio: '{servizio.nome}' (ID: {servizio.id})")

    except Exception as e:
        print(f"Errore durante l'inserimento: {e}")        
    
if __name__ == "__main__":
    #run()
    # Crea n servizi in un colpo solo
    for _ in range(100): 
        inserisci_servizio_random()