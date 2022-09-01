from csv import writer, reader
from csv import DictWriter, DictReader
from pprint import pprint
import re
from tkinter import *
import tkinter as tk
from tkinter import ttk
from CRUDCSV import *
janela = tk.Tk()

class funcs(Csv):
    def chamada(self):
        Csv.__init__(self)
    def variaveis(self):
        self.codigo = self.entry_codigoE.get()
        self.nome = self.entry_nomeE.get()
        self.cpf = self.entry_cpfE.get()
        self.item = self.entry_itemE.get()


    def busca(self):
        self.view_frame2.delete(*self.view_frame2.get_children())

        #self.entry_nomeE.insert(END, '%')
        codigo = self.entry_codigoE.get()
        nome = self.entry_nomeE.get()
        cpf = self.entry_cpfE.get()
        item = self.entry_itemE.get()
        #self.buscar(nome)
        self.busca_pessoa(codigo)
        self.busca_pessoa(nome)
        self.busca_pessoa(cpf)
        self.busca_pessoa(item)
        #self.search(nome)

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
        #self.doubleclick(event='click')
        self.update(self.codigo, self.nome, self.cpf, self.item)

        self.select_list()
        self.limpar_dados()

    def delete(self):
        self.variaveis()
        #self.delete(self.codigo)

        self.delet(self.codigo)
        self.limpar_dados()
        self.select_list()

    def add_cliente(self):

        try:
            self.variaveis()
            #self.insertt(self.codigo, self.nome, self.cpf, self.item)
            self.append(self.codigo, self.nome, self.cpf, self.item)
            self.select_list()

        except Exception as e:
            print("error ao inserir", e)
        self.limpar_dados()

    def select_list(self):
        self.view_frame2.delete(*self.view_frame2.get_children())
        #self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        #lista = self.leitor_dict()
        #lista = self.leitura()
        lista = self.leitor()
        for i in lista:
            if i == ['codigo', 'nome', 'cpf', 'item']:
                continue
            self.view_frame2.insert("", END, values=i)

    def limpar_dados(self):
        self.entry_nomeE.delete(0, END)
        self.entry_cpfE.delete(0, END)
        self.entry_itemE.delete(0, END)
        self.entry_codigoE.delete(0, END)

    def doubleclick(self, event):
        self.limpar_dados()
        self.view_frame2.selection()

        for n in self.view_frame2.selection():
            col1, col2, col3, col4 = self.view_frame2.item(n, 'values')
            self.entry_codigoE.insert(END, col1)
            self.entry_nomeE.insert(END, col2)
            self.entry_cpfE.insert(END, col3)
            self.entry_itemE.insert(END, col4)


class Aplication(funcs):
    def __init__(self):
        funcs.__init__(self)
        self.janela = janela
        self.configuration()
        self.Frames()
        self.BLE()
        self.trueeview()
        self.select_list()
        self.menu()
        janela.mainloop()

    def configuration(self):
        self.janela.title("janela teste")
        self.janela.geometry("900x700")
        self.janela.configure(background='#B9B7BD')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=1080, height=780)
        self.janela.minsize(width=500, height=300)

    def Frames(self):
        self.frame_1 = Frame(self.janela, bd=4, bg="#868B8E", highlightbackground="#868B8E", highlightthickness=2)
        self.frame_1.place(relx=0.01, rely=0.006, relwidth=0.98, relheight=0.488)
        self.frame_2 = Frame(self.janela, bd=4, bg="#868B8E", highlightbackground="#868B8E", highlightthickness=2)
        self.frame_2.place(relx=0.01, rely=0.505, relwidth=0.98, relheight=0.488)

    def BLE(self):
        self.botao_limpar = Button(self.frame_1, text='Limpar', bd=6, bg='#868B8E', fg='white',
                                   font=('poppins', 10, 'bold'), command=self.limpar_dados)
        self.botao_limpar.place(relx=0.2, rely=0.8, relwidth=0.1, relheight=0.1)

        self.botao_buscar = Button(self.frame_1, text='Buscar', bd=6, bg='#868B8E', fg='white',
                                   font=('poppins', 10, 'bold'), command= self.busca)
        self.botao_buscar.place(relx=0.31, rely=0.8, relwidth=0.1, relheight=0.1)

        self.botao_novo = Button(self.frame_1, text='Novo', bd=10, bg='#868B8E', fg='white',
                                 font=('poppins', 10, 'bold'), command= self.add_cliente)
        self.botao_novo.place(relx=0.7, rely=0.8, relwidth=0.09, relheight=0.09)

        self.botao_alterar = Button(self.frame_1, text='Atualizar', bd=6, bg='#868B8E', fg='white',
                                    font=('poppins', 10, 'bold'), command= self.atualizar)
        self.botao_alterar.place(relx=0.8, rely=0.8, relwidth=0.09, relheight=0.09)

        self.botao_apagar = Button(self.frame_1, text='Apagar', bd=6, bg='#868B8E', fg='white',
                                   font=('poppins', 10, 'bold'), command=self.delete)
        self.botao_apagar.place(relx=0.9, rely=0.8, relwidth=0.09, relheight=0.09)
        ###valores LABELS
        self.label_nome = Label(self.frame_1, text='NOME : ', bd=6, font=('poppins', 10, 'bold'))
        self.label_nome.place(relx=0.04, rely=0.04)

        self.label_cpf = Label(self.frame_1, text='CPF : ', bd=6, font=('poppins', 10, 'bold'))
        self.label_cpf.place(relx=0.04, rely=0.2)

        self.label_item = Label(self.frame_1, text='ITEM : ', bd=6, font=('poppins', 10, 'bold'))
        self.label_item.place(relx=0.04, rely=0.34)

        self.label_codigo = Label(self.frame_1, text='CODIGO : ', bd=6, font=('poppins', 10, 'bold'))
        self.label_codigo.place(relx=0.04, rely=0.48)
        ###valores ENTRYS

        self.entry_nomeE = Entry(self.frame_1, bd=3, font=('poppins', 10, 'bold'))
        self.entry_nomeE.place(relx=0.2, rely=0.04, relwidth=0.4, relheight=0.08)

        self.entry_cpfE = Entry(self.frame_1, bd=3, font=('poppins', 10, 'bold'))
        self.entry_cpfE.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)

        self.entry_itemE = Entry(self.frame_1, bd=3, font=('poppins', 10, 'bold'))
        self.entry_itemE.place(relx=0.2, rely=0.34, relwidth=0.4, relheight=0.08)

        self.entry_codigoE = Entry(self.frame_1, bd=3, font=('poppins', 10, 'bold'))
        self.entry_codigoE.place(relx=0.2, rely=0.48)

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

    def quit(self):
        self.janela.destroy()

    def menu(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar)

        menubar.add_cascade(label="Opções", menu=menu1)
        menubar.add_cascade(label="sobre", menu=menu2)

        menu1.add_command(label="Sair", command=self.quit)
        menu2.add_command(label="Limpar cliente", command=self.limpar_dados)


Aplication()