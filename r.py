import tkinter as tk

def janela_cadastro_reservas():
    cadastro_reservas = tk.Toplevel()
    cadastro_reservas.title('Janela de Cadastro de Reservas')
    cadastro_reservas.iconphoto(False, tk.PhotoImage(file='ico/reserva.png'))
    cadastro_reservas.configure(background='#B9B7BD')
    cadastro_reservas.geometry('700x500')
    cadastro_reservas.resizable(True, True)
    cadastro_reservas.maxsize(width= 900, height=600) # dimensões máximas
    cadastro_reservas.minsize(width= 400, height= 300) # dimensões mínimas
    

def janela_consulta_reservas():
    consulta_reservas = tk.Toplevel()
    consulta_reservas.title('Janela de Consulta de Reservas')
    consulta_reservas.iconphoto(False, tk.PhotoImage(file='ico/reserva.png'))
    consulta_reservas.configure(background='#B9B7BD')
    consulta_reservas.geometry('700x500')
    consulta_reservas.resizable(True, True)
    consulta_reservas.maxsize(width= 900, height=600) # dimensões máximas
    consulta_reservas.minsize(width= 400, height= 300) # dimensões mínimas