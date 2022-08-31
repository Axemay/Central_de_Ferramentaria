import re
from csv import DictWriter, DictReader, reader
import re
from typing import Dict

# #pessoas: List[Dict[str, str]] = [
#     {'nome': 'Luiz', 'sobrenome': 'Miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Moreira'},
#     {'nome': 'Elaine', 'sobrenome': 'Figueiredo'},
#     {'nome': 'Helena', 'sobrenome': 'Oliveira'},
#     {'nome': 'vivian', 'sobrenome': 'Silva'},
#     {'nome': 'Fabrício', 'sobrenome': 'Costa'},
#     {'nome': 'Eduardo', 'sobrenome': 'Vieira'},
#     {'nome': 'Lívia', 'sobrenome': 'Madeira'},
#     {'nome': 'João', 'sobrenome': 'Barbosa'},
#     {'nome': 'Dania', 'sobrenome': 'Maia'},
#]


def busca_pessoa(
    nome_buscado):
    with open('./appcsv.csv') as file:

        csv_Dreader = reader(file)
        data = list(csv_Dreader)

    for pessoa in data:
        col1, col2, col3, col4 = pessoa

        # if nome_buscado == f'{col1}':
        #
        #     return [pessoa]
        # if nome_buscado == f'{col2}':
        #     return [pessoa]
        # if nome_buscado == f'{col3}':
        #     return [pessoa]
        # if nome_buscado == f'{col4}':
        #
        #     return [pessoa]

        regex = re.compile(fr'{col1}|{col2}|{col3}|{col4}', flags=re.I)
        if regex.findall(nome_buscado):

            return pessoa


    return {}


# with open('./appcsv.csv') as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#
#     for row in data:
#         print(data)

if __name__ == "__main__":
    #pessoa_1 = busca_pessoa('5')
    pessoa_2 = busca_pessoa('578')
   # print(pessoa_1)
    print(pessoa_2)



# with open('./appcsv.csv') as file:
#     csv_Dreader = DictReader(file)
#     data = list(csv_Dreader)
# with open('./appcsv.csv') as file:
#     csv_reader = reader(file)
#     data2 = list(csv_reader)
#
#
#
#     for row in data:
#         if row['codigo'] == '2':
#             print(row)
def buscar(self, codigo):
    with open('./appcsv.csv') as self.file:
        self.csv_Dreader = DictReader(self.file)
        self.data = list(self.csv_Dreader)


        for row in self.data:
            if row['codigo'] == codigo:
                return row



def buscar():
    with open('./users.csv') as file:
        csv_Dreader = DictReader(file)
        data = list(csv_Dreader)
        x = input()
        f = ['First Name']
        l = ['Last name']
        a = ['Age']
        for row in data:
            f, l, a = row.values()

            if x == f'{f} {l} {a}':
                return row
            regex = re.compile(fr'{f} {l} {a}', flags=re.I)
            if regex.search(x) :
                return row
            return row
        return {}

# def busca_pessoa():
#     with open('./users.csv') as file:
#         csv_Dreader = DictReader(file)
#         data = list(csv_Dreader)
#         x = input()
#         f = ['First Name']
#         l = ['Last name']
#         a = ['Age']
#         for row in data :
#             f, l, a = row.values()
#
#             if x == f'{f} {l} {a}':
#                 return row
#         return {}

def buscassr():
    with open('./users.csv') as file:
        csv_Dreader = DictReader(file)
        data = list(csv_Dreader)
        x = input('algum nome: ')
        regex = re.compile(fr'{x}\w+', flags=re.I)
        p = regex.search(x)
        for row in data:
            if row['First Name'] == p:
                print(row)
        return {}


# with open('./users.csv', mode='r', encoding='utf8') as file:
#     texto = file.read()
#
#
#     header = ('First Name', 'Last name')
#
#     for row in texto :
#         print(row)
