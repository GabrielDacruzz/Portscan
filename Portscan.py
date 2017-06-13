import socket
ip = raw_input('digite o ip que desejado: ')
port = input('digite a porta desejada: ')
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
    print "porta",port,"esta aberta"
else:
    print "porta",port,"esta fechada"
