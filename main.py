from lib.menu import *
from lib.banco import *


saldo = 0
extrato = []


while True:
    opc = menu(['Depositar', 'Sacar', 'Extrato', 'Saldo', 'Sair'])
    if opc == 1:
        saldo = depositar(saldo, extrato)
        print()
    elif opc == 2:
        saldo = sacar(saldo, extrato)
        print()
    elif opc == 3:
        mostrar_extrato(saldo, extrato)
        print()
    elif opc == 4:
        mostrar_saldo(saldo)
        print()
    elif opc == 5:
        print('Volte sempre!')
        break