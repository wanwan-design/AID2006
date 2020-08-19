import socket
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=('127.0.0.1',8888)
msg=input("<<<")
udp_socket.sendto(msg.encode(),address)
data,addr=udp_socket.recvfrom(1024)
print("从服务端收到：",data.decode())
udp_socket.close()
