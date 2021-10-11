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
                users[data[1:].lower().decode('utf-8')]=connect
                print("User " + data[1:].decode('utf-8') +" added.")
                RSAEncryption.generate_key(data[1:].decode('utf-8'))
                msg = "Your user detail saved as : "+str(data[1:].decode('utf-8'))
                connect.send(msg.encode('utf-8'))
            elif data.startswith(b"@"):
                user = data.rpartition(b':')[0]
                msg = data.rpartition(b':')[2]
                userIndex = user[1:].lower()
                print(userIndex.decode('utf-8'))
                print(msg.decode('utf-8'))
                users[userIndex.decode('utf-8')].send(msg)
server_socket.close()