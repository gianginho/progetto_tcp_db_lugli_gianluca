import socket
import sys

HOST = 'localhost' 
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def login():
    for i in range(3):
        password = input("Inserisci la password: ")
        s.send(password.encode())
        response = s.recv(1024).decode()
        if response == "Password corretta.":
            print('Password corretta.\n')
            break
        else:
            print(response)
            if i == 2: 
                s.close()
                sys.exit()

def menu():
    print("\nOperazioni disponibili:")
    print("1. Leggi dati di una tabella")
    print("2. Elimina un'istanza di una tabella")
    print("3. Inserisci un'istanza nella tabella")
    print("4. Modifica un dato di una tabella")
    print("5. Esci")    

def dati_dip():
    s.send(input("Inserisci il nome del dipendente: ").encode())
    s.send(input("Inserisci il cognome del dipendente: ").encode())
    s.send(input("Inserisci il lavoro del dipendente: ").encode())
    s.send(input("Inserisci la data di nascita del dipendente: ").encode())
    s.send(input("Inserisci lo stipendio del dipendente: ").encode())    

def dati_zona():
    s.send(input("Inserisci il nome della zona: ").encode())
    s.send(input("Inserisci il numero dei clienti della zona: ").encode())
    s.send(input("Inserisci il numero del distretto in cui è la zona: ").encode())

if __name__ == '__main__':
    login()

    while True:
        menu()

        scelta = input("Operazione: ")
        s.send(scelta.encode())

        if scelta == "5":
            print("\nPagina chiusa.\n")
            break

        if scelta == "1":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per leggere dipendenti o 2 per le zone: ")

            s.send(scelta2.encode())

            if scelta2 == "1":
                nome_d = input("Inserisci il nome del dipendente: ")
                s.send(nome_d.encode())
                response = s.recv(1024).decode()
                print(response)
            else:
                nome = input("Inserisci il nome della zona: ")
                s.send(nome.encode())
                response = s.recv(1024).decode()
                print(response)

        if scelta == "2":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per eliminare dipendenti o 2 per eliminare zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                id_elimina = input("Inserisci l'id del dipendente da eliminare: ")
                s.send(id_elimina.encode())
            else:
                id_elimina = input("Inserisci l'id della zona da eliminare: ")
                s.send(id_elimina.encode())

        if scelta == "3":

            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per inserire dipendenti o 2 per inserire zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                dati_dip()
            else:
                dati_zona()
                
        if scelta == "4":
            scelta2 = 0
            while(scelta2 != "1" and scelta2 != "2"):
                scelta2=input("Inserisci 1 per modificare dipendenti o 2 per modificare zone: ")

            s.send(str(scelta2).encode())

            if scelta2 == "1":
                id_modifica = input("Inserisci l'id del dipendente: ")
                s.send(id_modifica.encode())
                dati_dip()
            else:
                id_modifica = input("Inserisci l'id della zona: ")
                s.send(id_modifica.encode())
                dati_zona()

    s.close()