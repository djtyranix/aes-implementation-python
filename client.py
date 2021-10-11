from base64 import b64decode, b64encode
import socket, json
from aes import AESEncryption
from rsa import RSAEncryption

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
username = send_msg[1:].lower()
client_socket.send(send_msg.encode('utf-8'))
#receive and send message from/to different user/s
while True:
    recv_msg = client_socket.recv(1024).decode('utf-8')
    b64 = json.loads(recv_msg)
    iv = b64['iv']
    cipher = b64['cipher']
    enc_key = b64decode(b64['rsa'])
    key = RSAEncryption.decrypt_session_key(username, enc_key)
    msg = AESEncryption.decrypt_with_key(iv, cipher, key)
    print(msg.decode('utf-8'))
    send_msg = input("Send your message in format [@user:message] ")
    if send_msg == 'exit':
        break;
    else:
        user = send_msg.rpartition(':')[0]
        msg = send_msg.rpartition(':')[2]
        enc_key, key = RSAEncryption.get_session_key(username)
        iv, cipher = AESEncryption.encrypt_with_key(msg, key)
        result = "@" + json.dumps({'username': user, 'iv': iv, 'cipher': cipher, 'rsa': b64encode(enc_key).decode('utf-8')})
        client_socket.send(result.encode("utf-8"))
client_socket.close()