from socket import *
udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(('127.0.0.1',8888))#参数是二元元组
data,addr=udp_socket.recvfrom(1024)
print(addr,"收到消息：",data.decode())
n=udp_socket.sendto("服务端发送的消息".encode(),addr)
print(n)
"""
n = sockfd.sendto(data,addr)
功能： 发送UDP消息
参数： data  发送的内容 bytes格式
	  addr  目标地址
返回值：发送的字节数
"""
