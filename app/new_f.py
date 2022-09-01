from msilib.schema import ComboBox
import tkinter as tk
from tkinter import *
from tkinter import Frame, ttk
from tkinter import END
from tkinter import messagebox
from tkinter import Scrollbar
import csv
from CRUD_F import *


class funcs(Csv):
    def entrada(self):
        Csv.__init__(self)
    #chamada do modulo herança multipla
    def variaveisf(self):
        self.codigo = self.vcodigo_ferramenta.get()
        self.descricao = self.vdescricao_ferramenta.get()
        self.fabricante = self.vfabricante.get()
        self.voltagem = self.vvoltagem.get()
        self.part_number= self.vpart_number.get()
        self.tamanho = self.vtamanho.get()
        self.unidade = self.vunidade_medida.get()
        self.tipo = self.vtipo_ferramenta.get()
        self.material = self.vmaterial_ferramenta.get()

    def buscaf(self):
        self.view_frame2f.delete(*self.view_frame2f.get_children())

        # self.entry_nomeE.insert(END, '%')
        cpf = self.vcpf.get()
        nome = self.vnome.get()
        telefone =  self.vtelefone.get()
        turno = self.vturno.get()
        equipe = self.vequipe.get()
        # self.buscar(nome)
        self.busca_pessoa(cpf)
        self.busca_pessoa(nome)
        self.busca_pessoa(telefone)
        self.busca_pessoa(turno)
        self.busca_pessoa(equipe)

        # self.search(nome)

        buscacpflista = self.busca_pessoa(cpf)
        buscanomelista = self.busca_pessoa(nome)
        buscatelefonelista = self.busca_pessoa(telefone)
        buscaturnolista = self.busca_pessoa(turno)
        buscaequipelista = self.busca_pessoa(equipe)

        for i in buscacpflista:
            self.view_frame2.insert("", END, values=i)
        for i in buscanomelista:
            self.view_frame2.insert("", END, values=i)
        for i in buscatelefonelista:
            self.view_frame2.insert("", END, values=i)
        for i in buscaturnolista:
            self.view_frame2.insert("", END, values=i)
        for i in buscaequipelista:
            self.view_frame2.insert("", END, values=i)
        self.limpar_dados()

    def atualizarf(self):
        self.variaveisf()
        # self.doubleclick(event='click')
        self.update(self.cpf, self.nome, self.telefone, self.turno, self.equipe)

        self.select_listf()
        self.limpar_dadosF()

    def deletef(self):
        self.variaveisf()
        # self.delete(self.codigo)

        self.deletf(self.codigo)
        self.limpar_dadosF()
        self.select_listf()

    def add_clientef(self):
        codigo = self.vcodigo_ferramenta.get()
        while True:
            try:
                codigo = int(codigo)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "Codigo: Digite apenas números")
            else:
                self.res1 = codigo
            break

        descricao = self.vdescricao_ferramenta.get()
        self.res2 = descricao.capitalize()

        fabricante = self.vfabricante.get()
        self.res3 = fabricante.capitalize()

        voltagem = self.vvoltagem.get()
        while True:
            try:
                voltagem = int(voltagem)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "Voltagem: Digite apenas números")
            else:
                self.res4 = voltagem
            break

        part_number = self.vpart_number.get()
        self.res5 = part_number.lower()
        # sugestões

        tamanho = self.vtamanho.get()
        self.res6 = tamanho
        # sugestões

        unidade_medida = self.vunidade_medida.get()
        self.res7 = unidade_medida.lower()
        # sugestões

        tipo_ferramenta = self.vtipo_ferramenta.get()
        self.res8 = tipo_ferramenta.lower()
        # sugestões
        material = self.vmaterial_ferramenta.get()
        self.res9 = material.lower()
        try:
            self.appendf(self.res1, self.res2, self.res3, self.res4, self.res5, self.res6, self.res7, self.res8, self.res9)
            self.select_listf()

        except Exception as e:
            print("error ao inserir", e)
        self.limpar_dadosF()

    def select_listf(self):
        self.view_frame2f.delete(*self.view_frame2f.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitorf()
        for i in lista:
            if i == ["codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material"]:
                continue
            self.view_frame2f.insert("", END, values=i)

    def limpar_dadosF(self):
        self.vcodigo_ferramenta.delete(0, END)
        self.vdescricao_ferramenta.delete(0, END)
        self.vfabricante.delete(0, END)
        self.vvoltagem.delete(0, END)
        self.vpart_number.delete(0, END)
        self.vtamanho.delete(0, END)
        self.vunidade_medida.delete(0, END)
        self.vtipo_ferramenta.delete(0, END)
        self.vmaterial_ferramenta.delete(0, END)

    def doubleclickf(self, event):
        self.limpar_dadosF()
        self.view_frame2f.selection()

        for n in self.view_frame2f.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.view_frame2f.item(n, 'values')
            self.vcodigo_ferramenta.insert(END, col1)
            self.vdescricao_ferramenta.insert(END, col2)
            self.vfabricante.insert(END, col3)
            self.vvoltagem.insert(END, col4)
            self.vpart_number.insert(END, col5)
            self.vtamanho.insert(END, col6)
            self.vunidade_medida.insert(END, col7)
            self.vtipo_ferramenta.insert(END, col8)
            self.vmaterial_ferramenta.insert(END, col9)

class front_Ferramentas(funcs):
    def janela_frontF(self):
        self.cadastro_ferramentas = tk.Toplevel()
        self.cadastro_ferramentas.title('Janela de Cadastro de Ferramentas')
        self.cadastro_ferramentas.iconphoto(False, tk.PhotoImage(file='ico/tools.png'))
        self.cadastro_ferramentas.configure(background='#B9B7BD')
        self.cadastro_ferramentas.geometry('1380x780')
        self.cadastro_ferramentas.resizable(True, True)
        self.cadastro_ferramentas.maxsize(width=1920, height=1080)  # dimensões máximas
        self.cadastro_ferramentas.minsize(width=600, height=400)  # dimensões mínimas
####------------------------FRAMES--------------------------------------------------------------------###############
        self.frame_1 = Frame(self.cadastro_ferramentas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_1.place(relx=0.01, rely=0.006, relwidth=0.98, relheight=0.6)
        self.frame_2 = Frame(self.cadastro_ferramentas, bd=4, bg="#ffd", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_2.place(relx=0.3, rely=0.6, relwidth=0.368, relheight=0.045)

        self.frame_3 = Frame(self.cadastro_ferramentas, bd=4, bg="#868B8E", highlightbackground="#868B8E",
                             highlightthickness=1)
        self.frame_3.place(relx=0.01, rely=0.65, relwidth=0.98, relheight=0.34)

##############    ##### LABELS, ENTRYS
        self.codigo_ferramenta = tk.Label(self.frame_1, text='Código da Ferramenta:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.codigo_ferramenta.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.08)
        self.vcodigo_ferramenta = tk.Entry(self.frame_1, bd=3, font=('poppins', 14, 'bold'))
        self.vcodigo_ferramenta.place(relx=0.28, rely=0.01, relwidth=0.7, relheight=0.07)

        self.descricao_ferramenta = tk.Label(self.frame_1, text='Descrição da Ferramenta:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.descricao_ferramenta.place(relx=0.01, rely=0.11, relwidth=0.25, relheight=0.08)
        self.vdescricao_ferramenta = tk.Entry(self.frame_1, bd=3, font=('poppins', 14, 'bold'))
        self.vdescricao_ferramenta.place(relx=0.28, rely=0.11, relwidth=0.7, relheight=0.07)

        self.fabricante = tk.Label(self.frame_1, text='Fabricante: ',  bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.fabricante.place(relx=0.01, rely=0.21, relwidth=0.25, relheight=0.08)
        self.vfabricante = tk.Entry(self.frame_1, bd=3, font=('poppins', 14, 'bold'))
        self.vfabricante.place(relx=0.28, rely=0.21, relwidth=0.7, relheight=0.07)

        self.voltagem = tk.Label(self.frame_1, text='Voltagem de Uso:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.voltagem.place(relx=0.01, rely=0.31, relwidth=0.25, relheight=0.08)
        self.vvoltagem = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vvoltagem.place(relx=0.28, rely=0.31, relwidth=0.7, relheight=0.07)

        self.part_number = tk.Label(self.frame_1, text='Part Number:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.part_number.place(relx=0.01, rely=0.41, relwidth=0.25, relheight=0.08)
        self.vpart_number = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vpart_number.place(relx=0.28, rely=0.41, relwidth=0.7, relheight=0.07)

        self.tamanho = tk.Label(self.frame_1, text='Tamanho da Ferramenta:',  bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.tamanho.place(relx=0.01, rely=0.51, relwidth=0.25, relheight=0.08)
        self.vtamanho = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vtamanho.place(relx=0.28, rely=0.51, relwidth=0.7, relheight=0.07)

        self.unidade_medida = tk.Label(self.frame_1, text='Unidade de Medida:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.unidade_medida.place(relx=0.01, rely=0.61, relwidth=0.25, relheight=0.08)
        self.vunidade_medida = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vunidade_medida.place(relx=0.28, rely=0.61, relwidth=0.7, relheight=0.07)

        self.tipo_ferramenta = tk.Label(self.frame_1, text='Tipo da Ferramenta:',  bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.tipo_ferramenta.place(relx=0.01, rely=0.71, relwidth=0.25, relheight=0.08)
        self.vtipo_ferramenta = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vtipo_ferramenta.place(relx=0.28, rely=0.71, relwidth=0.7, relheight=0.07)

        self.material_ferramenta = tk.Label(self.frame_1, text='Material da Ferramenta', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.material_ferramenta.place(relx=0.01, rely=0.81, relwidth=0.25, relheight=0.08)
        self.vmaterial_ferramenta = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vmaterial_ferramenta.place(relx=0.28, rely=0.81, relwidth=0.7, relheight=0.07)
# ################ -------------- BOTÕES    ####--------------------------------------------------------------------------------
#
        self.bsalvar = tk.Button(self.frame_1, text='Salvar Cadastro', command= self.add_clientef)
        self.bsalvar.place(relx=0.15, rely=0.92, relwidth=0.15, relheight=0.07)

        self.blimpar = tk.Button(self.frame_1, text="Limpar Campos", command=self.limpar_dadosF)
        self.blimpar.place(relx=0.01, rely=0.92, relwidth=0.1, relheight=0.07)

        self.bbusca = tk.Button(self.frame_1, text="Pesquisar", bd=5, command=self.buscaf)
        self.bbusca.place(relx=0.55, rely=0.92, relwidth=0.12, relheight=0.07)

        self.bup = tk.Button(self.frame_1, text="Atualizar", bd=5, command= self.atualizarf)
        self.bup.place(relx=0.69, rely=0.92, relwidth=0.13, relheight=0.07)

        self.bdelet = tk.Button(self.frame_1, text="Deletar", bd=5, command= self.deletef)
        self.bdelet.place(relx=0.83, rely=0.92, relwidth=0.13, relheight=0.07)

        # self.bat = tk.Button(self.cadastro_tecnicos, text="Atualizar Lista", bd=5, command=self.select_list)
        # self.bat.place(relx=0.05, rely=0.45, relwidth=0.065, relheight=0.05)

        res = tk.Label(self.frame_2, text="Insira acima os dados da ferramenta", bg="#ffd", font=("poppins", 18, 'bold'))
        res.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        ## TRUEE VIEW

        self.dados_colunas = ("codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material")
        self.view_frame2f = ttk.Treeview(self.frame_3, columns=self.dados_colunas, selectmode='browse')

        self.view_frame2f.heading("#0", text="")
        self.view_frame2f.heading("codigo", text="Codigo", )
        self.view_frame2f.heading("descricao", text="Descrição", )
        self.view_frame2f.heading("fabricante", text="Fabricante", )
        self.view_frame2f.heading("voltagem", text="Voltagem", )
        self.view_frame2f.heading("partnumber", text="Partnumber", )
        self.view_frame2f.heading("tamanho", text="Tamanho", )
        self.view_frame2f.heading("unidade", text="Unidade")
        self.view_frame2f.heading("tipo", text="Tipo")
        self.view_frame2f.heading("material", text="Material")

        self.view_frame2f.column("#0", width=1)
        self.view_frame2f.column("codigo", minwidth=0, width=250)
        self.view_frame2f.column("descricao", minwidth=0, width=250)
        self.view_frame2f.column("fabricante", minwidth=0, width=250)
        self.view_frame2f.column("voltagem", minwidth=0, width=250)
        self.view_frame2f.column("partnumber", minwidth=0, width=249)
        self.view_frame2f.column("tamanho", minwidth=0, width=249)
        self.view_frame2f.column("unidade", minwidth=0, width=249)
        self.view_frame2f.column("tipo", minwidth=0, width=249)
        self.view_frame2f.column("material", minwidth=0, width=249)


        self.view_frame2f.place(relx=0.005, rely=0.03, relwidth=0.98, relheight=0.90)

        self.scrolbar_lista = Scrollbar(self.frame_3, orient="vertical", command=self.view_frame2f.yview)
        self.view_frame2f.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.03, relwidth=0.018, relheight=0.85)

        self.scrolbar_lista2 = Scrollbar(self.frame_3, orient="horizontal", command=self.view_frame2f.xview)
        self.view_frame2f.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        self.view_frame2f.bind("<Double-1>", self.doubleclickf)
        self.select_listf()











# #

