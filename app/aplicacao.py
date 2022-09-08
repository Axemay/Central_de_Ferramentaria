import tkinter as tk
import time
from tecnico import *
from ferramenta import *
from reserva import *
from sobre import *
import webbrowser

# criar tela

janela = tk.Tk()


class Aplicacao(TK, front_Ferramentas, Reserva, sobre):
    def __init__(self):
        TK.__init__(self)
        front_Ferramentas.__init__(self)
        self.janela = janela
        self.janela_config()
        self.frames()
        self.botoes()
        self.labels()

        janela.mainloop()

    def janela_config(self):
        self.janela.title('Central de Ferramentaria')
        self.janela.iconphoto(False, tk.PhotoImage(file='../ico/tools.png'))
        self.janela.configure(background='#B9B7BD')
        self.janela.geometry('1380x780')
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 1920, height=1080) # dimensões máximas
        self.janela.minsize(width= 400, height= 300) # dimensões mínimas

    def abrir_manual(self):
        webbrowser.open("manual.pdf")

    def frames(self):
        self.frame_titulo = tk.Frame(self.janela, bd=4, bg='#B9B7BD',
                                      highlightbackground='#B9B7BD',
                                      highlightthickness=2)
        self.frame_titulo.place(relx=0.05, rely=0, relwidth=0.91, relheight=0.3)

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

        self.frame_manual = tk.Frame(self.janela, bd=4, bg='#B9B7BD',
                                     highlightbackground='#B9B7BD',
                                     highlightthickness=2)
        self.frame_manual.place(relx=0.67, rely=0.8, relwidth=0.29, relheight=0.2)

        self.frame_copyright = tk.Frame(self.janela, bd=4, bg='#B9B7BD',
                                     highlightbackground='#B9B7BD',
                                     highlightthickness=2)
        self.frame_copyright.place(relx=0.05, rely=0.85, relwidth=0.5, relheight=0.1)

    def botoes(self):

        self.bt_cadastrar_tec = tk.Button(self.frame_tecnico, text="Acessar", command= self.janela_frontT, bd=3, font=('poppins', 19, 'bold'))
        self.bt_cadastrar_tec.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

        self.bt_cadastrar_ferramenta = tk.Button(self.frame_ferramenta, text="Acessar", bd=3, font=('poppins', 19, 'bold'), command= self.janela_frontF)
        self.bt_cadastrar_ferramenta.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

        self.bt_cadastrar_reserva = tk.Button(self.frame_reserva, text="Acessar", bd=3, font=('poppins', 19, 'bold'), command= self.janela_cadastro_reservas)
        self.bt_cadastrar_reserva.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

        self.bt_sobre = tk.Button(self.janela, text="Sobre", bd=5, command=self.janela_sobre)
        self.bt_sobre.place(relx=0.68, rely=0.90, relwidth=0.13, relheight=0.05)

        self.bt_manual = tk.Button(self.janela, text="Consultar Manual", bd=5, command=self.abrir_manual)
        self.bt_manual.place(relx=0.82, rely=0.90, relwidth=0.13, relheight=0.05)



    def labels(self):
        self.label_titulo = tk.Label(self.frame_titulo, text="Central de Ferramentaria", bg='#B9B7BD', font=('poppins', 50, 'bold'))
        self.label_titulo.place(relx=0.0, rely=0.3, relwidth=1, relheight=0.3)
        self.label_versao = tk.Label(self.frame_titulo, text="Versão 1.0", bg='#B9B7BD',
                                     font=('poppins', 15))
        self.label_versao.place(relx=0.0, rely=0.56, relwidth=1, relheight=0.3)

        self.label_tec = tk.Label(self.frame_tecnico, text="Técnico", bg='#fff', font=('poppins', 25, 'bold'))
        self.img_tec = tk.PhotoImage(file='../ico/worker.png')
        self.label_tec_Img = tk.Label(self.frame_tecnico, image=self.img_tec, bg='#fff')
        self.label_tec.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.2)
        self.label_tec_Img.place(relx=0.29, rely=0.05, relwidth=0.4, relheight=0.4)

        self.label_ferramenta = tk.Label(self.frame_ferramenta, text="Ferramenta", bg='#fff', font=('poppins', 25, 'bold'))
        self.img_ferramenta = tk.PhotoImage(file='../ico/toolcard.png')
        self.label_ferramenta_Img = tk.Label(self.frame_ferramenta, image=self.img_ferramenta, bg='#fff')
        self.label_ferramenta.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.2)
        self.label_ferramenta_Img.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.4)

        self.label_reserva = tk.Label(self.frame_reserva, text="Reserva", bg='#fff', font=('poppins', 25, 'bold'))
        self.img_reserva = tk.PhotoImage(file='../ico/reserva.png')
        self.label_reserva_Img = tk.Label(self.frame_reserva, image=self.img_reserva, bg='#fff')
        self.label_reserva.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.1)
        self.label_reserva_Img.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.4)

        self.label_copyright = tk.Label(self.frame_copyright, text="copyright © 2022 - Todos os direitos reservados - DevTeam13", bg='#B9B7BD',
                                     font=('poppins', 10, 'bold'))
        self.label_copyright.place(relx=0.0, rely=0, relwidth=0.65, relheight=0.3)

        

Aplicacao()

#axemay
#dpsndroid
#Rafinha
#fneto
