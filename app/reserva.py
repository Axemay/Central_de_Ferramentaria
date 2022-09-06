import datetime
import tkinter as tk
from tkinter import END
from tkinter import Frame, ttk
from tkinter import Scrollbar
from tkinter import messagebox
from CRUD_F import *
from CRUD_R import *
from tkcalendar import Calendar
from datetime import date, time, datetime, timedelta


from CRUD_T import *



class funcsRF (Csvf):
    def vazioF(self, msg):
        if msg == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")

        else:

            return msg

    def buscaF(self):
        self.view_frame2.delete(*self.view_frame2.get_children())

        # self.entry_nomeE.insert(END, '%')
        pesquisa = self.vPesquisa_ReservaF.get()
        buscacpflista = self.busca_cod(pesquisa)

        if pesquisa == "":
            messagebox.showerror("Erro", "O campo deve ser preenchidos")
        else:
            for i in buscacpflista:
                self.view_frame2.insert("", END, values=i)

            self.limpar_dadosFF()
            return
        self.select_listF()

    def select_listF(self):
        self.view_frame2.delete(*self.view_frame2.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitorf()

        for i in lista:
            if i == ["codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo"]:
                continue

            self.view_frame2.insert("", END, values = i)

    def limpar_dadosFF(self):
        self.vPesquisa_ReservaF.delete(0, END)

        self.Gcod.delete(0, END)
        self.Gdes.delete(0, END)
        self.Gvolt.delete(0, END)
        self.Gtipo.delete(0, END)

    def doubleclickF(self, event):
        self.limpar_dadosFF()
        self.view_frame2.selection()
        global fvalida
        fvalida = True

        for n in self.view_frame2.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = self.view_frame2.item(n, 'values')

            self.vPesquisa_ReservaF.insert(END, col1)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col2)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col4)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col8)
            self.Gcod.insert(END, col1)
            self.Gdes.insert(END, col2)
            self.Gvolt.insert(END, col4)
            self.Gtipo.insert(END, col8)
class funcsRT (Csv):
    def vazio(self, msg):
        if msg == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")

        else:

            return msg

    def buscaT(self):


        self.view_frame1.delete(*self.view_frame1.get_children())

        # self.entry_nomeE.insert(END, '%')
        pesquisa = self.vPesquisa_ReservaT.get()
        buscacpflista = self.busca_cpf(pesquisa)

        if pesquisa == "":
            messagebox.showerror("Erro", "Os campos devem ser preenchidos")
        else:
            for i in buscacpflista:
                self.view_frame1.insert("", END, values=i)

            self.limpar_dadosT()
            return
        self.select_listT()

    def select_listT(self):
        self.view_frame1.delete(*self.view_frame1.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitor()
        for i in lista:
            if i == ["cpf", "nome", "telefone", "turno", "equipe"]:
                continue
            self.view_frame1.insert("", END, values=i)

    def limpar_dadosT(self):
        self.vPesquisa_ReservaT.delete(0, END)

        self.Gcpf.delete(0, END)
        self.Gnome.delete(0, END)
        self.Gtel.delete(0, END)

    def doubleclickT(self, event):
        self.limpar_dadosT()
        self.view_frame1.selection()
        global fvalida
        fvalida = True

        for n in self.view_frame1.selection():
            col1, col2, col3, col4, col5 = self.view_frame1.item(n, 'values')

            self.vPesquisa_ReservaT.insert(END, col1)
            self.vPesquisa_ReservaT.insert(END, ",")
            self.vPesquisa_ReservaT.insert(END, col2)
            self.vPesquisa_ReservaT.insert(END, ",")
            self.vPesquisa_ReservaT.insert(END, col3)
            self.Gcpf.insert(END, col1)
            self.Gnome.insert(END, col2)
            self.Gtel.insert(END, col3)
class funcsRR (CsvR):
    def variaveisR(self):

        global data
        data = datetime.now()

        self.gcpf = self.Gcpf.get()
        self.gnome = self.Gnome.get()
        self.gtel = self.Gtel.get()
        self.gcod = self.Gcod.get()
        self.gdes = self.Gdes.get()
        self.gvolt = self.Gvolt.get()
        self.gtipo = self.Gtipo.get()

        def validadh(msg):
            try:
                msg = int(msg)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "Digite apenas números")
            else:
                return str(msg)

        def doisdigitos(msg):
            if len(msg) > 2 or  len(msg) == 0:
                messagebox.showerror("Erro", "Insira até 2 dígitos")
            else:
                return msg

        def validahora(msg):
            msg = int(msg)
            if msg < 0 or msg > 24:
                messagebox.showerror("Erro", "O horário de expediente para retirada e entrega\ndas ferramentas é de 08:00hs às 17:00hs")
            else:
                return str(msg)

        def validames(msg):
            msg = int(msg)
            if msg < 1 or msg > 12:
                messagebox.showerror("Erro", "O ano deve estar compatível com o calendário")
            else:
                return str(msg)

        def validadia(msg):
             try:
                res = msg
             except (ValueError, TypeError):
                messagebox.showerror("Erro", "Esse dia não consta no calendário")
             else:
                return res
                    
        self.dataentD = doisdigitos(validadh(self.vData_entregaD.get()))        
        self.dataentM = validames(doisdigitos(validadh(self.vData_entregaM.get())))
        self.dataentA = self.vData_entregaA.get()
        self.horaentH = validahora(doisdigitos(validadh(self.vHora_entregaH.get())))
        self.horaentM = self.vHora_entregaM.get()
        self.horaentS = self.vHora_entregaS.get()
        self.dataretD = doisdigitos(validadh(self.vData_retiradaD.get()))
        self.dataretM = validames(doisdigitos(validadh(self.vData_retiradaM.get())))
        self.dataretA = self.vData_retiradaA.get()
        self.horaretH = validahora(doisdigitos(validadh(self.vHora_retiradaH.get())))
        self.horaretM = self.vHora_retiradaM.get()
        self.horaretS = self.vHora_retiradaS.get()

        
        self.retira = validadia(datetime(int(self.dataretA), int(self.dataretM), int(self.dataretD), int(self.horaretH),
                               int(self.horaretM), int(self.horaretS)))

        self.entrega = validadia(datetime(int(self.dataentA), int(self.dataentM), int(self.dataentD), int(self.horaentH),
                               int(self.horaentM), int(self.horaentS)))
        
        self.diferenca = self.retira - data
        self.string=str(self.diferenca)
        self.output=self.string.split()
        if "-" in self.output[0]:
            messagebox.showerror("Erro", "Você não pode reservar com uma data ou hora passada")
        else:        
            self.dataretirada = f"{self.dataretD}/{self.dataretM}/{self.dataretA}"
            self.horaretirada = f"{self.horaretH}:{self.horaretM}:{self.horaretS}"

        self.diferenca2 = self.entrega - self.retira
        self.string2=str(self.diferenca2)
        self.output2=self.string2.split()
        if "-" in self.output2[0]:
            messagebox.showerror("Erro", "Você não pode entregar com  data e hora anterior a reserva")
        else: 
            self.dataentrega = f"{self.dataentD}/{self.dataentM}/{self.dataentA}"   
            self.horaentrega = f"{self.horaentH}:{self.horaentM}:{self.horaentS}"
        
    def limpar_dadosR(self):
        self.Gcpf.delete(0, END)
        self.Gnome.delete(0, END)
        self.Gtel.delete(0, END)
        self.Gcod.delete(0, END)
        self.Gdes.delete(0, END)
        self.Gvolt.delete(0, END)
        self.Gtipo.delete(0, END)
        self.vPesquisa_ReservaT.delete(0, END)
        self.vPesquisa_ReservaF.delete(0, END)

    def select_listR(self):
        self.view_frame3.delete(*self.view_frame3.get_children())
        # self.view_frame2.selection(*self.view_frame2.get_children())
        # lista = self.query("SELECT * FROM teste1")
        # lista = self.leitor_dict()
        # lista = self.leitura()
        lista = self.leitorR()

        for i in lista:
            if i == ["cpf", "nome", "telefone", "codigo", "descricao", "voltagem", "tipo", "dataretirada", "horaretirada", "dataentrega", "horaentrega"]:
                continue

            self.view_frame3.insert("", END, values = i)
    def doubleclickR(self, event):
        self.limpar_dadosR()
        self.view_frame3.selection()
        global fvalida
        fvalida = True

        for n in self.view_frame3.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11= self.view_frame3.item(n, 'values')
            self.Gcpf.insert(END, col1)
            self.Gnome.insert(END, col2)
            self.Gtel.insert(END, col3)
            self.Gcod.insert(END, col4)
            self.Gdes.insert(END, col5)
            self.Gvolt.insert(END, col6)
            self.Gtipo.insert(END, col7)

            self.vPesquisa_ReservaT.insert(END, col1)
            self.vPesquisa_ReservaT.insert(END, ",")
            self.vPesquisa_ReservaT.insert(END, col2)
            self.vPesquisa_ReservaT.insert(END, ",")
            self.vPesquisa_ReservaT.insert(END, col3)

            self.vPesquisa_ReservaF.insert(END, col4)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col5)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col6)
            self.vPesquisa_ReservaF.insert(END, ",")
            self.vPesquisa_ReservaF.insert(END, col7)

            

    def limpar_entries(self):
        self.vPesquisa_ReservaT.delete(0, END)
        self.vPesquisa_ReservaF.delete(0, END)
        self.vData_entregaD.delete(0, END)        
        self.vData_entregaM.delete(0, END) 
        self.vHora_entregaH.delete(0, END)
        self.vData_retiradaD.delete(0, END)
        self.vData_retiradaM.delete(0, END)
        self.vHora_retiradaH.delete(0, END)
        


            
    def add_reserva(self):
        self.variaveisR()
        self.appendR(self.gcpf, self.gnome, self.gtel, self.gcod, self.gdes, self.gvolt, self.gtipo, self.dataretirada, self.horaretirada, self.dataentrega, self.horaentrega)
        self.select_listR()

        # self.res = tk.Label(self.frame_4, text=f"{contador} Cadastro(s) efetuado(s) com sucesso!", bg="#868B8E",
        #                             fg="#ffd", font=("poppins", 16, 'bold'))
        # self.res.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.7)
        self.limpar_dadosR()


    def calendario(self):
        self.calendario1 = Calendar(self.cadastro_reservas, fg="gray75", bg="blue", font=("poppins", "9", "bold"), locale="pt_br")
        self.calendario1.place(relx=0.28, rely=0.25)
        self.cal_data = tk.Button(self.cadastro_reservas, text="Inserir data", command=self.puxar_data_ret)
        self.cal_data.place(relx=0.38, rely=0.5, height=25, width=100)
        self.calendario2 = Calendar(self.cadastro_reservas, fg="gray75", bg="blue", font=("poppins", "9", "bold"),
                                    locale="pt_br")
        self.calendario2.place(relx=0.50, rely=0.25)
        self.cal_data_dev = tk.Button(self.cadastro_reservas, text="Inserir data", command=self.puxar_data_dev)
        self.cal_data_dev.place(relx=0.47, rely=0.5, height=25, width=100)

    def puxar_data_ret(self):
        data_inicial = self.calendario1.get_date()
        self.entry_data_retirada.delete(0, END)
        self.entry_data_retirada.insert(END, data_inicial)
        self.calendario1.destroy()
        self.cal_data.destroy()

    def puxar_data_dev(self):
        data_final = self.calendario2.get_date()
        self.entry_data_dev.delete(0, END)
        self.entry_data_dev.insert(END, data_final)
        self.calendario2.destroy()
        self.cal_data_dev.destroy()
#----------------------------------------------------------------------------------------------------------------------
class Reserva (funcsRT, funcsRF, funcsRR) :
    def janela_cadastro_reservas(self):
        self.cadastro_reservas = tk.Toplevel()
        self.cadastro_reservas.title('Reserva')
        self.cadastro_reservas.iconphoto(False, tk.PhotoImage(file='../ico/reserva.png'))
        self.cadastro_reservas.configure(background='#B9B7BD')
        self.cadastro_reservas.geometry('1380x780')
        self.cadastro_reservas.resizable(True, True)
        self.cadastro_reservas.maxsize(width= 1920, height=1080) # dimensões máximas
        self.cadastro_reservas.minsize(width= 600, height= 400) # dimensões mínimas

####################################  FRAMES ==============================================================

        self.frame_1 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_1.place(relx=0.048, rely=0.006, relwidth=0.9, relheight=0.23)

        self.frame_2 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_2.place(relx=0.048, rely=0.245, relwidth=0.9, relheight=0.23)

        self.frame_3 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_3.place(relx=0.01, rely=0.65, relwidth=0.98, relheight=0.34)
        
###################################  ENTRY LABELS BOTOES ===============================================

        self.Pesquisa_ReservaT = tk.Label(self.frame_1, text='Pesquisa por CPF:', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 14, 'bold'))
        self.Pesquisa_ReservaT.place(relx=0.0, rely=0.0, relwidth=0.15, relheight=0.15)
        self.vPesquisa_ReservaT = tk.Entry(self.frame_1, bd=3, font=('poppins', 11, 'bold'))
        self.vPesquisa_ReservaT.place(relx=0.155, rely=0.0, relwidth=0.4, relheight=0.14)

    ##  Botão Tecnico
        self.bupT = tk.Button(self.frame_1, text="Pesquisar", bd=5, command= self.buscaT)
        self.bupT.place(relx=0.63, rely=0.0,  relwidth=0.1, relheight=0.15)

        self.batualizarT = tk.Button(self.frame_1, text="Atualizar Lista", bd=5, command= self.select_listT)
        self.batualizarT.place(relx=0.74, rely=0.0, relwidth=0.1, relheight=0.15)
    ##  ENTRY,  LABELS FERRAMENTA
        self.Pesquisa_ReservaF = tk.Label(self.frame_2, text='Pesquisa por Codigo da Ferramenta:', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 11, 'bold'))
        self.Pesquisa_ReservaF.place(relx=0.0, rely=0.0, relwidth=0.224, relheight=0.15)
        self.vPesquisa_ReservaF = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.vPesquisa_ReservaF.place(relx=0.23, rely=0.0, relwidth=0.4, relheight=0.14)

    ##  Botão FERRAMENTA
        self.bupT = tk.Button(self.frame_2, text="Pesquisar", bd=5, command=self.buscaF)
        self.bupT.place(relx=0.68, rely=0.0, relwidth=0.1, relheight=0.15)

        self.batualizarT = tk.Button(self.frame_2, text="Atualizar Lista", bd=5, command=self.select_listF)
        self.batualizarT.place(relx=0.79, rely=0.0, relwidth=0.1, relheight=0.15)

#------------------------------------------------------------------

        # ano = date.today().year
        #
        # text2Entry = tk.StringVar()
        # text2Entry.set(ano)
        #
        # textEntry = tk.StringVar()
        # textEntry.set("00")
        
        self.bt_calendario = tk.Button(self.cadastro_reservas, text='Data da Retirada', command=self.calendario)
        self.bt_calendario.place(relx=0.14, rely=0.5, relwidth=0.14, relheight=0.04)
        self.entry_data_retirada = tk.Entry(self.cadastro_reservas, width=4)
        self.entry_data_retirada.place(relx=0.29, rely=0.5, relwidth=0.08, relheight=0.04)

        self.bt_calendario_entrega = tk.Button(self.cadastro_reservas, text='Data da Devolução', command=self.calendario)
        self.bt_calendario_entrega.place(relx=0.55, rely=0.5, relwidth=0.14, relheight=0.04)
        self.entry_data_dev = tk.Entry(self.cadastro_reservas, width=4)
        self.entry_data_dev.place(relx=0.70, rely=0.5, relwidth=0.08, relheight=0.04)
        
#         self.Data_entrega = tk.Label(self.cadastro_reservas, text='Data da Entrega :', bg='#ffd', fg='#0D0D0D',
#                                       font=('poppins', 14, 'bold'))
#         self.Data_entrega.place(relx=0.55, rely=0.5, relwidth=0.14, relheight=0.04)
#         self.vData_entregaD = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
#         self.vData_entregaD.place(relx=0.7, rely=0.5, relwidth=0.04, relheight=0.04)
#         self.vData_entregaM = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
#         self.vData_entregaM.place(relx=0.74, rely=0.5, relwidth=0.04, relheight=0.04)
#         self.vData_entregaA = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'), textvariable = text2Entry, state="readonly")
#         self.vData_entregaA.place(relx=0.78, rely=0.5, relwidth=0.04, relheight=0.04)
#
# #------------------------------------------------------------------
#
#
#         self.Hora_entrega = tk.Label(self.cadastro_reservas, text='Hora da Entrega :', bg='#ffd', fg='#0D0D0D',
#                                      font=('poppins', 14, 'bold'))
#         self.Hora_entrega.place(relx=0.55, rely=0.55, relwidth=0.14, relheight=0.04)
#         self.vHora_entregaH = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
#         self.vHora_entregaH.place(relx=0.7, rely=0.55, relwidth=0.04, relheight=0.04)
#         self.vHora_entregaM = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'), textvariable = textEntry, state="readonly")
#         self.vHora_entregaM.place(relx=0.74, rely=0.55, relwidth=0.04, relheight=0.04)
#         self.vHora_entregaS = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'), textvariable = textEntry, state="readonly")
#         self.vHora_entregaS.place(relx=0.78, rely=0.55, relwidth=0.04, relheight=0.04)

        
#-------------------------------------------------------------------

        
#         self.Data_retirada = tk.Label(self.cadastro_reservas, text='Data da Retirada :', bg='#ffd', fg='#0D0D0D',
#                                           font=('poppins', 14, 'bold'))
#         self.Data_retirada.place(relx=0.14, rely=0.5, relwidth=0.14, relheight=0.04)
#         self.vData_retiradaD = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
#         self.vData_retiradaD.place(relx=0.29, rely=0.5, relwidth=0.04, relheight=0.04)
#         self.vData_retiradaM = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
#         self.vData_retiradaM.place(relx=0.33, rely=0.5, relwidth=0.04, relheight=0.04)
#         self.vData_retiradaA = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'), textvariable = text2Entry, state="readonly")
#         self.vData_retiradaA.place(relx=0.37, rely=0.5, relwidth=0.04, relheight=0.04)
#
# #-------------------------------------------------------------------
#
#
#         self.Hora_retirada = tk.Label(self.cadastro_reservas, text='Hora da Retirada :', bg='#ffd', fg='#0D0D0D',
#                                      font=('poppins', 14, 'bold'))
#         self.Hora_retirada.place(relx=0.14, rely=0.55, relwidth=0.14, relheight=0.04)
#
#         self.vHora_retiradaH = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'))
#         self.vHora_retiradaH.place(relx=0.29, rely=0.55, relwidth=0.04, relheight=0.04)
#         self.vHora_retiradaM = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'), textvariable = textEntry, state="readonly")
#         self.vHora_retiradaM.place(relx=0.33, rely=0.55, relwidth=0.04, relheight=0.04)
#         self.vHora_retiradaS = tk.Entry(self.cadastro_reservas, bd=3, font=('poppins', 11, 'bold'), textvariable = textEntry, state="readonly")
#         self.vHora_retiradaS.place(relx=0.37, rely=0.55, relwidth=0.04, relheight=0.04)
        
#----------------------- SOLUCAO-------------------------------------------------------------------------------
        self.Gcpf = tk.Entry(self.frame_1, bd=3, font=('poppins', 11, 'bold'))
        self.Gcpf.place(relx=0.00, rely=0.00, relwidth=0.0, relheight=0.0)
        self.Gnome = tk.Entry(self.frame_1, bd=3, font=('poppins', 11, 'bold'))
        self.Gnome.place(relx=0.00, rely=0.00, relwidth=0.00, relheight=0.00)
        self.Gtel = tk.Entry(self.frame_1, bd=3, font=('poppins', 11, 'bold'))
        self.Gtel.place(relx=0.00, rely=0.00, relwidth=0.00, relheight=0.00)
        
#==========
        
        self.Gcod = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.Gcod.place(relx=0.00, rely=0.00, relwidth=0.00, relheight=0.00)
        self.Gdes = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.Gdes.place(relx=0.00, rely=0.00, relwidth=0.00, relheight=0.00)
        self.Gvolt = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.Gvolt.place(relx=0.00, rely=0.00, relwidth=0.00, relheight=0.00)
        self.Gtipo = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.Gtipo.place(relx=0.00, rely=0.00, relwidth=0.00, relheight=0.00)

#------------------------------------------------------------
        ##  OUTROS BOTÕES, ENTRYS E LEBELS

        self.limpacamp = tk.Button(self.cadastro_reservas, text="Limpar Campos", bd=5, command=self.limpar_entries)
        self.limpacamp.place(relx=0.10, rely=0.6, relwidth=0.1, relheight=0.05)

        self.btdel = tk.Button(self.cadastro_reservas, text="Delete", bd=5)
        self.btdel.place(relx=0.30, rely=0.6, relwidth=0.1, relheight=0.05)

        self.bupR = tk.Button(self.cadastro_reservas, text="Reservar", bd=5, command= self.add_reserva)
        self.bupR.place(relx=0.43, rely=0.6, relwidth=0.1, relheight=0.05)

        self.batR = tk.Button(self.cadastro_reservas, text="Atualizar Lista", bd=5, command=self.select_listR)
        self.batR.place(relx=0.6, rely=0.6, relwidth=0.1, relheight=0.05)
        
############################### TRUE VIEW ==============================================================================
    ## true view frame 1
        self.dados_colunas = ("cpf", "nome", "telefone")

        self.view_frame1 = ttk.Treeview(self.frame_1, columns=self.dados_colunas, selectmode='browse')

        self.view_frame1.heading("#0", text="")
        self.view_frame1.heading("cpf", text="CPF")
        self.view_frame1.heading("nome", text="NOME")
        self.view_frame1.heading("telefone", text="TELEFONE")

        self.view_frame1.column("#0", width=0)
        self.view_frame1.column("cpf", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame1.column("nome", minwidth=0, width=350, anchor=tk.CENTER)
        self.view_frame1.column("telefone", minwidth=0, width=350, anchor=tk.CENTER)

        self.view_frame1.place(relx=0.005, rely=0.155, relwidth=0.98, relheight=0.8)

        self.scrolbar_lista = Scrollbar(self.frame_1, orient="vertical", command=self.view_frame1.yview)
        self.view_frame1.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.15, relwidth=0.015, relheight=0.8)

        self.scrolbar_lista2 = Scrollbar(self.frame_1, orient="horizontal", command=self.view_frame1.xview)
        self.view_frame1.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        self.view_frame1.bind("<Double-1>", self.doubleclickT)
        self.select_listT()

## true view frame 2
        self.dados_colunas = ( "codigo","descricao","fabricante","voltagem","partnumber","tamanho","unidade","tipo","material", "tempo")

        self.view_frame2 = ttk.Treeview(self.frame_2, columns=self.dados_colunas, selectmode='browse')

        self.view_frame2.heading("#0", text="")
        self.view_frame2.heading("codigo", text="CÓDIGO", )
        self.view_frame2.heading("descricao", text="DESCRIÇÃO", )
        self.view_frame2.heading("fabricante", text="FABRICANTE", )
        self.view_frame2.heading("voltagem", text="VOLTAGEM", )
        self.view_frame2.heading("partnumber", text="PARTNUMBER", )
        self.view_frame2.heading("tamanho", text="TAMANHO", )
        self.view_frame2.heading("unidade", text="UNIDADE")
        self.view_frame2.heading("tipo", text="TIPO")
        self.view_frame2.heading("material", text="MATERIAL")
        self.view_frame2.heading("tempo", text="TEMPO DE RESERVA")


        self.view_frame2.column("#0", width=0)
        self.view_frame2.column("codigo", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame2.column("descricao", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame2.column("fabricante", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("voltagem", minwidth=0, width=300, anchor=tk.CENTER)
        self.view_frame2.column("partnumber", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tamanho", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("unidade", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tipo", minwidth=0, width=350, anchor=tk.CENTER)
        self.view_frame2.column("material", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tempo", minwidth=0, width=0, anchor=tk.CENTER)

        self.view_frame2.place(relx=0.005, rely=0.155, relwidth=0.98, relheight=0.8)

        self.scrolbar_lista = Scrollbar(self.frame_2, orient="vertical", command=self.view_frame2.yview)
        self.view_frame2.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.15, relwidth=0.015, relheight=0.8)

        self.scrolbar_lista2 = Scrollbar(self.frame_2, orient="horizontal", command=self.view_frame2.xview)
        self.view_frame2.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        self.view_frame2.bind("<Double-1>", self.doubleclickF)
        self.select_listF()

    ## true view frame 3
        self.dados_colunas = ("cpf", "nome", "telefone", "codigo", "descricao", "voltagem", "tipo", "dataretirada", "horaretirada", "dataentrega", "horaentrega")
        self.view_frame3 = ttk.Treeview(self.frame_3, columns=self.dados_colunas, selectmode='browse')

        self.view_frame3.heading("#0", text="")
        self.view_frame3.heading("cpf", text="CPF")
        self.view_frame3.heading("nome", text="NOME")
        self.view_frame3.heading("telefone", text="TELEFONE")
        self.view_frame3.heading("codigo", text="CÓDIGO", )
        self.view_frame3.heading("descricao", text="DESCRIÇÃO", )
        self.view_frame3.heading("voltagem", text="VOLTAGEM", )
        self.view_frame3.heading("tipo", text="TIPO")
        self.view_frame3.heading("dataretirada", text="DATA RETIRADA")
        self.view_frame3.heading("horaretirada", text="HORA RETIRADA")
        self.view_frame3.heading("dataentrega", text="DATA ENTREGA")
        self.view_frame3.heading("horaentrega", text="HORA ENTREGA")


        self.view_frame3.column("#0", width=0)
        self.view_frame3.column("cpf", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("nome", minwidth=0, width=170, anchor=tk.CENTER)
        self.view_frame3.column("telefone", minwidth=0, width=150, anchor=tk.CENTER)
        self.view_frame3.column("codigo", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("descricao", minwidth=0, width=200, anchor=tk.CENTER)
        self.view_frame3.column("voltagem", minwidth=0, width=100, anchor=tk.CENTER)
        self.view_frame3.column("tipo", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("dataretirada", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("horaretirada", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("dataentrega", minwidth=0, width=120, anchor=tk.CENTER)
        self.view_frame3.column("horaentrega", minwidth=0, width=120, anchor=tk.CENTER)

        self.view_frame3.place(relx=0.005, rely=0.03, relwidth=0.98, relheight=0.90)

        self.scrolbar_lista = Scrollbar(self.frame_3, orient="vertical", command=self.view_frame3.yview)
        self.view_frame3.configure(yscrollcommand=self.scrolbar_lista.set)
        self.scrolbar_lista.place(relx=0.985, rely=0.03, relwidth=0.018, relheight=0.85)

        self.scrolbar_lista2 = Scrollbar(self.frame_3, orient="horizontal", command=self.view_frame3.xview)
        self.view_frame3.configure(xscrollcommand=self.scrolbar_lista2.set)
        self.scrolbar_lista2.place(relx=0.005, rely=0.93, relwidth=0.97, relheight=0.07)
        self.view_frame3.bind("<Double-1>", self.doubleclickR)
        self.select_listR()
