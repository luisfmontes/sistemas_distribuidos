import os
from Server import Servidor

if __name__ == '__main__':
    server = Servidor().start()

    # opcao = int(input("""\n
    #      ************************
    #      *     File Transfer    *
    #      ************************
    #      |  1 - Server          |
    #      |  2 - Client          |
    #      |  0 - Exit            |
    #      ************************
    #      Opção: """))
    # if opcao == 0:
    #     exit(0)
    # elif opcao == 1:
    #     startserver()
    # elif opcao == 2:
    #     startcliente()
    exit(0)
