import socket
import os
import time
from datetime import datetime

HOST = '127.0.0.1'  # The Client's hostname or IP address
PORT = 65432  # The port used by the Client


def send():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(b'R')
    time.sleep(5)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print('Client: Trying to Connect to {}'.format(HOST, PORT))
        s.connect((HOST, PORT))
        print('Client: Sucesseful to Connect to {}'.format(HOST, PORT))

        file_name = 'SendServer.txt'
        if not os.path.isfile(os.path.join(path_file, file_name)):
            print('Client: File not Found')
            print('Client: Makeing a new file to send...')
            with open(os.path.join(path_file, file_name), 'w+') as f:
                for x in range(100):
                    data = 'line {}\n'.format(x)
                    f.write(data)

        print('Client: Ready to send the file')
        with open(os.path.join(path_file, file_name), 'rb+') as f:
            data = f.read(1024)
            while data:
                print('Client: Sending data...')
                s.send(data)
                data = f.read(1024)
        print('Client: file {} was send successfully'.format(file_name))
        print('Client: Closeing conection')
        time.sleep(5)


def recve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(b'S')
    time.sleep(5)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print('Client: Trying to Connect to {}'.format(HOST, PORT))
        s.connect((HOST, PORT))
        print('Client: Sucesseful to Connect to {}'.format(HOST, PORT))
        file_name = 'ReceveServer_{}.txt'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
        print('Client: Ready to receve the file')
        with open(os.path.join(path_file, file_name), 'wb') as f:
            while True:
                print('Client: Receiving data...')
                recev = s.recv(1024)
                if not recev:
                    break
                f.write(recev)
        print('Client: file {} was receved successfully'.format(file_name))
        print('Client: Closeing conection')
        time.sleep(5)


if __name__ == '__main__':
    path_file = r'arquivos_client'
    if not os.path.exists(path_file):
        os.makedirs(path_file)

    while True:
        option = int(input("""\n
                 ************************
                 *     File Transfer    *
                 ************************
                 |  1 - Send File       |
                 |  2 - Download File   |
                 |  0 - Exit            |
                 ************************
                 Option: """))
        if option == 0:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.send(b'C')
            break
        elif option == 1:
            send()
        elif option == 2:
            recve()
