def leiaFloat(texto):
   """
   -> responsavel por validar dados float somente.
   :param texto: o texto a ser mostrado ao usuario
   :return: retorna o valor float validado
   """
   valida = True
   while valida:
       try:
           num = float(input(texto))
       except:
           print(f'Erro: por favor, digite um número válido.')
           continue
       else:
           return num


def depositar(saldo, extrato):
    while True:
        deposito = leiaFloat('Qual valor do deposito? ')
        if deposito > 0:
            saldo += deposito
            extrato.append(f'Deposito: R${deposito:.2f}')
            print('Deposito realizado com sucesso!')
            return saldo
        else:
            print('Deposite um valor maior que 0.')


def sacar(saldo, extrato):
    if saldo > 0:
        while True:
            saque = leiaFloat('Qual valor para saque? ')
            if saque > 0 and saque <= saldo:
                saldo -= saque
                extrato.append(f'Saque: R${saque:.2f}')
                print('Saque realizado com sucesso!')
                return saldo
            else:
                if saque <= 0:
                    print(f'Informe um valor de saque maior que R$0')
                else:
                    print(f'Saque R${saque:.2f} excede o valor de saldo R${saldo:.2f}')
    else:
        print(f'Saldo R${saldo}. Deposite para poder sacar')


def mostrar_extrato(saldo, extrato):
    print(f'{" EXTRATO ":=^32}')
    if len(extrato) == 0:
        print('Não foram realizadas movimentações.')
    for mov in extrato:
        print(f'{mov}')
    mostrar_saldo(saldo)


def mostrar_saldo(saldo):
    print(f'Saldo atual: R${saldo:.2f}')