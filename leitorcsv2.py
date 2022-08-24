import csv

arquivo = csv.reader(open("tecnico.csv"), delimiter=",")
for [CPF, Nome, Telefone, Turno, Equipe] in arquivo:
    print(f"{CPF} - {Nome} - {Telefone} - {Turno} - {Equipe}")
    
teste = arquivo[CPF]
print(teste)   