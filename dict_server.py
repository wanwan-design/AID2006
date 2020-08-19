from socket import *
import  pymysql
class Database:
    def __init__(self):
        self.db = pymysql.connect(
                            host="localhost",
                            port=3306,
                            user='root',
                            password='123456',
                            database='words',
                            charset='utf8'
                            )
        self.cur=self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def find_word(self,word):
        sql="select mean from word where word=%s;"
        self.cur.execute(sql,[word])
        result=self.cur.fetchone()
        if result:
            return result[0]
        else:
            return "Not Found"

def main():
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0",8888))
    db=Database()
    while True:
        word,addr=udp_socket.recvfrom(1024)#接受单词
        mean=db.find_word(word)
        udp_socket.sendto(mean.encode(),addr)#发送单词解释
    udp_socket.close()

if __name__ == '__main__':
    main()