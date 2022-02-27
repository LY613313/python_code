import socket

ip = '192.168.123.189' # 要改为被控端的IP，对方要在同一局域网内
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

while True:
    data = input("please input command：")
    data = bytes(data, encoding="utf8")
    s.send(data)  # 发送数据给对方
    data2 = s.recv(1024)  # 接收返回的数据
    print(str(data2, encoding="utf8"))
    if data == b"exit":
        print("disconnect!")
        break

s.close()
