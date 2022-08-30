from csv import writer, reader
from csv import DictWriter, DictReader
from pprint import pprint
import re
from tkinter import *
import tkinter as tk
from tkinter import ttk




class csv :
    # def leitor_dict(self):
    #     with open('./users.csv') as self.file:
    #         self.csv_Dreader = DictReader(self.file)
    #         self.data = list(self.csv_Dreader)
    #
    #         for row in self.data:
    #             print(row)
    #             return self.data

    # def leitura(self):
    #     self.leitura = open("users.csv", 'r')
    #     for linha in self.leitura.readlines():
    #         print(linha)
    #         return linha
    #     self.leitura.close()

    def inserir_linhas(self):
        with open('./users.csv', 'w') as self.file:
            self.csv_writer = writer(self.file, lineterminator='\n')
            header = ('First Name', 'Last Name', 'Age')
            data = (('Rafa', 'Altero', 25),
                    ('Renan', 'Altero', 28),
                    ('Arai', 'Gohara', 49))

            self.csv_writer.writerow(header)
            self.csv_writer.writerows(data)
            # for row in data:
            #   csv_writer.writerow(row)

    def inserir_Dict(self, leitor):
        with open('./users.csv', leitor) as self.file:
            header = ('First Name', 'Last name', 'Age')

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            #data = ({'First Name': 'Rafa',
            #         'Last name': 'Altero',
            #         'Age': 25},
            #        {'First Name': 'Renan',
             ##        'Age': 28},
             #       {'First Name': 'Arai',
               #      'Last name': 'Gohara',
              #       'Age': 49})

            #self.csv_Dwriter.writeheader()
            # csv_Dwriter.writerow({'First Name' : 'Bala',
            #                      'Last name' : 'faca',
            #                     'Age' : 20})
            #self.csv_Dwriter.writerows(data)

    def leitor(self):
        with open('./appcsv.csv') as self.file:
            self.csv_reader = reader(self.file)
            self.data = list(self.csv_reader)

            for row in self.data:


                return self.data
            #     return row


    def append(self, codigo, nome, cpf, item):
        # with open('./appcsv.csv') as self.file:
        #     self.csv_Dreader = DictReader(self.file)
        #     self.data2 = list(self.csv_Dreader)
        with open('./appcsv.csv', 'a') as self.file:
            header = ('codigo', 'nome', 'cpf', 'item')
            #pulo = "\n"
            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator="\n" )

            data = ({'codigo' : codigo,
                    'nome' : nome,
                     'cpf' : cpf,
                     'item' : item})

            #self.csv_Dwriter.writerows(self.data2)
            self.csv_Dwriter.writerow(data)
            #self.csv_Dwriter.writerows(data)

    def delet(self, codigo):
        with open('./appcsv.csv') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./appcsv.csv', 'w') as self.file:
            header = ('codigo', 'nome', 'cpf', 'item')

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            for row in self.data:
                if row['codigo'] == codigo:
                    continue

                self.csv_Dwriter.writerow(row)

    def update(self, codigo, nome, cpf, item):
        with open('./appcsv.csv') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./appcsv.csv', 'w') as self.file:
            header = ('codigo', 'nome', 'cpf', 'item')

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            try:
                for row in self.data:
                    if row['codigo'] == codigo :
                            #or row['nome'] == nome or row['cpf'] == cpf or row['item'] == item:
                        #row['codigo'] = codigo
                        row['nome'] = nome
                        row['cpf'] = cpf
                        row['item'] = item
                    self.csv_Dwriter.writerow(row)
            except Exception as e:
                print('erro ao atualizar: ', e)

    def buscar(self, codigo):
        with open('./appcsv.csv') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)


            for row in self.data:
                if row['codigo'] == codigo:
                    return row

# with open('./appcsv.csv') as file:
#     csv_Dreader = DictReader(file)
#     data = list(csv_Dreader)
# with open('./appcsv.csv', 'w') as file:
#     header = ('codigo', 'nome', 'cpf', 'item')
#
#     csv_Dwriter = DictWriter(file, fieldnames=header, lineterminator='\n')
#
#     csv_Dwriter.writeheader()
#     for row in data:
#         if row['codigo'] == '3' and row['nome'] == 'arai'  :
#             row['codigo'] = '555'
#             row['nome'] = 'marquinho'
#             row['cpf'] = 444
#             row['item'] = 'mmm'
#         csv_Dwriter.writerow(row)





if __name__ == '__main__':

    teste = csv()
    #print(teste.leitura())
    #teste.inserir_linhas()
    #print(teste.leitor())
    #print(teste.inserir_Dict('w'))
    #print(teste.leitor_dict())
    #print(teste.append('fanho', 'legal', 24))
    #print(teste.buscar())]
    #print(teste.delet())
