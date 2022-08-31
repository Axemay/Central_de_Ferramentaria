from contextlib import ContextDecorator
import tkinter as tk
from tkinter import Frame, ttk
from tkinter import END
from tkinter import messagebox
import csv
from CRUD_T import *
tecnico = dict()


class funcs(Csv):
    def entrada(self):
        Csv.__init__(self)
    #chamada do modulo herança multipla
    def variaveis(self):
        self.codigo = self.entry_codigoE.get()
        self.nome = self.entry_nomeE.get()
        self.cpf = self.entry_cpfE.get()
        self.item = self.entry_itemE.get()

    def busca(self):
        self.view_frame2.delete(*self.view_frame2.get_children())

        # self.entry_nomeE.insert(END, '%')
        codigo = self.entry_codigoE.get()
        nome = self.entry_nomeE.get()
        cpf = self.entry_cpfE.get()
        item = self.entry_itemE.get()
        # self.buscar(nome)
        self.busca_pessoa(codigo)
        self.busca_pessoa(nome)
        self.busca_pessoa(cpf)
        self.busca_pessoa(item)
        # self.search(nome)

        buscacodigolista = self.busca_pessoa(codigo)
        buscanomelista = self.busca_pessoa(nome)
        buscacpflista = self.busca_pessoa(cpf)
        buscaitemlista = self.busca_pessoa(item)

        for i in buscacodigolista:
            self.view_frame2.insert("", END, values=i)
        for i in buscanomelista:
            self.view_frame2.insert("", END, values=i)
        for i in buscacpflista:
            self.view_frame2.insert("", END, values=i)
        for i in buscaitemlista:
            self.view_frame2.insert("", END, values=i)

        self.limpar_dados()

    def atualizar(self):
        self.variaveis()
        # self.doubleclick(event='click')
        self.update(self.codigo, self.nome, self.cpf, self.item)

        self.select_list()
        self.limpar_dados()

    def delete(self):
        self.variaveis()
        # self.delete(self.codigo)

        self.delet(self.codigo)
        self.limpar_dados()
        self.select_list()

    def add_cliente(self):

        try:
            self.variaveis()
            # self.insertt(self.codigo, self.nome, self.cpf, self.item)
            self.append(self.codigo, self.nome, self.cpf, self.item)
            self.select_list()

        except Exception as e:
            print("error ao inserir", e)
        self.limpar_dados()

    def select_list(self):
        self.view_frame2.delete(*self.view_frame2.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitor()
        for i in lista:
            if i == ['codigo', 'nome', 'cpf', 'item']:
                continue
            self.view_frame2.insert("", END, values=i)

    def limpa_tela(self):
        self.vcpf.delete(0, END)
        self.vnome.delete(0, END)
        self.vtelefone.delete(0, END)
        self.vturno.delete(0, END)
        self.vequipe.delete(0, END)

    def doubleclick(self, event):
        self.limpar_dados()
        self.view_frame2.selection()

        for n in self.view_frame2.selection():
            col1, col2, col3, col4 = self.view_frame2.item(n, 'values')
            self.x = self.entry_codigoE.insert(END, col1)
            y = self.entry_nomeE.insert(END, col2)
            z = self.entry_cpfE.insert(END, col3)
            self.entry_itemE.insert(END, col4)
class TK(funcs):
    def janela_cadastro_tecnicos(self):
        global lista_tecnicos
        lista_tecnicos = []

        global contador
        contador = 0

        ######### VERIFICAÇÃO DE ERROS, VALIDAÇÃO ########################

    def codigo_tecnicos(self):
        cpf = self.vcpf.get()
        while True:
            if len(cpf) == 11:
                try:
                    cpf = int(cpf)
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "CPF: Digite apenas números")
                else:
                    res1 = cpf
            else:
                messagebox.showerror("Erro", "CPF: Insira exatamente 11 dígitos")
            break

        nome = self.vnome.get()
        res2 = nome.title()

        tel = self.vtelefone.get()
        while True:
            if len(tel) == 10 or len(tel) == 11:
                try:
                    tel = int(tel)
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "TELEFONE: Digite apenas números")
                else:
                    res3 = tel
            else:
                messagebox.showerror("Erro",
                                     "TELEFONE: Insira 10 dígitos para telefone fixo e 11 dígitos para celular, incluindo prefixo")
            break

        turno = self.vturno.get()
        turno = turno.upper()
        while True:
            if turno == "M":
                res4 = turno
            elif turno == "T":
                res4 = turno
            elif turno == "N":
                res4 = turno
            else:
                messagebox.showerror("Erro", "TURNO: Os turnos disponíveis são: M, T ou N")
            break

        equipe = self.vequipe.get()
        while True:
            try:
                equipe = int(equipe)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "EQUIPE: Digite apenas números")
            else:
                res5 = equipe
            break

        # lista_tecnicos.append(tecnico.copy())
        # print(lista_tecnicos)
        # return tecnico

        ########### REGISTRO NO ARQUIVO CSV ##################################

        with open("tecnico.csv", "a", newline="") as arquivo:

            campos = ["CPF", "Nome", "Telefone", "Turno", "Equipe"]
            escrever = csv.DictWriter(arquivo, fieldnames=campos, delimiter=",", lineterminator="\n")
            # não consegui manter o cabeçalho, ele repetia. Inseri no csv e permiti apenas a inserção das linhas
            # escrever.writeheader()

            escrever.writerow({"CPF": res1, "Nome": res2, "Telefone": res3, "Turno": res4, "Equipe": res5})

            self.limpa_tela()

            global contador

            contador += 1

            res = tk.Label(self.cadastro_tecnicos,
                           text=f"{contador} Cadastro(s) efetuado(s) com sucesso!\nDigite novamente para mais um cadastro",
                           bg="#B9B7BD", font=("verdana", 11))
            res.place(relx=0.05, rely=0.50, relwidth=0.8, relheight=0.1)

    ###### função para limpar os campos do entry, para nova digitação, tem que importar END do tkinter



    # ------------------------------------------------------------------------------------------
    def tabelaTc(self):
        self.cadastro_tecnicos = tk.Toplevel()
        self.cadastro_tecnicos.title('Janela de Cadastro de Técnicos')
        self.cadastro_tecnicos.iconphoto(False, tk.PhotoImage(file='ico/worker.png'))
        self.cadastro_tecnicos.configure(background='#B9B7BD')
        self.cadastro_tecnicos.geometry('700x500')
        self.cadastro_tecnicos.resizable(True, True)
        self.cadastro_tecnicos.maxsize(width=900, height=600)  # dimensões máximas
        self.cadastro_tecnicos.minsize(width=400, height=300)  # dimensões mínimas

        self.cpf = tk.Label(self.cadastro_tecnicos, text="CPF:", bg='#ffd')
        self.cpf.place(relx=0.05, rely=0.02, relwidth=0.1, relheight=0.05)
        self.vcpf = tk.Entry(self.cadastro_tecnicos)
        self.vcpf.place(relx=0.2, rely=0.02, relwidth=0.5, relheight=0.05)

        self.nome = tk.Label(self.cadastro_tecnicos, text='Nome:', bg='#ffd')
        self.nome.place(relx=0.05, rely=0.08, relwidth=0.1, relheight=0.05)
        self.vnome = tk.Entry(self.cadastro_tecnicos)
        self.vnome.place(relx=0.2, rely=0.08, relwidth=0.5, relheight=0.05)

        self.telefone = tk.Label(self.cadastro_tecnicos, text='Telefone:', bg='#ffd')
        self.telefone.place(relx=0.05, rely=0.14, relwidth=0.1, relheight=0.05)
        self.vtelefone = tk.Entry(self.cadastro_tecnicos)
        self.vtelefone.place(relx=0.2, rely=0.14, relwidth=0.5, relheight=0.05)

        self.turno = tk.Label(self.cadastro_tecnicos, text='Turno:', bg='#ffd')
        self.turno.place(relx=0.05, rely=0.2, relwidth=0.1, relheight=0.05)
        self.vturno = tk.Entry(self.cadastro_tecnicos)
        self.vturno.place(relx=0.2, rely=0.2, relwidth=0.5, relheight=0.05)

        self.equipe = tk.Label(self.cadastro_tecnicos, text='Equipe:', bg='#ffd')
        self.equipe.place(relx=0.05, rely=0.26, relwidth=0.1, relheight=0.05)
        self.vequipe = tk.Entry(self.cadastro_tecnicos)
        self.vequipe.place(relx=0.2, rely=0.26, relwidth=0.5, relheight=0.05)

        self.bsalvar = tk.Button(self.cadastro_tecnicos, text='Salvar Cadastro', command=self.codigo_tecnicos)
        self.bsalvar.place(relx=0.24, rely=0.35, relwidth=0.2, relheight=0.05)

        self.blimpar = tk.Button(self.cadastro_tecnicos, text="Limpar Campos", command=self.limpa_tela)
        self.blimpar.place(relx=0.46, rely=0.35, relwidth=0.2, relheight=0.05)

        self.res = tk.Label(self.cadastro_tecnicos, text="Insira acima os dados do funcionário", bg="#B9B7BD", font=("verdana", 11))
        self.res.place(relx=0.05, rely=0.50, relwidth=0.8, relheight=0.05)

        self.op = tk.Label(self.cadastro_tecnicos,
                      text="TURNO: Manhã (m), Tarde (t), Noite (n)\n\nCPF deve conter exatamente 11 dígitos\n\nTelefone deve conter 10 dígitos com prefixo incluso\n\nTodos os campos devem ser preenchidos",
                      bg="#B9B7BD", font=("verdana", 9))
        self.op.place(relx=0.05, rely=0.60, relwidth=0.8, relheight=0.40)

    def trueeview(self):
        self.dados_colunas = ("codigo", "nome", "cpf", "item")
        self.view_frame2 = ttk.Treeview(self.frame_2, columns=self.dados_colunas, selectmode='browse')

        self.view_frame2.heading("#0", text="")
        self.view_frame2.heading("codigo", text="Código", )
        self.view_frame2.heading("nome", text="Nome", )
        self.view_frame2.heading("cpf", text="CPF", )
        self.view_frame2.heading("item", text="Item")

        self.view_frame2.column("#0", width=1)
        self.view_frame2.column("codigo", minwidth=0, width=250)
        self.view_frame2.column("nome", minwidth=0, width=250)
        self.view_frame2.column("cpf", minwidth=0, width=250)
        self.view_frame2.column("item", minwidth=0, width=249)
        self.view_frame2.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.85)

        self.scrolbar_lista = Scrollbar(self.frame_2, orient="vertical", command=self.view_frame2.yview)
        self.view_frame2.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.98, rely=0.1, relwidth=0.07, relheight=0.85)

        self.scrolbar_lista2 = Scrollbar(self.frame_2, orient="horizontal", command=self.view_frame2.xview)
        self.view_frame2.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.01, rely=0.94, relwidth=0.97, relheight=0.07)
        self.view_frame2.bind("<Double-1>", self.doubleclick)

