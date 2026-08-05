import pandas as pd
from menu import iniciar_menu

path = r"H:\Python\sistemaBancarioCSV\banco_5000_clientes.csv"
arquivo = pd.read_csv(path, sep = ",", encoding = "utf8")

arquivo['Deposito'] = ""

arquivo["Hora_deposito"] = ""

print(arquivo)



if __name__ == "__main__":
    iniciar_menu()