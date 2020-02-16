import socket
s=socket.socket()
host=socket.gethostname()
port=9000
s.bind((host,port))
s.listen(1)
print("Waiting for connections")
conn1,addr=s.accept()
print("client 1 is connected")
c="Welcome i am server"
conn1.send(c.encode())
print("Waiting for 1 connection")
conn2,addr=s.accept()
print("client 2 is connected")
p="Welcome i am server you have to wait for while"
conn2.send(p.encode())
m=list()
m.append(conn1)
m.append(conn2)

while 1:
    try:
        for key in m:
            s=key.recv(1024).decode()
            if(s == 'w' or s =='W'):
                f=open("komal.txt",'w')
                sendd="Write in file::"
                key.send(sendd.encode())
                data4=key.recv(1024).decode()
                f.write(data4)
                f.close()
            elif(s=='r' or s=='R'):
                f=open("komal.txt",'rb')
                Buffer_size=4024
                flow=f.read(Buffer_size)
                key.sendall(flow)

            elif(s=='q' or s=='Q'):
                print("OK bye then")
                key.close()
                p="Client2 please start you operation"
                conn1.send(p.encode())
                conn2.send(p.encode())
                
            elif(s=='a' or s=='A'):
                f=open("komal.txt",'a')
                sendd1="append in file::"
                key.send(sendd1.encode())
                data4=key.recv(1024).decode()
                f.write(data4)
                f.close()
            else:
                sendd2="something went wrong"
                key.send(sendd2.encode())
            
            
    except e:
        print(e)
    
    

