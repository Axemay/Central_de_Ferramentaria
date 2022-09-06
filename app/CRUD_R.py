from csv import writer, reader
from csv import DictWriter, DictReader
import re

class CsvR:
    def leitorR(self):
        with open('./reserva.csv', encoding='utf-8') as self.file:
            self.csv_reader = reader(self.file)
            self.data = list(self.csv_reader)

            for row in self.data:


                return self.data

            #     return row
    def appendR(self, cpf, nome, telefone, codigo, descricao, voltagem, tipo, dataretirada, horaretirada, datadevolucao, horaentrega):
        # with open('./appcsv.csv') as self.file:
        #     self.csv_Dreader = DictReader(self.file)
        #     self.data2 = list(self.csv_Dreader)
        with open('./reserva.csv', 'a', newline="", encoding='utf-8') as self.file:
            header = ("cpf", "nome", "telefone", "codigo", "descricao", "voltagem", "tipo", "dataretirada", "horaretirada", "datadevolucao", "horaentrega")
            #pulo = "\n"
            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator="\n" )

            data = ({'cpf' : cpf,
                    'nome' : nome,
                     'telefone' : telefone,
                     'descricao' : descricao,
                     'codigo' : codigo,
                    'voltagem': voltagem,
                    'tipo': tipo,
                    'dataretirada' : dataretirada,
            'horaretirada': horaretirada,
            'datadevolucao': datadevolucao,
            'horaentrega': horaentrega})


            #self.csv_Dwriter.writerows(self.data2)
            self.csv_Dwriter.writerow(data)
            #self.csv_Dwriter.writerows(data)
    def deletR(self, cpf):
        with open('./reserva.csv', encoding='utf-8') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./reserva.csv', 'w', encoding='utf-8') as self.file:
            header = ("cpf", "nome", "telefone", "codigo", "descricao", "voltagem", "tipo", "dataretirada", "horaretirada", "dataentrega", "horaentrega")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            for row in self.data:
                if row['cpf'] == cpf:
                    continue

                self.csv_Dwriter.writerow(row)
