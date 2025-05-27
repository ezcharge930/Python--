import socket
# 创建socket对象
sk = socket.socket()
# 绑定ip和端口
sk.bind(('0.0.0.0', 8995))
# 设置监听
sk.listen(5)
# 等待客户端连接
conn,addr = sk.accept()

print(conn)
print(addr)

while True:
    accept_data = conn.recv(1024)
    print("客户端发送的数据：", accept_data.decode('utf-8'))
    send_data = '服务器已收到数据'
    conn.send(send_data.encode('utf-8'))

