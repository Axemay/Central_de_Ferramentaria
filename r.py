from secrets import randbelow
import tkinter as tk
from tkinter import ttk
from t import *
from f import *

def janela_cadastro_reservas():

    global lista_reserva
    lista_reserva = []

    def salvar_reserva():
        tecnico = comb_tecnicos.get()
        ferramenta = comb_ferramentas.get()
        lista_reserva.append((tecnico, ferramenta))

    cadastro_reservas = tk.Toplevel()
    cadastro_reservas.title('Janela de Cadastro de Reservas')
    cadastro_reservas.iconphoto(False, tk.PhotoImage(file='ico/reserva.png'))
    cadastro_reservas.configure(background='#B9B7BD')
    cadastro_reservas.geometry('700x500')
    cadastro_reservas.resizable(True, True)
    cadastro_reservas.maxsize(width= 900, height=600) # dimensões máximas
    cadastro_reservas.minsize(width= 400, height= 300) # dimensões mínimas
    comb_tecnicos = ttk.Combobox(cadastro_reservas, )
    comb_tecnicos.place(relx = 0.02, rely= 0.15, relwidth=0.75, relheight=0.05)
    comb_ferramentas = ttk.Combobox(cadastro_reservas,)
    comb_ferramentas.place(relx = 0.02, rely= 0.25, relwidth=0.75, relheight=0.05)
    bsalvar = tk.Button(cadastro_reservas, text='Salvar Cadastro', bg='#ffd', )
    bsalvar.place(relx = 0.33, rely = 0.35, relwidth=0.35 ,relheight= 0.05)
    

def janela_consulta_reservas():
    consulta_reservas = tk.Toplevel()
    consulta_reservas.title('Janela de Consulta de Reservas')
    consulta_reservas.iconphoto(False, tk.PhotoImage(file='ico/reserva.png'))
    consulta_reservas.configure(background='#B9B7BD')
    consulta_reservas.geometry('700x500')
    consulta_reservas.resizable(True, True)
    consulta_reservas.maxsize(width= 900, height=600) # dimensões máximas
    consulta_reservas.minsize(width= 400, height= 300) # dimensões mínimas
    combobox = ttk.Combobox(consulta_reservas, values=lista_reserva)
    combobox.place(relx= 0.2, rely= 0.15, relwidth= 0.98, relheight=0.05)