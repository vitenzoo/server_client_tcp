import threading #multi-threads = processos que rodam paralelamente
import socket 

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777)) 
        #tenta se conectar com o servidor e a porta indicados

    except Exception as dfsf:
        return print("\nNão foi posivel se conectar ao servidor!\n")
        print(error)
    


    username = input("Usuário> ")
    print('\nConectato')


    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2  = threading.Thread(target=sendMessages, args=[client, username])
    #Roda as duas funções ao mesmo tempo
    thread1.start()
    thread2.start()
    

def receiveMessages(client): #Receber Mensagens 
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')#<- bytes
            print(msg+'\n')
        except:
            print("Não foi possível permanecer conectado no servidor\n")
            print("Pressione Enter para continuar...")
            client.close()
            break
            

def sendMessages(client, username): #Eviar Mensagens
    while True: 
        try:
            msg = input("\n")
            client.send(f"<{username}> {msg} ".encode("utf-8")) #mesma coisa que .format      
        except:
             return

main()