menu = '''
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair do Sistema
'''
saldo = 0
limite = 500
extrato = ''
número_saque = 0
LIMITE_SAQUES = 3

while True:
    usuário = input(f'Qual operação você deseja realizar? {menu}')
   
    if usuário == '1':
        valor = float(input('Informe o valor do Depósito: '))
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!\n")
           
        else:
            print('Valor inválido. Tente novamente!')
           
    elif usuário == '2':
        valor = float(input('Informe o valor do Saque: '))
       
        if valor > 0:
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = número_saque >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print('Operação Falhou! Você não tem saldo suficiente.\n')
               
            elif excedeu_limite:
                print('Operação Falhou! O valor do saque excedeu o limite proposto.\n')
            
            elif excedeu_saques:
                print('Operação Falhou! O número máximo de saques foi excedido.\n')
               
            else:
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                número_saque += 1
                print('Saque realizado com sucesso!\n')
               
        else:
            print('Operação falhou! O valor informado é inválido!\n')
           
    elif usuário == '3':
        print('\n==================== EXTRATO ====================')
        print('Não foram realizada transições.' if not extrato else extrato)
        print(f'\nSeu saldo atual é de R$ {saldo:.2f}\n')
        print('\n================================================')
       
    elif usuário == '4':
        print('Muito Obrigado por fazer parte do nosso Sistema Bancário. Até Breve!')
        break
   
    else:
        print('\nOpção Inválida! Por favor, selecione uma opção válida.')