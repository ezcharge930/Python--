import socket
# 创建一个socket对象
sk = socket.socket()
# 连接服务器
sk.connect(('127.0.0.1',8995))

while True:
    send_data = input("请输入要发送的数据：")
    # 发送数据到服务器
    sk.send(send_data.encode('utf-8'))
    # 等待服务器的响应
    accept_data = sk.recv(1024)
    # 解码并打印服务器响应
    print("服务器响应：", accept_data.decode('utf-8'))
    