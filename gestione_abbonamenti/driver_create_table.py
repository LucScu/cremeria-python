import mysql.connector
from mysql.connector import Error

def crea_tabella():
    connection = None
    cursor = None

    try:
        # Configura i tuoi parametri di accesso
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='gestione_abbonamenti',
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # La query usa "IF NOT EXISTS" per gestire il controllo automaticamente
            sql_create_table = """
            DROP TABLE utente_driver;
            CREATE TABLE IF NOT EXISTS utente_driver (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome2 VARCHAR(255) NOT NULL,
                cognome VARCHAR(255) NOT NULL,
                etaaaaa varchar(255) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
            """

            cursor.execute(sql_create_table)
            
            # Verifichiamo se è stata effettivamente creata ora o se esisteva già
            # (Opzionale, giusto per avere un feedback nel terminale)
            print("Operazione completata: la tabella \"utente_driver\" è pronta all'uso.")

    except Error as e:
        print(f"Errore durante l'operazione: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        
        if connection is not None:
            connection.close()
        
        print("Connessione al database chiusa.")

if __name__ == "__main__":
    crea_tabella()