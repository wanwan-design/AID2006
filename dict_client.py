from socket import *
#服务端地址写好
address=("127.0.0.1",8888)
#创建udp套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)
#输入什么发送什么
while True:
    word=input("word:")
    if not word:
        break
    # 发送UDP消息
    udp_socket.sendto(word.encode(),address)
    #接受udp消息
    data,addr=udp_socket.recvfrom(1024)
    print(word,"：",data.decode())
udp_socket.close()

