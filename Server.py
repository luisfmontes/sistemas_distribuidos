import socket
import os


class Servidor:
    """ Classe Servidor, esta classe cria e
        gerencia as operações do servidor
    """
    def __init__(self, port=6028, local=True, adrress=''):
        self.port = port
        self.host = 'localhost' if local else adrress
        self.socket = None
        self.path_files = r'Files_Servidor'
        self.files = []
        for _path, _, files in os.walk(os.path.abspath(self.path_files)):
            for file in files:
                self.files.append(file)

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        print('Server: Listening on {}:{}'.format(self.host, self.port))

    def file_send(self, conn, file_name):
        with open('{}{}'.format(self.path_files, file_name), 'rb+') as f:
            data = f.read(1024)
            while data:
                print('Server: Sending data...')
                conn.send(data)
                data = f.read(1024)
        print('Server: file {} was send successfully'.format(file_name))

    def file_recv(self, conn, file_name):
        with open('{}{}'.format(self.path_files, file_name), 'wb+') as f:
            while True:
                print('Server: Receiving data...')
                recev = conn.recv(1024)
                if not recev:
                    break
                f.write(recev)
                f.close()
        print('Server: file {} was receved successfully'.format(file_name))


def server():
    s = Servidor()
    s.start()
    try:
        os.mkdir(path=s.path_files)
    except OSError:
        pass
    while True:
        connection, address = s.socket.accept()
        print('Server: Client {} connected'.format(address))
        with connection:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                try:
                    opc, file_name = str(data.decode()).split('-')
                except ValueError:
                    opc = str(data.decode())

                if opc == 'Show Files':
                    for file in s.files:
                        connection.send(file)
                elif opc == 'Transferir':
                    print('transferencia')
                    s.file_recv(connection, file_name)
                    connection.send(b'Server: Finishing Connection')
                    connection.close()
                elif opc == 'Download':
                    s.file_send(connection, file_name)
                    connection.send(b'Server: Finishing Connection')
                    connection.close()
                else:
                    print('Server: Receved {} from Client'.format(data))
    # except KeyboardInterrupt:
    #     print('Server: shutting down.....')


if __name__ == '__main__':
    server()
