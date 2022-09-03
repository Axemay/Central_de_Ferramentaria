import code
from hmac import compare_digest
from msilib.schema import ComboBox
import tkinter as tk
from tkinter import *
from tkinter import Frame, ttk
from tkinter import END
from tkinter import messagebox
from tkinter import Scrollbar
import csv
from CRUD_F import *


global fcontador
fcontador = 0

global fvalida
fvalida = False

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
        self.tempo = self.vTemMax_ferramenta.get()
    def buscaf(self):
        self.view_frame2f.delete(*self.view_frame2f.get_children())

        codigo = self.vcodigo_ferramenta.get()

        self.busca_pessoaf(codigo)

        buscacodigolista = self.busca_pessoaf(codigo)

        for i in buscacodigolista:
            self.view_frame2f.insert("", END, values=i)

        self.limpar_dadosF()

    def atualizarf(self):
        self.variaveisf()
        # self.doubleclick(event='click')

        self.updatef(self.codigo, self.descricao, self.fabricante, self.voltagem, self.part_number, self.tamanho, self.unidade, self.tipo, self.material, self.tempo )

        self.select_listf()
        self.limpar_dadosF()

    def deletef(self):
        global fvalida
        if fvalida == True:
            self.variaveisf()
            # self.delete(self.codigo)

            self.deletf(self.codigo)
            self.limpar_dadosF()
            self.select_listf()
        
            self.res = tk.Label(self.frame_2, text=f"Cadastro excluído  com sucesso!", bg="#B9B7BD", font=("poppins", 16, 'bold'))
            self.res.place(relx=0.00, rely=0.14, relwidth=1, relheight=1)
            fvalida = False
        else:
            messagebox.showerror("Erro", "Selecione um cadastro para deletar")

    def vazio(self, msg):
        if msg == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
        else:
            return msg

    def add_clientef(self):
        global chave
        chave = 0

        global codigo
        codigo = 0

        with open('./ferramenta.csv', encoding='utf-8') as self.file:
            self.csv_reader = reader(self.file)
            self.data = list(self.csv_reader)
            for row in self.data:
                print(row)
            print((row[0]))
            self.numero = row[0]

            if self.numero == "codigo":
                self.res1 = 101
                chave += 1
            else:
                self.res1 = int(row[0]) + 1
                chave += 1

        #while True:
        #    try:
        #        codigo = int(codigo)
        #    except (ValueError, TypeError):
        #        messagebox.showerror("Erro", "Codigo: Digite apenas números")
        #    else:
        #        self.res1 = codigo
        #        chave += 1
        #    break

        descricao = self.vazio(self.vdescricao_ferramenta.get())
        self.res2 = descricao.capitalize()
        chave += 1

        fabricante = self.vazio(self.vfabricante.get())
        self.res3 = fabricante.capitalize()
        chave += 1

        voltagem = self.vvoltagem.get()
        while True:
            try:
                voltagem = int(voltagem)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "Voltagem: Digite apenas números")
            else:
                self.res4 = voltagem
                chave += 1
            break

        part_number = self.vazio(self.vpart_number.get())
        self.res5 = part_number.lower()
        chave += 1
        # sugestões

        tamanho = self.vazio(self.vtamanho.get())
        self.res6 = tamanho
        chave += 1
        # sugestões

        unidade_medida = self.vazio(self.vunidade_medida.get())
        self.res7 = unidade_medida.lower()
        chave += 1
        # sugestões

        tipo_ferramenta = self.vazio(self.vtipo_ferramenta.get())
        self.res8 = tipo_ferramenta.lower()
        chave += 1
        # sugestões
        material = self.vazio(self.vmaterial_ferramenta.get())
        self.res9 = material.lower()
        chave += 1

        tempo = self.vazio(self.vTemMax_ferramenta.get())
        self.res10 = tempo
        chave += 1

        while True:
            if chave == 10:
                    self.appendf(self.res1, self.res2, self.res3, self.res4, self.res5, self.res6, self.res7, self.res8, self.res9, self.res10)
                    self.select_listf()
                    global fcontador
                    fcontador += 1
                    self.res = tk.Label(self.frame_2, text=f"{fcontador} Cadastro(s) efetuado(s) com sucesso!", bg="#B9B7BD", font=("poppins", 16, 'bold'))
                    self.res.place(relx=0.00, rely=0.14, relwidth=1, relheight=1)
                    self.limpar_dadosF()
                    chave = 0
            break

    def select_listf(self):
        self.view_frame2f.delete(*self.view_frame2f.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitorf()
        for i in lista:
            if i == ["codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo"]:
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
        self.vTemMax_ferramenta.delete(0, END)

    def doubleclickf(self, event):
        self.limpar_dadosF()
        self.view_frame2f.selection()
        global fvalida
        fvalida = True

        for n in self.view_frame2f.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.view_frame2f.item(n, 'values')
            self.vcodigo_ferramenta.insert(END, col1)
            self.vdescricao_ferramenta.insert(END, col2)
            self.vfabricante.insert(END, col3)
            self.vvoltagem.insert(END, col4)
            self.vpart_number.insert(END, col5)
            self.vtamanho.insert(END, col6)
            self.vunidade_medida.insert(END, col7)
            self.vtipo_ferramenta.insert(END, col8)
            self.vmaterial_ferramenta.insert(END, col9)
            self.vTemMax_ferramenta.insert(END, col10)

class front_Ferramentas(funcs):
    def janela_frontF(self):
        self.cadastro_ferramentas = tk.Toplevel()
        self.cadastro_ferramentas.title('Janela de Cadastro de Ferramentas')
        self.cadastro_ferramentas.iconphoto(False, tk.PhotoImage(file='../ico/tools.png'))
        self.cadastro_ferramentas.configure(background='#B9B7BD')
        self.cadastro_ferramentas.geometry('1380x780')
        self.cadastro_ferramentas.resizable(True, True)
        self.cadastro_ferramentas.maxsize(width=1920, height=1080)  # dimensões máximas
        self.cadastro_ferramentas.minsize(width=600, height=400)  # dimensões mínimas
####------------------------FRAMES--------------------------------------------------------------------###############
        self.frame_1 = Frame(self.cadastro_ferramentas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D", highlightthickness=1)
        self.frame_1.place(relx=0.01, rely=0.006, relwidth=0.98, relheight=0.6)
        self.frame_2 = Frame(self.cadastro_ferramentas)
        #bd=4, bg="#ffd", highlightbackground="#0D0D0D",                           highlightthickness=1)
        self.frame_2.place(relx=0.3, rely=0.6, relwidth=0.38, relheight=0.045)

        self.frame_3 = Frame(self.cadastro_ferramentas, bd=4)
        #bg="#868B8E", highlightbackground="#868B8E",                              highlightthickness=1)
        self.frame_3.place(relx=0.01, rely=0.65, relwidth=0.98, relheight=0.34)

##############    ##### LABELS, ENTRIES
        self.codigo_ferramenta = tk.Label(self.frame_1, text='Pesquisa :', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 17, 'bold'))
        self.codigo_ferramenta.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.08)
        self.vcodigo_ferramenta = tk.Entry(self.frame_1, bd=3, font=('poppins', 14, 'bold'))
        self.vcodigo_ferramenta.place(relx=0.28, rely=0.01, relwidth=0.4, relheight=0.07)

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
        self.vmaterial_ferramenta.place(relx=0.28, rely=0.81, relwidth=0.35, relheight=0.07)

        self.TemMax_ferramenta = tk.Label(self.frame_1, text='Tempo MAX Reserva (D):', bg='#ffd', fg='#0D0D0D',
                                            font=('poppins', 15, 'bold'))
        self.TemMax_ferramenta.place(relx=0.65, rely=0.81, relwidth=0.22, relheight=0.07)
        self.vTemMax_ferramenta = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
        self.vTemMax_ferramenta.place(relx=0.88, rely=0.81, relwidth=0.1, relheight=0.07)

################# -------------- BOTÕES    ####--------------------------------------------------------------------------------

        self.bsalvar = tk.Button(self.frame_1, text='Salvar Cadastro', bd=5, command= self.add_clientef)
        self.bsalvar.place(relx=0.15, rely=0.92, relwidth=0.11, relheight=0.08)

        self.blimpar = tk.Button(self.frame_1, text="Limpar Campos", bd=5, command=self.limpar_dadosF)
        self.blimpar.place(relx=0.01, rely=0.92, relwidth=0.11, relheight=0.08)

        self.bbusca = tk.Button(self.frame_1, text="Pesquisar", bd=5, command=self.buscaf)
        self.bbusca.place(relx=0.7, rely=0.01, relwidth=0.11, relheight=0.08)

        self.bup = tk.Button(self.frame_1, text="Atualizar", bd=5, command= self.atualizarf)
        self.bup.place(relx=0.69, rely=0.92, relwidth=0.11, relheight=0.08)

        self.bdelet = tk.Button(self.frame_1, text="Deletar", bd=5, command= self.deletef)
        self.bdelet.place(relx=0.83, rely=0.92, relwidth=0.11, relheight=0.08)

        #self.bat = tk.Button(self.cadastro_tecnicos, text="Atualizar Lista", bd=5, command=self.select_list)
        #self.bat.place(relx=0.05, rely=0.45, relwidth=0.065, relheight=0.05)

        self.res = tk.Label(self.frame_2, text="Insira acima os dados da ferramenta", bg="#b9b7bd", font=("poppins", 16, 'bold'))
        self.res.place(relx=0.00, rely=0.14, relwidth=1, relheight=1)

        ## TRUEE VIEW

        self.dados_colunas = ("codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo")
        self.view_frame2f = ttk.Treeview(self.frame_3, columns=self.dados_colunas, selectmode='browse')

        self.view_frame2f.heading("#0", text="")
        self.view_frame2f.heading("codigo", text="CÓDIGO", )
        self.view_frame2f.heading("descricao", text="DESCRIÇÃO", )
        self.view_frame2f.heading("fabricante", text="FABRICANTE", )
        self.view_frame2f.heading("voltagem", text="VOLTAGEM", )
        self.view_frame2f.heading("partnumber", text="PARTNUMBER", )
        self.view_frame2f.heading("tamanho", text="TAMANHO", )
        self.view_frame2f.heading("unidade", text="UNIDADE")
        self.view_frame2f.heading("tipo", text="TIPO")
        self.view_frame2f.heading("material", text="MATERIAL")
        self.view_frame2f.heading("tempo", text="TEMPO DE RESERVA")

        self.view_frame2f.column("#0", width=0)
        self.view_frame2f.column("codigo", minwidth=0, width=30, anchor=tk.CENTER)
        self.view_frame2f.column("descricao", minwidth=0, width=350, anchor=tk.CENTER)
        self.view_frame2f.column("fabricante", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame2f.column("voltagem", minwidth=0, width=50, anchor=tk.CENTER)
        self.view_frame2f.column("partnumber", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame2f.column("tamanho", minwidth=0, width=100, anchor=tk.CENTER)
        self.view_frame2f.column("unidade", minwidth=0, width=50, anchor=tk.CENTER)
        self.view_frame2f.column("tipo", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame2f.column("material", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame2f.column("tempo", minwidth=0, width=120, anchor=tk.CENTER)


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

