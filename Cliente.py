import socket
import os


class Client:
    """ Classe Client, esta classe cria e
        gerencia as operações do servidor
    """
    def __init__(self, host='localhost', port=6028):
        self.port = port
        self.host = host
        self.socket = None
        self.path_files = r'Files_Client'
        self.files = []

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.send(b'Hello server!')

    def show_file(self):
        try:
            os.mkdir(path=self.path_files)
        except OSError:
            pass

        self.files = []
        for _path, _, files in os.walk(os.path.abspath(self.path_files)):
            for file in files:
                self.files.append(_path, file)


def client():
    c = Client()
    c.connect()


if __name__ == '__main__':
    client()
