import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 9000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

     # take input
    message = input(" -> ") 

    while message.lower().strip() != 'bye':
        print(client_socket.recv(1024).decode())
        print("Write w \n     Read r \n    q for quite  \n a for appending  \t")  # show in terminal
        message = input(" -> ") 
        client_socket.send(message.encode())  # send message
       # data = client_socket.recv(1024).decode()  # receive response
        #client_socket.send(s.encode())
        if message== 'r':
            print(client_socket.recv(1024).decode())
            client_socket.close()
        elif(message== 'q'):
                message3='q'
                client_socket.send(message3.encode())
        else:
            message1= input("Enter your text ")
            client_socket.send(message1.encode())
        # again take input
            if(message1== 'q'):
                message3="Closing connection"
                client_socket.send(message3.encode())
                client_socket.close()
            
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

