import socket
import os
from datetime import datetime

TYPECONN = None


def typeconn(s):
    global TYPECONN
    conn, addr = s.accept()
    with conn:
        TYPECONN = conn.recv(1024)


def receve(s):
    conn, addr = s.accept()
    with conn:
        print('Server: Connected to {}'.format(addr))
        file_name = 'RecevedClient_{}.txt'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
        print('Server: Ready to receve the file')
        with open(os.path.join(path_file, file_name), 'wb') as f:
            while True:
                print('Server: Receiving data...')
                recev = conn.recv(1024)
                if not recev:
                    break
                f.write(recev)
        print('Server: file {} was receved successfully'.format(file_name))


def send(s):
    conn, addr = s.accept()
    with conn:
        file_name = 'SendClient.txt'
        if not os.path.isfile(os.path.join(path_file, file_name)):
            print('Server: File not Found')
            print('Server: Makeing a new file to send...')
            with open(os.path.join(path_file, file_name), 'w+') as f:
                for x in range(100):
                    data = 'line {}\n'.format(x)
                    f.write(data)

        print('Server: Ready to send the file')
        with open(os.path.join(path_file, file_name), 'rb+') as f:
            data = f.read(1024)
            while data:
                print('Server: Sending data...')
                conn.send(data)
                data = f.read(1024)
        print('Server: file {} was send successfully'.format(file_name))


if __name__ == '__main__':

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    path_file = r'arquivos_servidor'
    if not os.path.exists(path_file):
        os.makedirs(path_file)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Server: Listening on {}:{}'.format(HOST, PORT))
        print('Server: Waiting new Conection...')
        while True:
            if TYPECONN is None:
                typeconn(s)
            elif TYPECONN == b'C':
                print('Server: Stop Service')
                break
            elif TYPECONN == b'R':
                try:
                    receve(s)
                except ConnectionAbortedError:
                    print('Server: Conection Lost')
                    pass
                TYPECONN = None
                print('Server: Closeing conection')
                print('Server: Waiting new Conection...')
            elif TYPECONN == b'S':
                try:
                    send(s)
                except ConnectionAbortedError:
                    print('Server: Conection Lost')
                    pass
                TYPECONN = None
                print('Server: Closeing conection')
                print('Server: Waiting new Conection...')