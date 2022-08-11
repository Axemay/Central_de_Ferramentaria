import tkinter as tk

from t import *
from r import *
from f import *

#nomedomodulo.nomedadef

# criar tela

janela = tk.Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.janela_config()
        self.frames()
        self.botoes()
        self.labels()
        janela.mainloop()


    def janela_config(self):
        self.janela.title('Controle de Ferramentas')
        self.janela.iconphoto(False, tk.PhotoImage(file='ico/tools.png'))
        self.janela.configure(background='#B9B7BD')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 900, height=600) # dimensões máximas
        self.janela.minsize(width= 400, height= 300) # dimensões mínimas

    def frames(self):
        self.frame_tecnico = tk.Frame(self.janela, bd= 4, bg='#fff',
                                      highlightbackground='#868B8E',
                                      highlightthickness=2)
        self.frame_tecnico.place(relx= 0.05, rely = 0.3, relwidth= 0.29, relheight = 0.5)

        self.frame_ferramenta = tk.Frame(self.janela, bd= 4, bg='#fff',
                                      highlightbackground='#868B8E',
                                      highlightthickness=2)
        self.frame_ferramenta.place(relx= 0.36, rely = 0.3, relwidth= 0.29, relheight = 0.5)

        self.frame_reserva = tk.Frame(self.janela, bd= 4, bg='#fff',
                                      highlightbackground='#868B8E',
                                      highlightthickness=2)
        self.frame_reserva.place(relx= 0.67, rely = 0.3, relwidth= 0.29, relheight = 0.5)

    def botoes(self):
        self.bt_cadastrar_tec = tk.Button(self.frame_tecnico, text="Cadastrar", command= janela_cadastro_tecnicos, bg='#B9B7BD')
        self.bt_cadastrar_tec.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.15)
        self.bt_consultar_tec = tk.Button(self.frame_tecnico, text="Consultar", bg='#B9B7BD', command= janela_consulta_tecnicos)
        self.bt_consultar_tec.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

        self.bt_cadastrar_ferramenta = tk.Button(self.frame_ferramenta, text="Cadastrar", bg='#B9B7BD', command= janela_cadastro_ferramentas)
        self.bt_cadastrar_ferramenta.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.15)
        self.bt_consultar_ferramenta = tk.Button(self.frame_ferramenta, text="Consultar", bg='#B9B7BD', command = janela_consulta_ferramentas)
        self.bt_consultar_ferramenta.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

        self.bt_cadastrar_reserva = tk.Button(self.frame_reserva, text="Cadastrar", bg='#B9B7BD', command= janela_cadastro_reservas)
        self.bt_cadastrar_reserva.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.15)
        self.bt_consultar_reserva = tk.Button(self.frame_reserva, text="Consultar", bg='#B9B7BD', command= janela_consulta_reservas)
        self.bt_consultar_reserva.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

    def labels(self):
        self.label_tec = tk.Label(self.frame_tecnico, text="Técnico", bg='#fff')
        self.img_tec = tk.PhotoImage(file='ico/worker.png')
        self.label_tec_Img = tk.Label(self.frame_tecnico, image=self.img_tec)
        self.label_tec.place(relx=0.4, rely=0.45, relwidth=0.25, relheight=0.1)
        self.label_tec_Img.place(relx=0.3, rely=0.0, relwidth=0.4, relheight=0.4)

        self.label_ferramenta = tk.Label(self.frame_ferramenta, text="Ferramenta", bg='#fff')
        self.img_ferramenta = tk.PhotoImage(file='ico/toolcard.png')
        self.label_ferramenta_Img = tk.Label(self.frame_ferramenta, image=self.img_ferramenta)
        self.label_ferramenta.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.1)
        self.label_ferramenta_Img.place(relx=0.3, rely=0.0, relwidth=0.5, relheight=0.4)

        self.label_reserva = tk.Label(self.frame_reserva, text="Reserva", bg='#fff')
        self.img_reserva = tk.PhotoImage(file='ico/reserva.png')
        self.label_reserva_Img = tk.Label(self.frame_reserva, image=self.img_reserva)
        self.label_reserva.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.1)
        self.label_reserva_Img.place(relx=0.2, rely=0.0, relwidth=0.6, relheight=0.4)

Aplicacao()

#axemay
#dpsndroid
