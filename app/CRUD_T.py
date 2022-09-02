from csv import writer, reader
from csv import DictWriter, DictReader
import re
from tkinter import Tk
from typing import Dict
import new_T


class Csv :

    def leitor(self):
        with open('./tecnico.csv') as self.file:
            self.csv_reader = reader(self.file)
            self.data = list(self.csv_reader)

            for row in self.data:


                return self.data

            #     return row

    def append(self, cpf, nome, telefone, turno, equipe):
        # with open('./appcsv.csv') as self.file:
        #     self.csv_Dreader = DictReader(self.file)
        #     self.data2 = list(self.csv_Dreader)
        with open('./tecnico.csv', 'a', newline="") as self.file:
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
        with open('./tecnico.csv') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./tecnico.csv', 'w') as self.file:
            header = ("cpf", "nome", "telefone", "turno", "equipe")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            for row in self.data:
                if row['cpf'] == cpf and row['nome'] == nome:
                    continue

                self.csv_Dwriter.writerow(row)



    def update(self, cpf, nome, telefone, turno, equipe):
        with open('./tecnico.csv') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./tecnico.csv', 'w') as self.file:
            header = ("cpf", "nome", "telefone", "turno", "equipe")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()

            try:
                for row in self.data:
                    if row['cpf'] == cpf or row['nome'] == nome:
                            #or row['nome'] == nome or row['cpf'] == cpf or row['item'] == item:
                        row['cpf'] = cpf
                        row['nome'] = nome
                        row['telefone'] = telefone
                        row['turno'] = turno
                        row['equipe'] = equipe
                    self.csv_Dwriter.writerow(row)
            except Exception as e:
                print('erro ao atualizar: ', e)

    def busca_pessoa(self, nome_buscado):

        with open('./tecnico.csv') as self.file:

            self.csv_Dreader = reader(self.file)
            self.data = list(self.csv_Dreader)

        for pessoa in self.data:
            col1, col2, col3, col4, col5 = pessoa

            # if nome_buscado == f'{col1}':
            #     yield (pessoa)
            # if nome_buscado == f'{col2}':
            #     yield (pessoa)
            # if nome_buscado == f'{col3}':
            #     yield (pessoa)
            if nome_buscado == f'{col4}':
                yield (pessoa)
            ###### pesquisa regex
            regex = re.compile(fr'{col1}', flags=re.I)
            regex2 = re.compile(fr'{col2}', flags=re.I)
            regex3 = re.compile(fr'{col3}', flags=re.I)
            regex4 = re.compile(fr'{col4}', flags=re.I)
            regex5 = re.compile(fr'{col5}', flags=re.I)

            if regex.findall(nome_buscado):
                yield (pessoa)

            if regex2.findall(nome_buscado):
                yield (pessoa)

            if regex3.findall(nome_buscado):
                yield (pessoa)


            if regex5.findall(nome_buscado):
                yield (pessoa)

        return {}


if __name__ == '__main__':
    TEST = Csv()