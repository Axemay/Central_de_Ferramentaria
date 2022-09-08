import tkinter as tk
from tkinter import END
from tkinter import Frame, ttk
from tkinter import Scrollbar
from tkinter import messagebox
import conversor_csv_xls as ccx

from CRUD_T import *

tecnico = dict()
global chave
chave = 0

global contador
contador = 0

global valida
valida = False


class funcs(Csv):
    def entrada(self):
        Csv.__init__(self)
    #chamada do modulo herança multipla
    def valida_digito(self, cpfd):
        cpf = cpfd
        numero = []
        digito = []
        soma_um = soma_dois = 0
        cont = 10
        cont_dois = 11
        for i in str(cpf):
            if len(numero) < 9:
                numero.append(i)
            else:
                digito.append(i)
        for i in numero:
            soma_um += (int(i) * cont)
            cont = cont - 1
        for i in numero:
            soma_dois += (int(i) * cont_dois)
            cont_dois = cont_dois - 1

        # Encontra primeiro digito esperado
        dig_um = 0 if soma_um % 11 < 2 else (11 - (soma_um % 11))

        # Encontra segundo digito esperado
        soma_dois += dig_um * 2
        dig_dois = 0 if soma_dois % 11 < 2 else (11 - (soma_dois % 11))

        # Verifica se digitos são válidos
        if dig_um == int(digito[0]) and dig_dois == int(digito[1]):
            return True
        else:
            return False

    def variaveis(self):
        self.cpf = self.vcpf.get()
        self.nome = self.vnome.get()
        self.telefone = self.vtelefone.get()
        self.turno = self.vturno.get()
        self.equipe = self.vequipe.get()

    def busca(self):
        self.view_frame2.delete(*self.view_frame2.get_children())

        # self.entry_nomeE.insert(END, '%')
        pesquisa = self.vpesquisa.get()
        pesquisa = pesquisa.upper()

        self.busca_pessoa(pesquisa)


        buscacpflista = self.busca_pessoa(pesquisa)


        for i in buscacpflista:
            self.view_frame2.insert("", END, values=i)

        self.limpar_dados()

    def atualizar(self):
        global valida
        if valida == True:
            self.variaveis()
            # self.doubleclick(event='click')
            nome = self.vazio(self.vnome.get())
            self.res2 = nome.title()
            tel = self.vazio(self.vtelefone.get())

            while True:
                if len(tel) == 10 or len(tel) == 11:
                    try:
                        tel = int(tel)
                    except (ValueError, TypeError):
                        messagebox.showerror("Erro", "TELEFONE: Digite apenas números")
                    else:
                        self.res3 = tel

                else:
                    messagebox.showerror("Erro",
                                         "TELEFONE: Insira 10 dígitos para telefone fixo e 11 dígitos para celular, incluindo prefixo")
                break

            turno = self.vazio(self.vturno.get())
            turno = turno.upper()
            while True:
                if turno == "M":
                    self.res4 = turno

                elif turno == "T":
                    self.res4 = turno

                elif turno == "N":
                    self.res4 = turno

                else:
                    messagebox.showerror("Erro", "TURNO: Os turnos disponíveis são: M, T ou N")
                break

            equipe = self.vazio(self.vequipe.get())
            while True:
                try:
                    equipe = int(equipe)
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "EQUIPE: Digite apenas números")
                else:
                    self.res5 = equipe

                break

            self.update(self.cpf, self.res2, self.res3, self.res4, self.res5)
            self.select_list()
            self.limpar_dados()
            self.res = tk.Label(self.frame_4, text=f" Cadastro(s) Atualizado(s) com sucesso!", bg="#868B8E", fg="#ffd", font=("poppins", 16, 'bold'))
            self.res.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.7)

            valida = False
        else:
            messagebox.showerror("Erro", "Selecione um cadastro para atualizar")

    def delete(self):
        global valida
        if valida == True:
            self.variaveis()
            # self.delete(self.codigo)

            self.delet(self.cpf, self.nome)
            self.limpar_dados()
            self.select_list()
        
            self.res = tk.Label(self.frame_4, text=f"Cadastro excluído  com sucesso!", bg="#868B8E", fg="#ffd", font=("poppins", 16, 'bold'))
            self.res.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.7)
            valida = False
        else:
            messagebox.showerror("Erro", "Selecione um cadastro para deletar")

    def vazio(self, msg):
        if msg == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
        else:
            return msg

    def add_cliente(self):
        global chave
        chave = 0

        cpf = self.vazio(self.vcpf.get())

        while True:
            with open('./tecnico.csv', encoding='utf-8') as self.file:
                self.csv_Dreader = DictReader(self.file)
                self.data = list(self.csv_Dreader)
            for row in self.data:
                if row['cpf'] == cpf:
                    messagebox.showerror("Erro", "CPF: Ja existe")
                    return
            if cpf.isnumeric():
                self.valido = self.valida_digito(cpf)
                if len(cpf) == 11 and len(set(cpf)) != 1 and self.valido:
                    try:
                        cpf = int(cpf)
                    except (ValueError, TypeError):
                        messagebox.showerror("Erro", "CPF: Digite apenas números")
                    else:
                        self.res1 = cpf
                        chave += 1
                else:
                    messagebox.showerror("Erro", "CPF: Insira um CPF Valido de 11 dígitos")
            else:
                messagebox.showerror("Erro", "CPF: Digite apenas números")
            break

        nome = self.vazio(self.vnome.get())
        self.res2 = nome.title()
        chave += 1


        tel = self.vazio(self.vtelefone.get())
        
        while True:
            if len(tel) == 10 or len(tel) == 11:
                try:
                    tel = int(tel)
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "TELEFONE: Digite apenas números")
                else:
                    self.res3 = tel
                    chave += 1
            else:
                messagebox.showerror("Erro",
                                    "TELEFONE: Insira 10 dígitos para telefone fixo e 11 dígitos para celular, incluindo prefixo")
            break

        turno = self.vazio(self.vturno.get())
        turno = turno.upper()
        while True:
            if turno == "M":
                self.res4 = turno
                chave += 1
            elif turno == "T":
                self.res4 = turno
                chave += 1
            elif turno == "N":
                self.res4 = turno
                chave += 1
            else:
                messagebox.showerror("Erro", "TURNO: Os turnos disponíveis são: M, T ou N")
            break

        equipe = self.vazio(self.vequipe.get())
        while True:
            try:
                equipe = int(equipe)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "EQUIPE: Digite apenas números")
            else:
                self.res5 = equipe
                chave += 1
            break

        while True:

            if chave == 5:
                    self.append(self.res1, self.res2, self.res3, self.res4, self.res5)
                    self.select_list()
                    global contador
                    contador += 1
                    self.res = tk.Label(self.frame_4, text=f"{contador} Cadastro(s) efetuado(s) com sucesso!", bg="#868B8E", fg="#ffd", font=("poppins", 16, 'bold'))
                    self.res.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.7)
                    self.limpar_dados()
                    chave = 0
            break

    def select_list(self):
        self.view_frame2.delete(*self.view_frame2.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitor()
        for i in lista:
            if i == ["cpf", "nome", "telefone", "turno", "equipe"]:
                continue
            self.view_frame2.insert("", END, values=i)

    def limpar_dados(self):
        self.vcpf.delete(0, END)
        self.vnome.delete(0, END)
        self.vtelefone.delete(0, END)
        self.vturno.delete(0, END)
        self.vequipe.delete(0, END)

    def doubleclick(self, event):
        self.limpar_dados()
        self.view_frame2.selection()
        global valida
        valida = True
        


        for n in self.view_frame2.selection():
            col1, col2, col3, col4, col5 = self.view_frame2.item(n, 'values')
            self.vcpf.insert(END, col1)
            self.vnome.insert(END, col2)
            self.vtelefone.insert(END, col3)
            self.vturno.insert(END, col4)
            self.vequipe.insert(END, col5)

class TK(funcs):

    # ------------------------------------------------------------------------------------------
    def janela_frontT(self):
            ##config
            self.cadastro_tecnicos = tk.Toplevel()
            self.cadastro_tecnicos.title('Técnico')
            self.cadastro_tecnicos.iconphoto(False, tk.PhotoImage(file='../ico/worker.png'))
            self.cadastro_tecnicos.configure(background='#B9B7BD')
            self.cadastro_tecnicos.geometry('1380x780')
            self.cadastro_tecnicos.resizable(True, True)
            self.cadastro_tecnicos.maxsize(width=1920, height=1080)  # dimensões máximas
            self.cadastro_tecnicos.minsize(width=600, height=400)  # dimensões mínimas

            ##FRAMES
            self.frame_1 = Frame(self.cadastro_tecnicos, bd=4, bg="#868B8E", highlightbackground="#868B8E", highlightthickness=1)
            self.frame_1.place(relx=0.01, rely=0.006, relwidth=0.62, relheight=0.42)

            self.frame_2 = Frame(self.cadastro_tecnicos, bd=4, bg="#868B8E", highlightbackground="#868B8E", highlightthickness=1)
            self.frame_2.place(relx=0.01, rely=0.505, relwidth=0.98, relheight=0.488)

            self.frame_3 = Frame(self.cadastro_tecnicos, bd=4, bg="#ffd", highlightbackground="#0D0D0D",highlightthickness=1)
            self.frame_3.place(relx=0.63, rely=0.006, relwidth=0.368, relheight=0.42)

            self.frame_4 = Frame(self.cadastro_tecnicos, bd = 4, bg= "#868B8E", highlightbackground="#0D0D0D",highlightthickness=1)
            #bg="#b9b7bd", highlightbackground="#b9b7bd")
            self.frame_4.place(relx=0.3, rely=0.43, relwidth=0.36, relheight=0.07)


            ## BOTÕES, LABELS, ENTRIES
            self.cpf = tk.Label(self.frame_1, text="CPF:", bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 19, 'bold'))
            self.cpf.place(relx=0.05, rely=0.20, relwidth=0.17, relheight=0.12)

            self.vcpf = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
            self.vcpf.place(relx=0.24, rely=0.21, relwidth=0.4, relheight=0.11)
            ################################
            self.nome = tk.Label(self.frame_1, text='Nome:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 19, 'bold'))
            self.nome.place(relx=0.05, rely=0.36, relwidth=0.17, relheight=0.12)

            self.vnome = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
            self.vnome.place(relx=0.24, rely=0.37, relwidth=0.4, relheight=0.11)
            # ####################################
            self.telefone = tk.Label(self.frame_1, text='Telefone:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 19, 'bold'))
            self.telefone.place(relx=0.05, rely=0.52, relwidth=0.17, relheight=0.12)

            self.vtelefone = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
            self.vtelefone.place(relx=0.24, rely=0.53, relwidth=0.4, relheight=0.11)
            # ####################################
            self.turno = tk.Label(self.frame_1, text='Turno:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 19, 'bold'))
            self.turno.place(relx=0.05, rely=0.68, relwidth=0.17, relheight=0.12)

            self.vturno = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
            self.vturno.place(relx=0.24, rely=0.68, relwidth=0.15, relheight=0.11)
            # ####################################
            self.equipe = tk.Label(self.frame_1, text='Equipe:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 19, 'bold'))
            self.equipe.place(relx=0.42, rely=0.68, relwidth=0.17, relheight=0.12)

            self.vequipe = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
            self.vequipe.place(relx=0.62, rely=0.68, relwidth=0.15, relheight=0.11)
        ########################
            self.pesquisa = tk.Label(self.frame_1, text='Pesquisar:', bg='#ffd', fg='#0D0D0D',
                                   font=('poppins', 19, 'bold'))
            self.pesquisa.place(relx=0.05, rely=0.03, relwidth=0.17, relheight=0.12)
            self.vpesquisa = tk.Entry(self.frame_1, bd=3, font=('poppins', 16, 'bold'))
            self.vpesquisa.place(relx=0.24, rely=0.04, relwidth=0.5, relheight=0.1)

####################   BUTTON
            self.bsalvar = tk.Button(self.frame_1, text='Salvar Cadastro', bd=5, command=self.add_cliente)
            self.bsalvar.place(relx=0.29, rely=0.85, relwidth=0.15, relheight=0.12)

            self.blimpar = tk.Button(self.frame_1, text="Limpar Campos",bd=5, command=self.limpar_dados)
            self.blimpar.place(relx=0.05, rely=0.85, relwidth=0.15, relheight=0.12)

            self.bbusca = tk.Button(self.frame_1, text="Pesquisar", bd=5, command=self.busca)
            self.bbusca.place(relx=0.8, rely=0.04, relwidth=0.15, relheight=0.12)

            self.bup = tk.Button(self.frame_1, text="Atualizar", bd=5, command= self.atualizar)
            self.bup.place(relx=0.56, rely=0.85, relwidth=0.15, relheight=0.12)

            self.bdelet = tk.Button(self.frame_1, text="Deletar", bd=5, command= self.delete)
            self.bdelet.place(relx=0.80, rely=0.85, relwidth=0.15, relheight=0.12)

            self.bat = tk.Button(self.cadastro_tecnicos, text="Atualizar Lista", bd=5, command=self.select_list)
            self.bat.place(relx=0.15, rely=0.44, relwidth=0.092, relheight=0.05)

            self.bat = tk.Button(self.cadastro_tecnicos, text="Gerar Arquivo XLSX", bd=5, command=ccx.exportxlsT)
            self.bat.place(relx=0.73, rely=0.44, relwidth=0.12, relheight=0.05)



            ########## MENSAGEM
            self.res = tk.Label(self.frame_4, text="Insira acima os dados do funcionário", bg="#868B8E", fg="#ffd", font=("poppins", 16, 'bold'))
            self.res.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.7)

            self.op = tk.Label(self.frame_3,
                          text="Para Atualizar : Não mude o cpf !\n\n      Salvar cadastro : \nCPF deve conter exatamente 11 dígitos\nTelefone deve conter 10 dígitos com prefixo incluso\nTURNO: Manhã (m), Tarde (t), Noite (n)\nTodos os campos devem ser preenchidos\n\n   Deletar :\nDe um Double click na Trueview",
                          bg="#ffd", font=("poppins", 11, 'bold'))
            self.op.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.99)

            ## TREE VIEW

            self.dados_colunas = ("cpf", "nome", "telefone", "turno", "equipe")
            self.view_frame2 = ttk.Treeview(self.frame_2, columns=self.dados_colunas, selectmode='browse')

            self.view_frame2.heading("#0", text="")
            self.view_frame2.heading("cpf", text="CPF")
            self.view_frame2.heading("nome", text="NOME")
            self.view_frame2.heading("telefone", text="TELEFONE")
            self.view_frame2.heading("turno", text="TURNO")
            self.view_frame2.heading("equipe", text="EQUIPE")

            self.view_frame2.column("#0", width=1)
            self.view_frame2.column("cpf", minwidth=0, width=200, anchor=tk.CENTER)
            self.view_frame2.column("nome", minwidth=0, width=450, anchor=tk.CENTER)
            self.view_frame2.column("telefone", minwidth=0, width=200, anchor=tk.CENTER )
            self.view_frame2.column("turno", minwidth=0, width=200, anchor=tk.CENTER)
            self.view_frame2.column("equipe", minwidth=0, width=199, anchor=tk.CENTER)
            self.view_frame2.place(relx=0.005, rely=0.03, relwidth=0.98, relheight=0.90)

            self.scrolbar_lista = Scrollbar(self.frame_2, orient="vertical", command=self.view_frame2.yview)
            self.view_frame2.configure(yscrollcommand=self.scrolbar_lista.set)
            self.scrolbar_lista.place(relx=0.985, rely=0.03, relwidth=0.018, relheight=0.85)

            self.scrolbar_lista2 = Scrollbar(self.frame_2, orient="horizontal", command=self.view_frame2.xview)
            self.view_frame2.configure(xscrollcommand=self.scrolbar_lista2.set)
            self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
            self.view_frame2.bind("<Double-1>", self.doubleclick)
            self.select_list()
