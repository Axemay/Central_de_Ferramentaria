import csv

with open("escrita.csv", "a", encoding="utf8") as arquivo_csv:
    escrever = csv.writer(arquivo_csv, delimiter=",", lineterminator="\n")
    escrever.writerow(["Yanka", "Desenvolvedora Sênior"])