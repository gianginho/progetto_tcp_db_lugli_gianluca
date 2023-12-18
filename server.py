import socket
import mysql.connector

PASSWORD = "iuji"

connes = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="progetto",
    port=3306
)
cur = connes.cursor()

def setCRUD(parametri):
    clausole = ""
    for key, value in parametri.items():
        clausole += f"and {key} = '{value}' "
    
    return clausole

def lettura(parametri, x):
    query = ''
    if x == 1:
        query = f"SELECT * FROM dipendente where 1=1 {setCRUD(parametri)}"
    if x == 2:
        query = f"SELECT * FROM zona_lavoro where 1=1 {setCRUD(parametri)}"

    cur.execute(query)
    dati = cur.fetchall()
    return dati

def elimina(parametri, x):
    query = ''
    if x == 1:
        query = f"DELETE FROM dipendente where 1=1 {setCRUD(parametri)}"
    if x == 2:
        query = f"DELETE FROM zona_lavoro where 1=1 {setCRUD(parametri)}"

    cur.execute(query)
    connes.commit()

def scrittura(parametri, x):
    query = ''
    if x == 1:
        query = f"INSERT INTO dipendente (nome, cognome, pos_lavorativa, data_nascita, stipendio) VALUES ('{lista[0]}','{lista[1]}','{lista[2]}','{lista[3]}','{lista[4]}')"
    if x == 2:
        query = f"INSERT INTO zona_lavoro (nome_zona, numero_clienti, Distretto) VALUES ('{lista[0]}','{lista[1]}','{lista[2]}')"
    cur.execute(query)
    connes.commit()

def modifica(par, x):
    query = ''
    if x == 1:
        query = f"UPDATE dipendente SET nome = '{lista[0]}', cognome = '{lista[1]}', pos_lavorativa = '{lista[2]}', data_nascita = '{lista[3]}', stipendio = '{lista[4]}' WHERE id_d = '{lista[5]}'"
    if x == 2:
        query = f"UPDATE zona_lavoro SET nome_zona = '{lista[0]}', numero_clienti = '{lista[1]}', Distretto = '{lista[2]}' WHERE id_z = '{lista[3]}'"
    cur.execute(query)
    connes.commit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8888))
s.listen()

print("In attesa di connessioni...")

conn, addr = s.accept()
print('Connected by', addr)
if __name__ == '__main__':
    for i in range(3):
        password = conn.recv(1024).decode()
        if password == PASSWORD:
            conn.send("Password corretta.".encode())
            break
        else:
            if i < 3:
                conn.send(f"Password errata.\n".encode())
            else:
                conn.send("Tentativi finiti, connessione chiusa.".encode())
                conn.close()
                exit()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break  
        if data == "5":
            break  

        if data == "1":
            scelta = conn.recv(1024).decode()
            nome = conn.recv(1024).decode()
            if scelta == "1":
                par = {"nome": nome}
            else:
                par = {"nome_zona": nome}
            result = lettura(par, int(scelta))
            conn.send(str(result).encode())
            
        elif data == "2":
            scelta = conn.recv(1024).decode()
            id_elimina = conn.recv(1024).decode()
            if scelta == "1":
                par = {"id_d": id_elimina}         
            else:
                par = {"id_z": id_elimina}
            elimina(par, int(scelta))

        elif data == "3":
            scelta = conn.recv(1024).decode()
            lista = []
            if scelta == "1":
                for i in range(5):
                    lista.append(conn.recv(1024).decode())
                par = {"nome": lista[0], "cognome": lista[1], "pos_lavorativa": lista[2], "data_nascita": lista[3], "stipendio": lista[4]}
                
            else:
                for i in range(3):
                    lista.append(conn.recv(1024).decode())
                par = {"nome_zona": lista[0], "numero_clienti": lista[1], "Distretto": lista[2]}
            scrittura(par, int(scelta))

        elif data == "4":

            scelta = conn.recv(1024).decode()
            if scelta == "1":
                for i in range(6):
                    lista.append(conn.recv(1024).decode())
                par = {"id_d": lista[0], "nome": lista[1], "cognome": lista[2], "pos_lavorativa": lista[3], "data_nascita": lista[4], "stipendio": lista[5]}
                
            else:
                for i in range(4):
                    lista.append(conn.recv(1024).decode())
                par = {"id_z": lista[0], "nome_zona": lista[1], "numero_clienti": lista[2], "Distretto": lista[3]}

            modifica(par, int(scelta))

    conn.close()