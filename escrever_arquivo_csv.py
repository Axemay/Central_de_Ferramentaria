import csv

arquivo = open("escrita.csv", "a", newline="", encoding="utf-8")
escreve = csv.writer(arquivo, delimiter=",")
funcionario1 = ["Jose", "25", "Ativo"]
while True:
    cont = str(input("S/N")).lower()
    if cont in "sn":
        if cont == "s":
            escreve.writerow(funcionario1)
            print("Linha 3 escrita")
        else:
            break

arquivo.close()