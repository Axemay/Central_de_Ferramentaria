from csv import writer, reader
from csv import DictWriter, DictReader
import re
from typing import Dict



class Csv :

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
                        row['codigo'] = codigo
                        row['nome'] = nome
                        row['cpf'] = cpf
                        row['item'] = item
                    self.csv_Dwriter.writerow(row)
            except Exception as e:
                print('erro ao atualizar: ', e)



    def busca_pessoa(self, nome_buscado: str) -> Dict[str, str]:

        with open('./appcsv.csv') as self.file:

            self.csv_Dreader = reader(self.file)
            self.data = list(self.csv_Dreader)

        for pessoa in self.data:
            col1, col2, col3, col4 = pessoa

            # if nome_buscado == f'{col1}':
            #     yield (pessoa)
            # if nome_buscado == f'{col2}':
            #     yield (pessoa)
            # if nome_buscado == f'{col3}':
            #     yield (pessoa)
            # if nome_buscado == f'{col4}':
            #     yield (pessoa)
            regex = re.compile(fr'{col1}|{col2}|{col3}|{col4}', flags=re.I)
            if regex.findall(nome_buscado):
                yield (pessoa)
        return {}



if __name__ == '__main__':
    TEST = Csv()