def leiaInt(texto):
   """
   -> responsavel por validar dados inteiros somente.
   :param texto: o texto a ser mostrado ao usuario
   :return: retorna o valor inteiro validado.
   """
   valida = True
   while valida:
       try:
           num = int(input(texto))
       except:
           print(f'Erro: por favor, digite um número inteiro válido')
           continue
       else:
           return num


def linha():
    print('-' * 42)

def menu(lista):
    print(f'{" BANCO PYTHON ":=^32}', end='\n\n')
    opc = 1
    for item in lista:
        print(f'{opc} - {item}')
        opc += 1
    linha()
    while True:
        escolha = leiaInt('Sua opção: ')
        if escolha > 0 and escolha <= len(lista):
            return escolha
        else:
            print('Digite uma opção válida acima.')