import socket
import os
import time


class Client:
    """ Classe Client, esta classe cria e
        gerencia as operações do servidor
    """
    def __init__(self, host='localhost', port=6028):
        self.port = port
        self.host = host
        self.socket = None
        self.path_files = r'Files_Client/'
        self.files = []
        for _path, _, files in os.walk(os.path.abspath(self.path_files)):
            for file in files:
                self.files.append(file)

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        # self.socket.send(b'Hello server!')

    def file_send(self, file_name):
        # self.connect()
        # time.sleep(20)
        self.socket.send(('Transferir - {}'.format(file_name)).encode())
        time.sleep(10)
        with open('{}{}'.format(self.path_files, file_name), 'rb+') as f:
            data = f.read(1024)
            while data:
                print('Client: Sending data...')
                self.socket.send(data)
                data = f.read(1024)
        print('Client: file {} was send successfully'.format(file_name))

    def file_recv(self, file_name):
        with open('{}{}'.format(self.path_files, file_name), 'wb+') as f:
            while True:
                print('Client: Receiving data...')
                recev = self.socket.recv(1024)
                if not recev:
                    break
                f.write(recev)
        print('Client: file {} was receved successfully'.format(file_name))


def client():
    c = Client()
    c.connect()
    try:
        os.mkdir(path=c.path_files)
    except OSError:
        pass

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
        exit(0)
    elif option == 1:
        print('Clinet: Files available ')
        for index, file in enumerate(c.files):
            print('File {}: {}'.format(index, file))
        index = int(input('File number: '))
        c.file_send(c.files[index])
    elif option == 2:
        exit(0)


    # try:
    #     while True:
    #         connection, address = s.socket.accept()
    #         with connection:
    #             print('Server: {} conectado'.format(address))
    #             while True:
    #                 data = connection.recv(1024)
    #                 if not data:
    #                     break
    #             opc, file_name = str(data).split('-')
    #             if opc == 'Show Files':
    #                 for file in s.files:
    #                     connection.send(file)
    #             elif opc == 'Transferir':
    #                 s.file_recv(connection, file_name)
    #                 connection.send(b'Server: Finishing Connection')
    #                 connection.close()
    #             elif opc == 'Download':
    #                 s.file_send(connection, file_name)
    #                 connection.send(b'Server: Finishing Connection')
    #                 connection.close()
    #             else:
    #                 print('Server: Receved {} from Client', repr(data))
    # except KeyboardInterrupt:
    #     print('Server: shutting down.....')


if __name__ == '__main__':
    client()
