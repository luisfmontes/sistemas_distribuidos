import os
from Server import Servidor


def startserver():
    resp = str(input('Deseja iniciar o Servidor nas configurações padroões [S/N] ?')).upper()
    if resp == 'S':
        Servidor()
    elif resp == 'N':
        tipo_servidor = input("1 - Local\n2 - Aberto")
    else:
        print('Esolha não identificada')


def startcliente():
    pass

def con():
    opcao = int(input("""\n
         ************************
         *     File Transfer    *
         ************************
         |  1 - Server          |
         |  2 - Client          |
         |  0 - Exit            |
         ************************         
         Opção: """))
    if opcao == 0:
        exit(0)
    elif opcao == 1:
        startserver()
    elif opcao == 2:
        startcliente()
    exit(0)


if __name__ == '__main__':
    con()
