import socket
# 鏈接服務端ip和端口
ip_port = ('127.0.0.1',9999)
# 生成一個socket對象
client = socket.socket()
# 請求連接服務端
client.connect(ip_port)
# 發送數據
# 也可寫成sk.send("hello,服務器".encode("utf-8"))

while 1:
    cmd=input()
    if cmd=='bye':
        print('this is bye')
        client.send(bytes(cmd,"utf-8"))
        client.close() # 關閉連接
        break
    try:
        client.send(bytes(cmd,"utf-8"))
    except :
        print('伺服器中斷了')
        client.close()

    # 接受數據
    server_reply = client.recv(1024)
    # 打印接受的數據
    print(server_reply.decode("utf-8"))

