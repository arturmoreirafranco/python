import csv
import os

ARQUIVO = 'banco_5000_clientes.csv'

def carregar_dados():
    contas = []
    if not os.path.exists(ARQUIVO):
        return contas
    with open(ARQUIVO, mode='r', newline='', encoding='utf-8') as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            linha['saldo'] = float(linha['saldo'])
            contas.append(linha)
    return contas

def salvar_dados(contas):
    with open(ARQUIVO, mode='w', newline='', encoding='utf-8') as f:
        campos = ['nome', 'cpf', 'conta', 'saldo']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(contas)

def buscar_conta(contas, numero):
    for c in contas:
        if c['conta'] == numero:
            return c
    return None

def realizar_deposito(contas):
    numero = input("Número da conta: ")
    c = buscar_conta(contas, numero)
    if c:
        valor = float(input("Valor do depósito: R$ "))
        c['saldo'] += valor
        print(f"Depósito realizado! Novo saldo de {c['nome']}: R$ {c['saldo']:.2f}")
        salvar_dados(contas)
    else:
        print("Conta não encontrada.")

def realizar_saque(contas):
    numero = input("Número da conta: ")
    c = buscar_conta(contas, numero)
    if c:
        valor = float(input("Valor do saque: R$ "))
        if valor <= c['saldo']:
            c['saldo'] -= valor
            print(f"Saque realizado! Novo saldo de {c['nome']}: R$ {c['saldo']:.2f}")
            salvar_dados(contas)
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

def iniciar_menu():
    contas = carregar_dados()
    while True:
        print("\n--- SISTEMA BANCÁRIO ---")
        print("1. Buscar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            num = input("Número da conta: ")
            c = buscar_conta(contas, num)
            if c:
                print(f"\nTitular: {c['nome']}")
                print(f"CPF: {c['cpf']}")
                print(f"Saldo: R$ {c['saldo']:.2f}")
            else:
                print("Conta não encontrada.")
        elif opcao == '2':
            realizar_deposito(contas)
        elif opcao == '3':
            realizar_saque(contas)
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")