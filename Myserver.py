import socket
import readTest
import writeTest
import threading
# 開啟ip和端口
ip_port = ('127.0.0.1', 9999)
# 生成一個socket對象
sk = socket.socket()
#sk=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP協定
# 綁定ip端口
sk.bind(ip_port)
# 最多連接數
sk.listen(5)
# 開啟死循環等待客戶端連接

print('服務器啟動...')
# 等待鏈接,阻塞，直到渠道鏈接 conn打開一個新的對象專門給當前鏈接的客戶端 addr是ip地址


def handle(conn, addr):

    try:
        client_data = conn.recv(1024)  # 獲取客戶端請求數據
        client_data = client_data.decode("utf-8")  # 轉換成utf-8格式
    except:
        conn.close()

    if 'write' in client_data:
        client_data = client_data.replace('write ', '', 1)
        writeTest.writeFile(client_data)
        print('get command:', 'write')
        print('write in:', client_data)
    elif client_data == 'bye':
        print('client disconnect')
        conn.close()
    # 打印對方的數據
    elif client_data == 'echo':
        getText = readTest.read_SendFile()
        send_text = conn.sendall(bytes(str(getText), "utf-8"))
    else:
        print('Command not find')

    # 向對方發送數據
    conn.send(bytes("伺服器收到了", "utf-8"))
    # 關閉鏈接

    conn.close()
while True:
    conn, addr = sk.accept()
    threading._start_new_thread(handle, (conn, addr))  # 5、多執行緒處理客戶端訊息
