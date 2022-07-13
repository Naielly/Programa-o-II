from peewee import *
import os 

db = SqliteDatabase("pessoa.db")

class Pessoa(Model):

    cpf = CharField()
    nome = CharField()
    endereco = CharField()
    telefone = CharField()

    class Meta():
        
        database = db

if __name__ == "__main__":
    '''
    arq = "pessoa.db"
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Pessoa])
    
    except OperationalError as err:
        print("ERROU")

    Pessoa.create (cpf = "000.000.000-00", nome = "Fulano Ciclano", 
    endereco = "Rua Ipiranga, 0", telefone = "(00) 9 0000-0000")
    '''
