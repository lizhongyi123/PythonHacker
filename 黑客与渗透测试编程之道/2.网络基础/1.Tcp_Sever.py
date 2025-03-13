
import socket#套接字，插槽
# def main():
#     server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#开启服务
#     server.bind(("",7891))#开始监听端口
#     server.listen(3)#允许的最大客户端连接数
#     data, addr = server.accept()
#     print("连接的客户端ip为：\t", addr)
#     while True:
#         Data=data.recv(1024).decode()
#         print("服务器接受到的数据为：",Data)
#         if Data.lower()=="null":
#             print("服务器已关闭！\n")
#             break



    #server.listen(5)

import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 7891))
    server.listen(3)

    print("服务器启动，等待客户端连接...")
    conn, addr = server.accept()  # 正确获取连接对象
    print("连接的客户端 IP 为：", addr)

    while True:
        Data = conn.recv(1024).decode()  # 从连接中读取数据
        if not Data:  # 客户端断开连接时 recv 返回空字符串
            print("客户端断开连接，服务器关闭！")
            break

        print("服务器接受到的数据为：", Data)

        if Data.lower() == "null":  # 检查退出条件
            print("服务器已关闭！\n")
            break

    conn.close()  # 关闭客户端连接
    server.close()  # 关闭服务器

if __name__ == "__main__":
    main()