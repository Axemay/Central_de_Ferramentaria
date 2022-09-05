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
    def appendR(self, cpf, nome, telefone, codigo, descricao, voltagem, tipo, dataretirada, horaretirada, dataentrega, horaentrega):
        # with open('./appcsv.csv') as self.file:
        #     self.csv_Dreader = DictReader(self.file)
        #     self.data2 = list(self.csv_Dreader)
        with open('./reserva.csv', 'a', newline="", encoding='utf-8') as self.file:
            header = ("cpf", "nome", "telefone", "codigo", "descricao", "voltagem", "tipo", "dataretirada", "horaretirada", "dataentrega", "horaentrega")
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
            'dataentrega': dataentrega,
            'horaentrega': horaentrega})


            #self.csv_Dwriter.writerows(self.data2)
            self.csv_Dwriter.writerow(data)
            #self.csv_Dwriter.writerows(data)
