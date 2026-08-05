from datetime import datetime
import banco_peca

def cadastro_pecas():
    idPeca = int(input("Digite o id da peça: "))
    nomePeca = input("Digite o nome da peça: ")
    tipoPeca = input("Tipo: ")
    partePeca = input("Parte: ")
    frabricantePeca = input("Fabricante: ")
    codigoFabricacao = input("Código de fabricação: ")
    fornecedorPeca = input("Fornecedor: ")
    precoPeca = float(input("Digite o preço da peça: "))
    anoPeca = int(input("Digite o ano de fabricação da peça: "))
    tamanhoPeca = int(input("Digite o tamanho da peça em cm: "))
    quantidadePeca = int(input("Quantidade: "))
    idFuncionario = int(input("Id do funcionário: "))

    veiculos = [v.strip() for v in input("Veículos: ").split(",")]
    data = datetime.now().strftime("%Y-%m-%d")
    novoId = max((p["id"] for p in banco_peca.banco["pecas"]), default=0) + 1

    novaPecas = {
        "Id": idPeca,
        "Nome": nomePeca,
        "Tipo" : tipoPeca,
        "Parte" : partePeca,
        "Fabricante" : frabricantePeca,
        "Código de frabricação" : codigoFabricacao,
        "Fornecedor" : fornecedorPeca,
        "Preço": precoPeca,
        "Ano": anoPeca,
        "Tamanho": tamanhoPeca
        "Quantidade" : quantidadePeca,
        "Id funcionário" : idFuncionario,
    }
    
    banco_peca.banco["pecas".append(novaPecas)]

    print("Peça cadastrada com sucesso!")

def mostrar_ultima():
    if not banco_peca.banco["pecas"]:
        print("Nenhuma peça cadastrada.")
        return

    ultima = banco_peca.banco["pecas"][-1]

    print("\n---Última peça cadastrada---\n")
    print(f"ID: {ultima['id']}")
    print(f"Peça: {ultima['peca']}")
    print(f"Tipo: {ultima['tipo']}")
    print(f"Parte: {ultima['parte']}")
    print(f"Veículos: {', '.join(ultima['veiculos'])}")
    print(f"Fabricante: {ultima['fabricante']}")
    print(f"Código de fabricação: {ultima['codigo_fabricacao']}")
    print(f"Fornecedor: {ultima['fornecedor']}")
    print(f"Tamanho: {ultima['tamanho']}")
    print(f"Preço: R$ {ultima['preco']}")
    print(f"Quantidade: {ultima['quantidade']}")
    print(f"Data: {ultima['data_fabricacao']}")

while True:
    opcao = int(input("\n---MENU PY--- \n1- Cadastrar uma peça \n2- Mostrar última peça \n3- Sair\n"))

    match opcao:
        case 1:
            cadastrar_peca()
        case 2:
            mostrar_ultima()
        case 3:
            break
