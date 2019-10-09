import socket
# import selectors
import os

class Servidor:
    """ Classe Servidor, esta classe cria e
        gerencia as operações do servidor
    """
    def __init__(self, port=6028, local=True, adrress=''):
        self.port = port
        self.host = 'localhost' if local else adrress
        self.socket = None
        self.files = []

    def server_start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen (5)
        print('Listening on {}:{}'.format(self.host, self.port))

    def file_send(self):
        conn, addr = self.socket.accept()
        with conn:
            print('{} conectado'.format(addr))
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    def file_recv(self):
        conn, addr = self.socket.accept()
        with conn:
            print('{} conectado'.format(addr))
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    def show_file(self):
        try:
            os.mkdir(path=r'Files')
        except OSError:
            pass

        self.files = []
        for _path, _, files in os.walk(os.path.abspath('Files_Servidor')):
            for file in files:
                self.files.append(_path, file)


def conect():
    port = 392817                    # Reserve a port for your service every new transfer wants a new port or you must wait.
    s = socket.socket()             # Create a socket object
    host = 'localhost'              # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.

    print( 'Server listening....')


    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))

        filename='TCPSERVER.py' #In the same folder or path is this file running must the file you want to tranfser to be
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
           conn.send(l)
           print('Sent ',repr(l))
           l = f.read(1024)
        f.close()

        print('Done sending')
        conn.send('Thank you for connecting')
        conn.close()

