import datetime
import tkinter as tk
from tkinter import END
from tkinter import Frame, ttk
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter.messagebox import askyesno
from CRUD_F import *
from CRUD_R import *
from tkcalendar import Calendar
from datetime import date, time, datetime, timedelta
from time import strptime
import conversor_csv_xls as ccx

from CRUD_T import *

global validaR
validaR = False


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
        self.Gtempo.delete(0, END)

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
            self.Gtempo.insert(END, col10)
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
        self.gcpf = self.Gcpf.get()
        self.gnome = self.Gnome.get()
        self.gtel = self.Gtel.get()
        self.gcod = self.Gcod.get()
        self.gdes = self.Gdes.get()
        self.gvolt = self.Gvolt.get()
        self.gtipo = self.Gtipo.get()
        self.gtempo = self.Gtempo.get()
        self.dataretirada = self.data_retirada.get()
        self.datadevolucao = self.data_devolucao.get()
        self.horaretirada = self.horas_ret.get()
        self.horadevolucao = self.horas_dev.get()

        #############################Verifica Data e hora de retirada e devolução ###############################################
    def verifica_data(self, datare, datade, horare, horade):
        mesmo_dia_ok = False
        dia_diferete_ok = False
        data_valida = False
        datar = datare
        datad = datade
        horare_str = horare[:2]
        horade_str = horade[:2]
        horar = int(horare_str)
        horad = int(horade_str)

        datar_formatada = strptime(datar, "%d/%m/%Y")
        datad_formatada = strptime(datad, "%d/%m/%Y")
        if datar_formatada <= datad_formatada:
            dia_diferete_ok = True
        if horad != horar:
            if horad > horar:
                mesmo_dia_ok = True
        if mesmo_dia_ok and dia_diferete_ok:
            data_valida = True

            return data_valida

#############################Verifica disponibilidade da ferramenta na data##########################################
    def valida_disp(self, codg, datare, horar, horad):
        cod = codg
        datar = datare
        datar_formatada = strptime(datar, "%d/%m/%Y")
        horare_str = horar[:2]
        horaret = int(horare_str)

        self.view_frame3.delete(*self.view_frame3.get_children())
        lista = self.leitorR()

        disponivel = True
        for i in range(len(lista)):
            fcods = lista[i][3]
            fcod = fcods


            if fcod == cod:
                hora_dev = lista[i][10]
                hora_dev_str = hora_dev[:2]
                hora_dev_int = int(hora_dev_str)
                print(hora_dev_str)
                data_ini = strptime(lista[i][7], "%d/%m/%Y")
                data_fim = strptime(lista[i][9], "%d/%m/%Y")
                print(f"data in {data_ini}")
                print(f"data de {data_fim}")
                if datar_formatada >= data_ini and datar_formatada < data_fim:
                    disponivel = False
                elif datar_formatada == data_fim:
                    if horaret >= hora_dev_int:
                        return True
                    else:
                        return False
                else:
                    disponivel = True
        print(f"data r {datar}")
        return disponivel

        #############################Converte tempo máximo da ferramenta pra int##########################################
    def conta_tempo(self, temp):
            tempo = temp
            conta_hora = 0
            if tempo == "06 horas":
                conta_hora = 6
            elif tempo == "12 horas":
                conta_hora = 12
            elif tempo == "18 horas":
                conta_hora = 18
            elif tempo == "24 horas":
                conta_hora = 24
            elif tempo == "30 horas":
                conta_hora = 30
            return conta_hora

        #############################Verifica tempo máximmo de reserva permitido##########################################
    def verifica_tempo(self, tempo, dataretirada, datadevolucao, horaretirada, horadevolucao):
        tempo = tempo
        datar = dataretirada
        datad = datadevolucao
        datar_formatada = strptime(datar, "%d/%m/%Y")
        datad_formatada = strptime(datad, "%d/%m/%Y")
        horar = horaretirada
        horad = horadevolucao
        tempo_max = self.conta_tempo(tempo)
        aux = 0
        tempo_reserva = 0
        tempo_max_ok = False
        horas_valores = ("00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00",
                         "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
                         "20:00", "21:00", "22:00", "23:00")

        for i in range(len(horas_valores)):
            if horas_valores[i] == horar:
                hora_ret_int = i
            if horas_valores[i] == horad:
                hora_dev_int = i
        if datar != datad:
            aux = 24 - hora_ret_int
            tempo_reserva = aux + hora_dev_int
        else:
            tempo_reserva = hora_dev_int - hora_ret_int

        if tempo_reserva <= tempo_max:
            tempo_max_ok = True

        return tempo_max_ok

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

    def deleteR(self):
        self.variaveisR()
        # self.delete(self.codigo)

        self.deletR(self.gcpf)
        self.limpar_dadosR()
        self.select_listR()

    def limpar_entries(self):
        self.vPesquisa_ReservaT.delete(0, END)
        self.vPesquisa_ReservaF.delete(0, END)
        self.data_retirada.delete(0, END)
        self.data_devolucao.delete(0, END)
        self.horas_ret.set("00:00")
        self.horas_dev.set("00:00")

    # def gera_cod(self):
    #     self.view_frame3.delete(*self.view_frame3.get_children())
    #     lista = self.leitorR()
    #     codr = len(lista)
    #     return codr

    def add_reserva(self):
        # cod_reserva = self.gera_cod()
        self.variaveisR()
        data_disponivel = self.valida_disp(self.gcod, self.dataretirada, self.horaretirada, self.horadevolucao)
        tempo_valido = self.verifica_tempo(self.gtempo, self.dataretirada, self.datadevolucao, self.horaretirada, self.horadevolucao)
        data_valido = self.verifica_data(self.dataretirada, self.datadevolucao, self.horaretirada, self.horadevolucao)
        while True:
            if data_valido:
                if tempo_valido:
                    if data_disponivel:

                        self.appendR(self.gcpf, self.gnome, self.gtel, self.gcod, self.gdes, self.gvolt, self.gtipo,
                                     self.dataretirada, self.horaretirada, self.datadevolucao, self.horadevolucao)
                        self.select_listR()

                    else:
                        messagebox.showerror("Erro",
                                             "A ferramenta não está disponível para essa data.")
                else:
                    messagebox.showerror("Erro", "O tempo total da reserva excede o permitido para essa ferramenta.")
            else:
                messagebox.showerror("Erro", "A data de devolução não pode ser inferior a de retirada.")


            break
        # self.res = tk.Label(self.frame_4, text=f"{contador} Cadastro(s) efetuado(s) com sucesso!", bg="#868B8E",
        #                             fg="#ffd", font=("poppins", 16, 'bold'))
        # self.res.place(relx=0.01, rely=0.2, relwidth=0.98, relheight=0.7)
        self.limpar_dadosR()

    def confirma(self):
        resposta = askyesno(title="Exclusão de reserva",  message="Confirma a exclusão da reserva selecionada?")
        if resposta:
            self.deleteR()


    # funções do calendário
    def calendario1(self):
        self.calendario1 = Calendar(self.cadastro_reservas, fg="gray75", bg="blue", font=("poppins", "9", "bold"), locale="pt_br", mindate=datetime.now() + timedelta(days=1))
        self.calendario1.place(relx=0.22, rely=0.25)
        self.cal_data_retirada = tk.Button(self.cadastro_reservas, text="Inserir data", command=self.puxar_data_ret)
        self.cal_data_retirada.place(relx=0.22, rely=0.56, height=25, width=100)

    def calendario2(self):
        self.calendario2 = Calendar(self.cadastro_reservas, fg="gray75", bg="blue", font=("poppins", "9", "bold"),
                                    locale="pt_br", mindate=datetime.now() + timedelta(days=1))
        self.calendario2.place(relx=0.63, rely=0.25)
        self.cal_data_devolucao = tk.Button(self.cadastro_reservas, text="Inserir data", command=self.puxar_data_dev)
        self.cal_data_devolucao.place(relx=0.71, rely=0.56, height=25, width=100)

    def puxar_data_ret(self):
        data_inicial = self.calendario1.get_date()
        self.data_retirada.delete(0, END)
        self.data_retirada.insert(END, data_inicial)
        self.calendario1.destroy()
        self.cal_data_retirada.destroy()

    def puxar_data_dev(self):
        data_final = self.calendario2.get_date()
        self.data_devolucao.delete(0, END)
        self.data_devolucao.insert(END, data_final)
        self.calendario2.destroy()
        self.cal_data_devolucao.destroy()
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
        self.frame_1.place(relx=0.01, rely=0.006, relwidth=0.98, relheight=0.23)

        self.frame_2 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_2.place(relx=0.01, rely=0.245, relwidth=0.98, relheight=0.23)

        self.frame_3 = Frame(self.cadastro_reservas, bd=4, bg="#868B8E", highlightbackground="#0D0D0D",
                             highlightthickness=1)
        self.frame_3.place(relx=0.01, rely=0.62, relwidth=0.98, relheight=0.37)
        
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


    # Botão calendário retirada
    
        self.bt_calendario = tk.Button(self.cadastro_reservas, text='Data da Retirada', font=('poppins', 12, 'bold'), command=self.calendario1)
        self.bt_calendario.place(relx=0.02, rely=0.5, relwidth=0.14, relheight=0.04)

    # Entry retirada
    
        self.data_retirada = tk.Entry(self.cadastro_reservas, width=4)
        self.data_retirada.place(relx=0.17, rely=0.5, relwidth=0.07, relheight=0.04)
        
    # Botão calendário devolução

        self.bt_calendario_entrega = tk.Button(self.cadastro_reservas, text='Data da Devolução',font=('poppins', 12, 'bold'), command=self.calendario2)
        self.bt_calendario_entrega.place(relx=0.53, rely=0.5, relwidth=0.14, relheight=0.04)

    # Entry devolução
    
        self.data_devolucao = tk.Entry(self.cadastro_reservas, width=4)
        self.data_devolucao.place(relx=0.68, rely=0.5, relwidth=0.07, relheight=0.04)


        self.horas_ret = tk.StringVar(self.cadastro_reservas)
        self.horas_dev = tk.StringVar(self.cadastro_reservas)
        self.horas_valores = ("00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00",
                              "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
                              "20:00", "21:00","22:00", "23:00")
        self.horas_ret.set("00:00")
        self.horas_dev.set("00:00")

    # Combobox hora retirada
    
        self.hora_menu_retirada = tk.OptionMenu(self.cadastro_reservas, self.horas_ret, *self.horas_valores)
        self.hora_menu_retirada.place(relx=0.40, rely=0.5, relwidth=0.07, relheight=0.04)

    # Combobox hora devolução
    
        self.hora_menu_devolucao = tk.OptionMenu(self.cadastro_reservas, self.horas_dev, *self.horas_valores)
        self.hora_menu_devolucao.place(relx=0.91, rely=0.5, relwidth=0.07, relheight=0.04)

    # Label hora retirada

        self.hora_menu_retirada_label = tk.Label(self.cadastro_reservas, text='Hora da Retirada:', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 12, 'bold'))
        self.hora_menu_retirada_label.place(relx=0.25, rely=0.5, relwidth=0.14, relheight=0.04)
        
    # Label hora devolução

        self.hora_menu_devolucao_label = tk.Label(self.cadastro_reservas, text='Hora da Devolução:', bg='#ffd', fg='#0D0D0D',
                                          font=('poppins', 12, 'bold'))
        self.hora_menu_devolucao_label.place(relx=0.76, rely=0.5, relwidth=0.14, relheight=0.04)



        
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
        self.Gtempo = tk.Entry(self.frame_2, bd=3, font=('poppins', 11, 'bold'))
        self.Gtempo.place(relx=0.00, rely=0.00, relwidth=0.0, relheight=0.0)

#------------------------------------------------------------
        ##  OUTROS BOTÕES, ENTRYS E LEBELS

        self.limpacamp = tk.Button(self.cadastro_reservas, text="Limpar Campos", bd=5, command=self.limpar_entries)
        self.limpacamp.place(relx=0.31, rely=0.56, relwidth=0.08, relheight=0.04)

        self.bupR = tk.Button(self.cadastro_reservas, text="Reservar", bd=5, command= self.add_reserva)
        self.bupR.place(relx=0.41, rely=0.56, relwidth=0.08, relheight=0.04)

        self.btdel = tk.Button(self.cadastro_reservas, text="Delete", bd=5, command=self.confirma)
        self.btdel.place(relx=0.51, rely=0.56, relwidth=0.08, relheight=0.04)

        self.batR = tk.Button(self.cadastro_reservas, text="Atualizar Lista", bd=5, command=self.select_listR)
        self.batR.place(relx=0.61, rely=0.56, relwidth=0.08, relheight=0.04)

        self.butxls = tk.Button(self.cadastro_reservas, text="Gerar Arquivo XLSX", bd=5, command=ccx.exportxlsR)
        self.butxls.place(relx=0.85, rely=0.56, relwidth=0.12, relheight=0.04)
        
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
        self.view_frame2.column("codigo", minwidth=0, width=130, anchor=tk.CENTER)
        self.view_frame2.column("descricao", minwidth=0, width=480, anchor=tk.CENTER)
        self.view_frame2.column("fabricante", minwidth=0, width=210, anchor=tk.CENTER)
        self.view_frame2.column("voltagem", minwidth=0, width=210, anchor=tk.CENTER)
        self.view_frame2.column("partnumber", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tamanho", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("unidade", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tipo", minwidth=0, width=210, anchor=tk.CENTER)
        self.view_frame2.column("material", minwidth=0, width=0, anchor=tk.CENTER)
        self.view_frame2.column("tempo", minwidth=0, width=220, anchor=tk.CENTER)

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
        self.view_frame3.column("cpf", minwidth=0, width=110, anchor=tk.CENTER)
        self.view_frame3.column("nome", minwidth=0, width=170, anchor=tk.CENTER)
        self.view_frame3.column("telefone", minwidth=0, width=140, anchor=tk.CENTER)
        self.view_frame3.column("codigo", minwidth=0, width=80, anchor=tk.CENTER)
        self.view_frame3.column("descricao", minwidth=0, width=200, anchor=tk.CENTER)
        self.view_frame3.column("voltagem", minwidth=0, width=90, anchor=tk.CENTER)
        self.view_frame3.column("tipo", minwidth=0, width=100, anchor=tk.CENTER)
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
