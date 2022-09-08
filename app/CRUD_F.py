from csv import writer, reader
from csv import DictWriter, DictReader
import re
from typing import Dict



class Csvf :

    def leitorf(self):
        with open('./ferramenta.csv', encoding='utf-8') as self.file:
            self.csv_reader = reader(self.file)
            self.data = list(self.csv_reader)

            for row in self.data:


                return self.data

            #     return row

    def appendf(self, codigo, descricao, fabricante, voltagem, partnumber, tamanho, unidade, tipo, material, tempo):
        # with open('./appcsv.csv') as self.file:
        #     self.csv_Dreader = DictReader(self.file)
        #     self.data2 = list(self.csv_Dreader)
        with open('./ferramenta.csv', 'a', newline="", encoding='utf-8') as self.file:
            header = ("codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo")
            #pulo = "\n"
            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator="\n" )

            data = ({'codigo' : codigo,
                    'descricao' : descricao,
                     'fabricante' : fabricante,
                     'voltagem' : voltagem,
                     'partnumber' : partnumber,
                     'tamanho' : tamanho,
                     'unidade' : unidade,
                     'tipo' : tipo,
                     'material' : material,
                     'tempo' : tempo})


            #self.csv_Dwriter.writerows(self.data2)
            self.csv_Dwriter.writerow(data)
            #self.csv_Dwriter.writerows(data)

    def deletf(self, codigo):
        with open('./ferramenta.csv', encoding='utf-8') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./ferramenta.csv', 'w', encoding='utf-8') as self.file:
            header = ("codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material","tempo")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            for row in self.data:
                if row['codigo'] == codigo :
                    continue

                self.csv_Dwriter.writerow(row)

    def updatef(self, codigo, descricao, fabricante, voltagem, partnumber, tamanho, unidade, tipo, material, tempo):
        with open('./ferramenta.csv', encoding='utf-8') as self.file:
            self.csv_Dreader = DictReader(self.file)
            self.data = list(self.csv_Dreader)
        with open('./ferramenta.csv', 'w', encoding='utf-8') as self.file:
            header = ("codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo")

            self.csv_Dwriter = DictWriter(self.file, fieldnames=header, lineterminator='\n')

            self.csv_Dwriter.writeheader()
            try:
                for row in self.data:
                    if row['codigo'] == codigo :
                            #or row['nome'] == nome or row['cpf'] == cpf or row['item'] == item:
                        row['codigo'] = codigo
                        row['descricao'] = descricao
                        row['fabricante'] = fabricante
                        row['voltagem'] = voltagem
                        row['partnumber'] = partnumber
                        row['tamanho'] = tamanho
                        row['unidade'] = unidade
                        row['tipo'] = tipo
                        row['material'] = material
                        row['tempo'] = tempo

                    self.csv_Dwriter.writerow(row)
            except Exception as e:
                print('erro ao atualizar: ', e)

    def busca_pessoaf(self, nome_buscado: str) -> Dict[str, str]:

        with open('./ferramenta.csv', encoding='utf-8') as self.file:

            self.csv_Dreader = reader(self.file)
            self.data = list(self.csv_Dreader)

        for pessoa in self.data:
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = pessoa

            if nome_buscado == f'{col1}':
                yield (pessoa)
            # if nome_buscado == f'{col2}':
            #     yield (pessoa)
            # if nome_buscado == f'{col3}':
            #     yield (pessoa)
            if nome_buscado == f'{col4}':
                yield (pessoa)
            if nome_buscado == f'{col6}':
                yield (pessoa)
            if nome_buscado == f'{col7}':
                yield (pessoa)
            if nome_buscado == f'{col10}':
                yield (pessoa)
            regex = re.compile(fr'{col2}|{col3}|{col5}|{col8}|{col9}', flags=re.I)
            if regex.findall(nome_buscado):
                yield (pessoa)
        return {}

    def busca_cod(self, nome_buscado: str) -> Dict[str, str]:

        with open('./ferramenta.csv', encoding='utf-8') as self.file:

            self.csv_Dreader = reader(self.file)
            self.data = list(self.csv_Dreader)

        for pessoa in self.data:
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = pessoa

            if nome_buscado == f'{col1}':
                yield (pessoa)

            # # if nome_buscado == f'{col2}':
            # #     yield (pessoa)
            # # if nome_buscado == f'{col3}':
            # #     yield (pessoa)
            # if nome_buscado == f'{col4}':
            #     yield (pessoa)
            # if nome_buscado == f'{col6}':
            #     yield (pessoa)
            # if nome_buscado == f'{col7}':
            #     yield (pessoa)
            # if nome_buscado == f'{col10}':
            #     yield (pessoa)
            # regex = re.compile(fr'{col2}|{col3}|{col5}|{col8}|{col9}', flags=re.I)
            # if regex.findall(nome_buscado):
            #     yield (pessoa)
        return {}


if __name__ == '__main__':
    TEST = Csvf()