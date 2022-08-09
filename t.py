import tkinter as tk
from tkinter import ttk
import csv

tecnico = dict()

def janela_cadastro_tecnicos():
    
    global lista_tecnicos
    lista_tecnicos = []

    def codigo_tecnicos():

        tecnico['cpf'] = vcpf.get()
        tecnico['nome'] = vnome.get()
        tecnico['telefone'] = vtelefone.get()
        tecnico['turno'] = vturno.get()
        tecnico['equipe'] = vequipe.get()
        lista_tecnicos.append(tecnico.copy())
        print(lista_tecnicos)
        return tecnico

    with open('tecnico.csv', 'w', newline='') as arquivo:
        campos = ['CPF', 'Nome', 'Telefone', 'Turno', 'Equipe']
        escrever = csv.DictWriter(arquivo, fieldnames=campos)
        escrever.writeheader()
        escrever.writerow(tecnico)

    cadastro_tecnicos = tk.Toplevel()
    cadastro_tecnicos.title('Janela de Cadastro de Técnicos')
    cadastro_tecnicos.iconphoto(False, tk.PhotoImage(file='ico/worker.png'))
    cadastro_tecnicos.configure(background='#B9B7BD')
    cadastro_tecnicos.geometry('700x500')
    cadastro_tecnicos.resizable(True, True)
    cadastro_tecnicos.maxsize(width= 900, height=600) # dimensões máximas
    cadastro_tecnicos.minsize(width= 400, height= 300) # dimensões mínimas
    cpf = tk.Label(cadastro_tecnicos, text="CPF:", bg='#ffd')
    cpf.place(relx=0.05, rely=0.02, relwidth=0.1, relheight=0.05)
    vcpf = tk.Entry(cadastro_tecnicos)
    vcpf.place(relx=0.2, rely=0.02, relwidth=0.5, relheight=0.05)
    nome = tk.Label(cadastro_tecnicos, text='Nome:', bg='#ffd')
    nome.place(relx=0.05, rely=0.08, relwidth=0.1, relheight=0.05)
    vnome = tk.Entry(cadastro_tecnicos)
    vnome.place(relx = 0.2, rely= 0.08, relwidth= 0.5, relheight= 0.05)
    telefone = tk.Label(cadastro_tecnicos, text='Telefone:', bg='#ffd')
    telefone.place(relx= 0.05, rely= 0.14, relwidth = 0.1, relheight=0.05)
    vtelefone = tk.Entry(cadastro_tecnicos)
    vtelefone.place(relx= 0.2, rely= 0.14, relwidth= 0.5, relheight=0.05)
    turno = tk.Label(cadastro_tecnicos, text='Turno:', bg='#ffd')
    turno.place(relx= 0.05, rely = 0.2, relwidth=0.1, relheight=0.05)
    vturno = tk.Entry(cadastro_tecnicos)
    vturno.place(relx= 0.2, rely= 0.2, relwidth= 0.5, relheight= 0.05)
    equipe = tk.Label(cadastro_tecnicos, text='Equipe:', bg='#ffd')
    equipe.place(relx=0.05, rely= 0.26, relwidth=0.1, relheight=0.05)
    vequipe = tk.Entry(cadastro_tecnicos)
    vequipe.place(relx= 0.2, rely= 0.26, relwidth=0.5, relheight=0.05)
    bsalvar = tk.Button(cadastro_tecnicos, text='Salvar Cadastro', command= codigo_tecnicos)
    bsalvar.place(relx = 0.33, rely= 0.35, relwidth=0.2, relheight= 0.05)    
    

    
def janela_consulta_tecnicos():
    consulta_tecnicos = tk.Toplevel()
    consulta_tecnicos.title('Janela de Consulta de Técnicos')
    consulta_tecnicos.iconphoto(False, tk.PhotoImage(file='ico/worker.png'))
    consulta_tecnicos.configure(background='#B9B7BD')
    consulta_tecnicos.geometry('700x500')
    consulta_tecnicos.resizable(True, True)
    consulta_tecnicos.maxsize(width= 900, height=600) # dimensões máximas
    consulta_tecnicos.minsize(width= 400, height= 300) # dimensões mínimas
    combobox = ttk.Combobox(consulta_tecnicos, values= lista_tecnicos)
    combobox.place(relx = 0.02, rely= 0.15, relwidth=0.75, relheight=0.05)