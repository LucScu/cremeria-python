from peewee import SQL, ForeignKeyField, MySQLDatabase, Model, CharField, DateTimeField
from dotenv import load_dotenv
import os
import datetime

# CARICAMENTO CONFIGURAZIONE (.env deve essere nella stessa cartella)
load_dotenv()

# INIZIALIZZAZIONE DATABASE
# Usiamo le variabili caricate dal file .env
db = MySQLDatabase(
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci'
)

class BaseModel(Model):
    class Meta:
        database = db

class Utente(BaseModel):
    # L'id viene creato automaticamente come Primary Key da Peewee
    # id_utente = AutoField()
    nome = CharField(max_length=255)
    cognome = CharField(max_length=255)

    class Meta:
        table_name = 'utente'


class Servizio(BaseModel):
    # L'id viene creato automaticamente come Primary Key da Peewee
    # id_servizio = AutoField()
    nome = CharField(max_length=255, unique=True)

    class Meta:
        table_name = 'servizio'


class Abbonamento(BaseModel):
    # L'id viene creato automaticamente come Primary Key da Peewee
    # id_abbonamento = AutoField()

    # Chiave esterna verso Utente
    utente = ForeignKeyField(Utente, backref='abbonamenti')
    
    # Chiave esterna verso Servizio
    servizio = ForeignKeyField(Servizio, backref='abbonati')
    
    # Campo data iscrizione
    # nota il doppio argomento
    data_iscrizione = DateTimeField(
        default=datetime.datetime.now,
        constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")]
    )

    class Meta:
        table_name = 'abbonamento'
        # Crea un indice unico composto da 2 campi
        indexes = (
            (('utente', 'servizio'), True), # Note the trailing comma!
        )