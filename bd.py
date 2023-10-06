import socket

IP = ''
PORT = 1111

new_port = input('enter Host port: (Blank if default.): ')
if new_port != "\n":
    REMOTE_PORT = new_port

server = socket.socket()
server.bind((IP, PORT))

print('[+] Starting server')
print('[+] listening.. ')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to server')

while True:
    command = input('cmd: ')
    command = command.encode()
    client.send(command)
    output = client.recv(1024)
    output = output.decode()
    print(f'{output}')
