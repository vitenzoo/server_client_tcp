import threading
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #determina o servidor 

    try:
        server.bind(("localhost", 7777)) #tenta ligar o servidor
        server.listen() #ouve todas as conexões que chegar
    except:
        return print("\nNão foi possível iniciar o servidor\n")
    
    while True:
        client, addr = server.accept() # aceita a requisição do usuário para se conectar   
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):  # tratamento de mensagens
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break


def broadcast(msg, client): #Transmissão de dados (msg=mensagem & client=quem enviou a mensagem)
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg) 
                #envia a mensagem para todos na lista clients que não seja o client qeu enviou a mensagem
            except:
                clients.remove(clientItem) 
                #se não conseguir enviar a mensagem para um cliente, remove pois ele não está mais conectado
                
                

def deleteClient(client):
    clients.remove(client)



main()