import re
from tkinter import Tk
from typing import Dict
import tecnico

from csv import DictWriter, DictReader
from csv import reader


class Csv():

    def leitor(self):
        with open('./tecnico.csv', encoding='utf-8') as self.file:
            self.csv_reader = reader(self.file)
            self.data = list(self.csv_reader)

            for row in self.data:


                return self.data

            #     return row

    def append(self, cpf, nome, telefone, turno, equipe):
        # with open('./appcsv.csv') as self.file:
        #     self.csv_Dreader = DictReader(self.file)
        #     self.data2 = list(self.csv_Dreader)
        with open('./tecnico.csv', 'a', newline="", encoding='utf-8') as self.file:
            header = ("cpf", "nome", "telefone", "turno", "equipe")
            #pulo = "\n"
            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator="\n" )

            data = ({'cpf' : cpf,
                    'nome' : nome,
                     'telefone' : telefone,
                     'turno' : turno,
                     'equipe' : equipe })


            #self.csv_Dwriter.writerows(self.data2)
            self.csv_Dwriter.writerow(data)
            #self.csv_Dwriter.writerows(data)

    def delet(self,cpf, nome):
        with open('./tecnico.csv', encoding='utf-8') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./tecnico.csv', 'w', encoding='utf-8') as self.file:
            header = ("cpf", "nome", "telefone", "turno", "equipe")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            for row in self.data:
                if row['cpf'] == cpf and row['nome'] == nome:
                    continue

                self.csv_Dwriter.writerow(row)

    def update(self, cpf, nome, telefone, turno, equipe):
        with open('./tecnico.csv', encoding='utf-8') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./tecnico.csv', 'w', encoding='utf-8') as self.file:
            header = ("cpf", "nome", "telefone", "turno", "equipe")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()

            try:
                for row in self.data:
                    if row['cpf'] == cpf :
                            #or row['nome'] == nome or row['cpf'] == cpf or row['item'] == item:
                       #row['cpf'] = cpf
                        row['nome'] = nome
                        row['telefone'] = telefone
                        row['turno'] = turno
                        row['equipe'] = equipe
                    self.csv_Dwriter.writerow(row)
            except Exception as e:
                print('erro ao atualizar: ', e)

    def busca_pessoa(self, nome_buscado):

        with open('./tecnico.csv', encoding='utf-8') as self.file:

            self.csv_Dreader = reader(self.file)
            self.data = list(self.csv_Dreader)

        for pessoa in self.data:
            col1, col2, col3, col4, col5 = pessoa

            if nome_buscado == f'{col1}':
                yield (pessoa)
            # if nome_buscado == f'{col2}':
            #     yield (pessoa)
            if nome_buscado == f'{col3}':
                yield (pessoa)
            if nome_buscado == f'{col4}':
                yield (pessoa)
            if nome_buscado == f'{col5}':
                yield (pessoa)
            ###### pesquisa regex
            regex = re.compile(fr'{col2}', flags=re.I)


            if regex.findall(nome_buscado):
                yield (pessoa)



        return {}

    def busca_cpf(self, nome_buscado):

        with open('./tecnico.csv', encoding='utf-8') as self.file:

            self.csv_Dreader = reader(self.file)
            self.data = list(self.csv_Dreader)

        for pessoa in self.data:
            col1, col2, col3, col4, col5 = pessoa

            if nome_buscado == f'{col1}':
                yield (pessoa)

        return {}

if __name__ == '__main__':
    TEST = Csv()
