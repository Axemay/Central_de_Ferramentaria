from contextlib import ContextDecorator
import tkinter as tk
from tkinter import Frame, ttk
from tkinter import END
from tkinter import messagebox
import csv


tecnico = dict()



def janela_cadastro_tecnicos():
    
    global lista_tecnicos
    lista_tecnicos = []

    global contador
    contador = 0

 ######### VERIFICAÇÃO DE ERROS, VALIDAÇÃO ########################           

    def codigo_tecnicos():
        cpf = vcpf.get()
        while True:
            if len(cpf) == 11:
                try:
                    cpf = int(cpf)
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "CPF: Digite apenas números")
                else:
                    res1 = cpf
            else:
                messagebox.showerror("Erro", "CPF: Insira exatamente 11 dígitos")
            break 
        
        nome = vnome.get()
        res2 = nome.title()
                
        tel = vtelefone.get()
        while True:
            if len(tel) == 10 or len(tel) == 11:
                try:
                    tel = int(tel)                
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "TELEFONE: Digite apenas números")
                else:
                    res3 = tel
            else:
                messagebox.showerror("Erro", "TELEFONE: Insira 10 dígitos para telefone fixo e 11 dígitos para celular, incluindo prefixo")
            break 

        turno = vturno.get()
        turno = turno.upper()
        while True:
            if turno == "M":
                res4 = turno
            elif turno == "T":
                res4 = turno
            elif turno == "N":
                res4 = turno
            else:
                messagebox.showerror("Erro", "TURNO: Os turnos disponíveis são: M, T ou N")
            break
        
        equipe = vequipe.get()
        while True:
            try:
                equipe = int(equipe)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "EQUIPE: Digite apenas números")
            else:
                res5 = equipe
            break
        
        #lista_tecnicos.append(tecnico.copy())
        #print(lista_tecnicos)
        #return tecnico
        
########### REGISTRO NO ARQUIVO CSV ##################################

        with open("tecnico.csv", "a", newline="") as arquivo:
            
            campos = ["CPF", "Nome", "Telefone", "Turno", "Equipe"]
            escrever = csv.DictWriter(arquivo, fieldnames=campos, delimiter=",", lineterminator="\n")
            # não consegui manter o cabeçalho, ele repetia. Inseri no csv e permiti apenas a inserção das linhas
            #escrever.writeheader()

            escrever.writerow({"CPF": res1, "Nome": res2, "Telefone": res3, "Turno": res4, "Equipe": res5}) 

            limpa_tela()

            global contador

            contador += 1  

            res = tk.Label(cadastro_tecnicos, text=f"{contador} Cadastro(s) efetuado(s) com sucesso!\nDigite novamente para mais um cadastro", bg="#B9B7BD", font= ("verdana", 11))
            res.place(relx= 0.05, rely= 0.50, relwidth = 0.8, relheight=0.1)
            
###### função para limpar os campos do entry, para nova digitação, tem que importar END do tkinter

    def limpa_tela(): 
        vcpf.delete(0, END)
        vnome.delete(0, END)
        vtelefone.delete(0, END)
        vturno.delete(0, END)
        vequipe.delete(0, END)

#------------------------------------------------------------------------------------------
    cadastro_tecnicos = tk.Toplevel()
    cadastro_tecnicos.title('Janela de Cadastro de Técnicos')
    cadastro_tecnicos.iconphoto(False, tk.PhotoImage(file='ico/worker.png'))
    cadastro_tecnicos.configure(background='#B9B7BD')
    cadastro_tecnicos.geometry('700x500')
    cadastro_tecnicos.resizable(True, True)
    cadastro_tecnicos.maxsize(width= 900, height=600) # dimensões máximas
    cadastro_tecnicos.minsize(width= 400, height= 300) # dimensões mínimas

############################   FRAMES   ######################################

    frame1 = Frame(cadastro_tecnicos)
    label1 = tk.Label(frame1, text="Label 1")
    frame1.place(relx= 0.00, rely=0.00, relwidth=0.75, relheight=0.35)

    frame2 = Frame(cadastro_tecnicos)
    label2 = tk.Label(frame2, text="Label 2")
    frame2.place(relx= 0.76, rely=0.00, relwidth=0.26, relheight=0.35)

    frame3 = Frame(cadastro_tecnicos)
    label3 = tk.Label(frame3, text="Label 3")
    frame3.place(relx= 0.00, rely=0.36, relwidth=1, relheight=0.46)


##############################################################################  

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
    
    bsalvar = tk.Button(frame2, text='Salvar Cadastro', command= codigo_tecnicos)
    bsalvar.place(relx = 0.05, rely= 0.20, relwidth=0.8, relheight= 0.15)

    blimpar = tk.Button(frame2, text="Limpar Campos", command=limpa_tela)
    blimpar.place(relx=0.05, rely=0.40, relwidth=0.8, relheight=0.15)

    res = tk.Label(frame3, text="Insira acima os dados do funcionário", bg="#B9B7BD",font= ("verdana",11))
    res.place(relx= 0.05, rely= 0.10, relwidth = 0.9, relheight=0.05)

    op = tk.Label(frame3, text="TURNO: Manhã (m), Tarde (t), Noite (n)\n\nCPF: 11 dígitos\n\nTelefone fixo: 10 dígitos, Celular: 11 dígitos", bg="#B9B7BD",font= ("verdana",9))
    op.place(relx= 0.05, rely= 0.25, relwidth = 0.9, relheight=0.45)


########################   CONSULTA TÉCNICOS     ####################


def janela_consulta_tecnicos():
    consulta_tecnicos = tk.Toplevel()
    consulta_tecnicos.title('Janela de Consulta de Técnicos')
    consulta_tecnicos.iconphoto(False, tk.PhotoImage(file='ico/worker.png'))
    consulta_tecnicos.configure(background='#B9B7BD')
    consulta_tecnicos.geometry('600x300')
    consulta_tecnicos.resizable(True, True)
    #consulta_tecnicos.maxsize(width= 900, height=600) # dimensões máximas
    consulta_tecnicos.minsize(width= 400, height= 300) # dimensões mínimas
    #combobox = ttk.Combobox(consulta_tecnicos, values= lista_tecnicos)
    #combobox.place(relx = 0.02, rely= 0.15, relwidth=0.75, relheight=0.05)

    
    frame2 = ttk.Frame(consulta_tecnicos, width=600, height=300)

    hscrollbar = ttk.Scrollbar(frame2, orient=tk.HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame2, orient=tk.VERTICAL)
    sizegrip = ttk.Sizegrip(frame2)
    canvas = tk.Canvas(frame2, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)
    
    subframe = ttk.Frame(canvas)

    with open("tecnico.csv", newline="") as arquivot:
        reader = csv.reader(arquivot)
        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tk.Label(subframe, height=2,text=row, relief=tk.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    subframe.pack(fill=tk.BOTH, expand=tk.TRUE)
    hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
    sizegrip.pack(in_=hscrollbar, side=tk.BOTTOM, anchor="se")
    canvas.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=tk.TRUE)
    frame2.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

    canvas.create_window(0, 0, window=subframe)
    consulta_tecnicos.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)





from contextlib import ContextDecorator
import tkinter as tk
from tkinter import Frame, ttk
from tkinter import END
from tkinter import messagebox
import csv


tecnico = dict()



def janela_cadastro_tecnicos():
    
    global lista_tecnicos
    lista_tecnicos = []

    global contador
    contador = 0

 ######### VERIFICAÇÃO DE ERROS, VALIDAÇÃO ########################           

    def codigo_tecnicos():
        cpf = vcpf.get()
        while True:
            if len(cpf) == 11:
                try:
                    cpf = int(cpf)
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "CPF: Digite apenas números")
                else:
                    res1 = cpf
            else:
                messagebox.showerror("Erro", "CPF: Insira exatamente 11 dígitos")
            break 
        
        nome = vnome.get()
        res2 = nome.title()
                
        tel = vtelefone.get()
        while True:
            if len(tel) == 10 or len(tel) == 11:
                try:
                    tel = int(tel)                
                except (ValueError, TypeError):
                    messagebox.showerror("Erro", "TELEFONE: Digite apenas números")
                else:
                    res3 = tel
            else:
                messagebox.showerror("Erro", "TELEFONE: Insira 10 dígitos para telefone fixo e 11 dígitos para celular, incluindo prefixo")
            break 

        turno = vturno.get()
        turno = turno.upper()
        while True:
            if turno == "M":
                res4 = turno
            elif turno == "T":
                res4 = turno
            elif turno == "N":
                res4 = turno
            else:
                messagebox.showerror("Erro", "TURNO: Os turnos disponíveis são: M, T ou N")
            break
        
        equipe = vequipe.get()
        while True:
            try:
                equipe = int(equipe)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "EQUIPE: Digite apenas números")
            else:
                res5 = equipe
            break
        
        #lista_tecnicos.append(tecnico.copy())
        #print(lista_tecnicos)
        #return tecnico
        
########### REGISTRO NO ARQUIVO CSV ##################################

        with open("tecnico.csv", "a", newline="") as arquivo:
            
            campos = ["CPF", "Nome", "Telefone", "Turno", "Equipe"]
            escrever = csv.DictWriter(arquivo, fieldnames=campos, delimiter=",", lineterminator="\n")
            # não consegui manter o cabeçalho, ele repetia. Inseri no csv e permiti apenas a inserção das linhas
            #escrever.writeheader()

            escrever.writerow({"CPF": res1, "Nome": res2, "Telefone": res3, "Turno": res4, "Equipe": res5}) 

            limpa_tela()

            global contador

            contador += 1  

            res = tk.Label(cadastro_tecnicos, text=f"{contador} Cadastro(s) efetuado(s) com sucesso!\nDigite novamente para mais um cadastro", bg="#B9B7BD", font= ("verdana", 11))
            res.place(relx= 0.05, rely= 0.50, relwidth = 0.8, relheight=0.1)
            
###### função para limpar os campos do entry, para nova digitação, tem que importar END do tkinter

    def limpa_tela(): 
        vcpf.delete(0, END)
        vnome.delete(0, END)
        vtelefone.delete(0, END)
        vturno.delete(0, END)
        vequipe.delete(0, END)

#------------------------------------------------------------------------------------------
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
    bsalvar.place(relx = 0.24, rely= 0.35, relwidth=0.2, relheight= 0.05)

    blimpar = tk.Button(cadastro_tecnicos, text="Limpar Campos", command=limpa_tela)
    blimpar.place(relx=0.46, rely=0.35, relwidth=0.2, relheight=0.05)

    res = tk.Label(cadastro_tecnicos, text="Insira acima os dados do funcionário", bg="#B9B7BD",font= ("verdana",11))
    res.place(relx= 0.05, rely= 0.50, relwidth = 0.8, relheight=0.05)

    op = tk.Label(cadastro_tecnicos, text="TURNO: Manhã (m), Tarde (t), Noite (n)\n\nCPF deve conter exatamente 11 dígitos\n\nTelefone deve conter 10 dígitos com prefixo incluso\n\nTodos os campos devem ser preenchidos", bg="#B9B7BD",font= ("verdana",9))
    op.place(relx= 0.05, rely= 0.60, relwidth = 0.8, relheight=0.40)
   
    
def janela_consulta_tecnicos():
    consulta_tecnicos = tk.Toplevel()
    consulta_tecnicos.title('Janela de Consulta de Técnicos')
    consulta_tecnicos.iconphoto(False, tk.PhotoImage(file='ico/worker.png'))
    consulta_tecnicos.configure(background='#B9B7BD')
    consulta_tecnicos.geometry('600x300')
    consulta_tecnicos.resizable(True, True)
    #consulta_tecnicos.maxsize(width= 900, height=600) # dimensões máximas
    consulta_tecnicos.minsize(width= 400, height= 300) # dimensões mínimas
    #combobox = ttk.Combobox(consulta_tecnicos, values= lista_tecnicos)
    #combobox.place(relx = 0.02, rely= 0.15, relwidth=0.75, relheight=0.05)

    
    frame1 = ttk.Frame(consulta_tecnicos, width=600, height=300)

    hscrollbar = ttk.Scrollbar(frame1, orient=tk.HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame1, orient=tk.VERTICAL)
    sizegrip = ttk.Sizegrip(frame1)
    canvas = tk.Canvas(frame1, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)
    
    subframe = ttk.Frame(canvas)

    with open("tecnico.csv", newline="") as arquivot:
        reader = csv.reader(arquivot)
        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tk.Label(subframe, height=2,text=row, relief=tk.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    subframe.pack(fill=tk.BOTH, expand=tk.TRUE)
    hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
    sizegrip.pack(in_=hscrollbar, side=tk.BOTTOM, anchor="se")
    canvas.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=tk.TRUE)
    frame1.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

    canvas.create_window(0, 0, window=subframe)
    consulta_tecnicos.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)





        