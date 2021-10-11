from base64 import b64decode
import socket, json
from aes import AESEncryption

client_socket = socket.socket()
port = 8080
client_socket.connect(('127.0.0.1',port))
#recieve connection message from server
recv_msg = client_socket.recv(1024).decode('utf-8')
b64 = json.loads(recv_msg)
iv = b64['iv']
cipher = b64['cipher']
msg = AESEncryption.decrypt(iv, cipher)
print(msg.decode('utf-8'))
#send user details to server
send_msg = input("Enter your user name(prefix with #):")
client_socket.send(send_msg.encode('utf-8'))
#receive and send message from/to different user/s
while True:
    recv_msg = client_socket.recv(1024)
    print(recv_msg.decode('utf-8'))
    send_msg = input("Send your message in format [@user:message] ")
    if send_msg == 'exit':
        break;
    else:
        client_socket.send(send_msg.encode("utf-8"))
client_socket.close()