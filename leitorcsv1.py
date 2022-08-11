import csv

# abrindo arquivo em python no modo leitura
with open("tecnico.csv", mode="r") as arqcsv:
    # passando arquivo texto csv para o leitor csv padrão do python
    leitor = csv.reader(arqcsv)
    # iterando cada linha para exibição
    for linha in leitor:
        print(linha)
