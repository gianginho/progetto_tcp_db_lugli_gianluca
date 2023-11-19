import socket
import mysql.connector

# Password autorizzata
PASSWORD = "einaudi1234"

def db_get_dipendenti(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )

    cur = conn.cursor()

    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "

    query = f"SELECT * FROM dipendenti_lugli_gianluca where 1=1 {clausole}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_get_zone(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )

    cur = conn.cursor()

    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "

    query = f"SELECT * FROM zone_di_lavoro_lugli_gianluca where 1=1 {clausole}"
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_elimina_dipendente(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    query = f"DELETE FROM dipendenti_lugli_gianluca where 1=1 {clausole}"
    cur.execute(query)
    conn.commit()

def db_elimina_zona(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    query = f"DELETE FROM zone_di_lavoro_lugli_gianluca where 1=1 {clausole}"
    cur.execute(query)
    conn.commit()

def db_inserisci_dipendente(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    query = f"INSERT INTO dipendenti_lugli_gianluca (nome, cognome, data_assunzione, stipendio, telefono) VALUES ('{nome}','{cognome}','{data_assunzione}','{stipendio}','{telefono}')"
    cur.execute(query)
    conn.commit()

def db_inserisci_zona(parametri):
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )
    
    cur = conn.cursor()
    
    query = f"INSERT INTO zone_di_lavoro_lugli_gianluca (nome, numero_clienti, dimensione) VALUES ('{nome}','{numero_clienti}','{dimensione}')"
    cur.execute(query)
    conn.commit()

def db_modifica_dipendente(par):
    
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )
    cur = conn.cursor()
    query = f"UPDATE dipendenti_lugli_gianluca SET nome = '{nome}', cognome = '{cognome}', data_assunzione = '{data_assunzione}', stipendio = '{stipendio}', telefono = '{telefono}' WHERE id_dipendente = '{id_modifica}'"
    cur.execute(query)
    conn.commit()

def db_modifica_zona(par):
    
    conn=mysql.connector.connect(
        host="10.10.0.10",
        user="gianluca_lugli",
        password="lugli1234",
        database="5BTepsit",
        port=3306
    )
    cur = conn.cursor()
    query = f"UPDATE zone_di_lavoro_lugli_gianluca SET nome = '{nome}', numero_clienti = '{numero_clienti}', dimensione = '{dimensione}' WHERE id_zona = '{id_modifica}'"
    cur.execute(query)
    conn.commit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50007))
s.listen()

print("In attesa di connessioni...")

conn, addr = s.accept()
print('Connected by', addr)

i = 0
while i < 3:
    password = conn.recv(1024).decode()
    if password == PASSWORD:
        conn.send("Password corretta. Inizia la comunicazione".encode())
        break
    else:
        i += 1
        tentativi_rimasti = 3 - i
        if i < 3:
            conn.send(f"Errore: Password sbagliata. Tentativi rimasti: {tentativi_rimasti}".encode())
        else:
            conn.send("Tentativi massimi raggiunti. Chiudo la connessione".encode())
            conn.close()
            exit()

while True:
    data = conn.recv(1024).decode()
    if not data:
        break  # Connessione chiusa dal client
    if data == "5":
        break  # Termina il server

    if data == "1":
        
        scelta = conn.recv(1024).decode()
        if scelta == "1":
            nome = conn.recv(1024).decode()
            par = {"nome": nome}
            result = db_get_dipendenti(par)
            conn.send(str(result).encode())
        
        else:
            nome = conn.recv(1024).decode()
            par = {"nome": nome}
            result = db_get_zone(par)
            conn.send(str(result).encode())
    
    elif data == "2":

        scelta = conn.recv(1024).decode()
        if scelta == "1":
            id_elimina = conn.recv(1024).decode()
            par = {"id_dipendente": id_elimina}
            db_elimina_dipendente(par)
        
        else:
            id_elimina = conn.recv(1024).decode()
            par = {"id_zona": id_elimina}
            db_elimina_zona(par)
        
    
    elif data == "3":

        scelta = conn.recv(1024).decode()
        if scelta == "1":
            nome = conn.recv(1024).decode()
            cognome = conn.recv(1024).decode()
            data_assunzione = conn.recv(1024).decode()
            stipendio = conn.recv(1024).decode()
            telefono = conn.recv(1024).decode()
            par = {"nome": nome, "cognome": cognome, "data_assunzione": data_assunzione, "stipendio": stipendio, "telefono": telefono}
            db_inserisci_dipendente(par)
        else:
            nome = conn.recv(1024).decode()
            numero_clienti = conn.recv(1024).decode()
            dimensione = conn.recv(1024).decode()
            par = {"nome": nome, "numero_clienti": numero_clienti, "dimensione": dimensione}
            db_inserisci_zona(par)

    elif data == "4":

        scelta = conn.recv(1024).decode()
        if scelta == "1":
            id_modifica = conn.recv(1024).decode()
            nome = conn.recv(1024).decode()
            cognome = conn.recv(1024).decode()
            data_assunzione = conn.recv(1024).decode()
            stipendio = conn.recv(1024).decode()
            telefono = conn.recv(1024).decode()
            par = {"id_dipendente": id_modifica, "nome": nome, "cognome": cognome, "data_assunzione": data_assunzione, "stipendio": stipendio, "telefono": telefono}
            db_modifica_dipendente(par)
        else:
            id_modifica = conn.recv(1024).decode()
            nome = conn.recv(1024).decode()
            numero_clienti = conn.recv(1024).decode()
            dimensione = conn.recv(1024).decode()
            par = {"id_zona": id_modifica, "nome": nome, "numero_clienti": numero_clienti, "dimensione": dimensione}
            db_modifica_zona(par)

conn.close()
