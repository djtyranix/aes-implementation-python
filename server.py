from base64 import b64encode
import socket,select, json
from aes import AESEncryption
from rsa import RSAEncryption

port = 8080
socket_list = []
users = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('',port))
server_socket.listen(5)
socket_list.append(server_socket)

while True:
    ready_to_read,ready_to_write,in_error = select.select(socket_list,[],[],0)
    for sock in ready_to_read:
        if sock == server_socket:
            connect, addr = server_socket.accept()
            socket_list.append(connect)
            msg = "You are connected from:" + str(addr)
            iv, cipher = AESEncryption.encrypt(msg)
            result = json.dumps({'iv': iv, 'cipher': cipher})
            connect.send(result.encode('utf-8'))
        else:
            data = sock.recv(2048)
            if data.startswith(b"#"):
                username = data[1:].lower().decode('utf-8')
                users[username]=connect
                print("User " + username +" added.")

                RSAEncryption.generate_key(username)
                enc_key, key = RSAEncryption.get_session_key(username)

                msg = "Your user detail saved as : "+ username

                iv, cipher = AESEncryption.encrypt_with_key(msg, key)
                result = json.dumps({'iv': iv, 'cipher': cipher, 'rsa': b64encode(enc_key).decode('utf-8')})

                connect.send(result.encode('utf-8'))
            elif data.startswith(b"@"):
                json_str = data.decode('utf-8')[1:]
                b64 = json.loads(json_str)
                userIndex = b64['username'][1:]
                iv = b64['iv']
                cipher = b64['cipher']
                rsa = b64['rsa']
                result = json.dumps({'iv': iv, 'cipher': cipher, 'rsa': rsa})
                print(userIndex)
                users[userIndex].send(result.encode('utf-8'))
server_socket.close()