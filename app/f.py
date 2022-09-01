from msilib.schema import ComboBox
import tkinter as tk
from t import *
import csv


def janela_cadastro_ferramentas():

    global lista_ferramentas
    lista_ferramentas = []
    global contador
    contador = 0

    def codigo_ferramentas():
        codigo = vcodigo_ferramenta.get()
        while True:
            try:
                codigo = int(codigo)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "CPF: Digite apenas números")
            else:
                res1 = codigo
            break
            
        descricao = vdescricao_ferramenta.get()
        res2 = descricao.capitalize()

        fabricante = vfabricante.get()
        res3 = fabricante.capitalize()

        voltagem = vvoltagem.get()
        while True:
            try:
                voltagem = int(voltagem)
            except (ValueError, TypeError):
                messagebox.showerror("Erro", "CPF: Digite apenas números")
            else:
                res4 = voltagem
            break

        part_number = vpart_number.get()
        res5 = part_number.lower()
        # sugestões

        tamanho = vtamanho.get()
        res6 = tamanho
        # sugestões

        unidade_medida = vunidade_medida.get()
        res7 = unidade_medida.lower()
        # sugestões

        tipo_ferramenta = vtipo_ferramenta.get()
        res8 = tipo_ferramenta.lower()
        # sugestões 
        material = vmaterial_ferramenta.get()
        res9 = material.lower()
        #lista_ferramentas.append((codigo, descricao, fabricante, voltagem, part_number, tamanho, unidade_medida, tipo_ferramenta, material))

#--------------------------------------------------------------------------------------------

        with open("ferramenta.csv", "a", newline="") as arquivo:
            campos = ["Codigo", "Descricao", "Fabricante", "Voltagem", "Partnumber","Tamanho","Unidade","Tipo","Material"]
            escrever = csv.DictWriter(arquivo, fieldnames=campos, delimiter=",", lineterminator="\n")
            # não consegui manter o cabeçalho, ele repetia. Inseri no csv e permiti apenas a inserção das linhas
            #escrever.writeheader()

            escrever.writerow({"Codigo": res1, "Descricao": res2, "Fabricante": res3, "Voltagem": res4, "Partnumber": res5, "Tamanho": res6, "Unidade": res7, "Tipo": res8, "Material": res9})
            limpa_tela()
            global contador
            contador += 1  
            res = tk.Label(cadastro_ferramentas, text=f"{contador} Cadastro(s) efetuado(s) com sucesso!\nDigite novamente para mais um cadastro", bg="#B9B7BD", font= ("verdana", 11))
            res.place(relx= 0.10, rely= 0.70, relwidth = 0.8, relheight=0.1)

        

    # função para limpar os campos do entry, para nova digitação

    def limpa_tela(): 
        vcodigo_ferramenta.delete(0, END)
        vdescricao_ferramenta.delete(0, END)
        vfabricante.delete(0, END)
        vvoltagem.delete(0, END)
        vpart_number.delete(0, END)
        vtamanho.delete(0, END)
        vunidade_medida.delete(0, END)
        vtipo_ferramenta.delete(0, END)
        vmaterial_ferramenta.delete(0, END)

#------------------------------------------------------------------------------------------------    

    cadastro_ferramentas = tk.Toplevel()
    cadastro_ferramentas.title('Janela de Cadastro de Ferramentas')
    cadastro_ferramentas.iconphoto(False, tk.PhotoImage(file='ico/tools.png'))
    cadastro_ferramentas.configure(background='#B9B7BD')
    cadastro_ferramentas.geometry('700x500')
    cadastro_ferramentas.resizable(True, True)
    cadastro_ferramentas.maxsize(width= 900, height=600) # dimensões máximas
    cadastro_ferramentas.minsize(width= 400, height= 300) # dimensões mínimas

    codigo_ferramenta = tk.Label(cadastro_ferramentas, text='Código da Ferramenta:', bg='#ffd')
    codigo_ferramenta.place(relx=0.05, rely=0.02, relwidth= 0.25, relheight= 0.05)
    vcodigo_ferramenta = tk.Entry(cadastro_ferramentas)
    vcodigo_ferramenta.place(relx= 0.35, rely=0.02, relwidth=0.5, relheight=0.05)
    
    descricao_ferramenta = tk.Label(cadastro_ferramentas, text= 'Descrição da Ferramenta:', bg= '#ffd')
    descricao_ferramenta.place(relx= 0.05, rely= 0.08, relwidth= 0.25, relheight= 0.05)
    vdescricao_ferramenta = tk.Entry(cadastro_ferramentas)
    vdescricao_ferramenta.place(relx = 0.35, rely= 0.08, relwidth= 0.5, relheight= 0.05)
    
    fabricante = tk.Label(cadastro_ferramentas, text='Fabricante: ', bg='#ffd')
    fabricante.place(relx= 0.05, rely = 0.14, relwidth= 0.25, relheight=0.05)
    vfabricante = tk.Entry(cadastro_ferramentas)
    vfabricante.place(relx= 0.35, rely= 0.14, relwidth= 0.5, relheight=0.05)
    
    voltagem = tk.Label(cadastro_ferramentas, text='Voltagem de Uso:', bg='#ffd')
    voltagem.place(relx=0.05, rely= 0.2, relwidth=0.25, relheight=0.05)
    vvoltagem = tk.Entry(cadastro_ferramentas)
    vvoltagem.place(relx= 0.35, rely = 0.2, relwidth=0.5, relheight=0.05)
    
    part_number = tk.Label(cadastro_ferramentas, text= 'Part Number:', bg='#ffd')
    part_number.place(relx= 0.05, rely= 0.26, relwidth=0.25, relheight=0.05)
    vpart_number = tk.Entry(cadastro_ferramentas)
    vpart_number.place(relx= 0.35, rely= 0.26, relwidth=0.5, relheight=0.05)
    
    tamanho = tk.Label(cadastro_ferramentas, text='Tamanho da Ferramenta:', bg='#ffd')
    tamanho.place(relx=0.05, rely= 0.32, relwidth=0.25, relheight=0.05)
    vtamanho = tk.Entry(cadastro_ferramentas)
    vtamanho.place(relx=0.35, rely= 0.32, relwidth=0.5, relheight=0.05)
    
    unidade_medida = tk.Label(cadastro_ferramentas, text='Unidade de Medida:', bg='#ffd')
    unidade_medida.place(relx= 0.05, rely= 0.38, relwidth=0.25, relheight=0.05)
    vunidade_medida = tk.Entry(cadastro_ferramentas)
    vunidade_medida.place(relx=0.35, rely= 0.38, relwidth= 0.5, relheight=0.05)
    
    tipo_ferramenta = tk.Label(cadastro_ferramentas, text='Tipo da Ferramenta:', bg='#ffd')
    tipo_ferramenta.place(relx= 0.05, rely=0.44, relwidth=0.25, relheight=0.05)
    vtipo_ferramenta = tk.Entry(cadastro_ferramentas)
    vtipo_ferramenta.place(relx= 0.35, rely=0.44, relwidth=0.5, relheight=0.05)
    
    material_ferramenta = tk.Label(cadastro_ferramentas, text='Material da Ferramenta', bg='#ffd')
    material_ferramenta.place(relx= 0.05, rely= 0.5, relwidth=0.25, relheight=0.05)
    vmaterial_ferramenta = tk.Entry(cadastro_ferramentas)
    vmaterial_ferramenta.place(relx = 0.35, rely=0.5, relwidth=0.5, relheight=0.05)
    
    bsalvar = tk.Button(cadastro_ferramentas, text= 'Salvar Cadastro', command = codigo_ferramentas)
    bsalvar.place(relx= 0.29, rely = 0.6, relwidth=0.2, relheight=0.05)

    blimpar = tk.Button(cadastro_ferramentas, text="Limpar Campos", command=limpa_tela)
    blimpar.place(relx=0.50, rely=0.6, relwidth=0.2, relheight=0.05)

    res = tk.Label(cadastro_ferramentas, text="Insira acima os dados da ferramenta", bg="#B9B7BD",font= ("verdana",11))
    res.place(relx= 0.10, rely= 0.70, relwidth = 0.8, relheight=0.05)


def janela_consulta_ferramentas():
    consulta_ferramentas = tk.Toplevel()
    consulta_ferramentas.title('Janela de Consulta de Ferramentas')
    consulta_ferramentas.iconphoto(False, tk.PhotoImage(file='ico/tools.png'))
    consulta_ferramentas.configure(background='#B9B7BD')
    consulta_ferramentas.geometry('700x500')
    consulta_ferramentas.resizable(True, True)
    consulta_ferramentas.maxsize(width= 1280, height=720) # dimensões máximas
    consulta_ferramentas.minsize(width= 1280, height= 720) # dimensões mínimas
    #combobox = ttk.Combobox(consulta_ferramentas, values= lista_ferramentas)
    #combobox.place(relx=0.02, rely=0.15, relwidth=0.98, relheight=0.05)

    frame2 = ttk.Frame(consulta_ferramentas, width=600, height=300)

    hscrollbar1 = ttk.Scrollbar(frame2, orient=tk.HORIZONTAL)
    vscrollbar1 = ttk.Scrollbar(frame2, orient=tk.VERTICAL)
    sizegrip1 = ttk.Sizegrip(frame2)
    canvas1 = tk.Canvas(frame2, bd=0, highlightthickness=0, yscrollcommand=vscrollbar1.set, xscrollcommand=hscrollbar1.set)
    vscrollbar1.config(command=canvas1.yview)
    hscrollbar1.config(command=canvas1.xview)
    
    subframe1 = ttk.Frame(canvas1)

    with open("ferramenta.csv", newline="") as arquivof:
        reader1 = csv.reader(arquivof)
        r = 0
        for col in reader1:
            c = 0
            for row in col:
                label = tk.Label(subframe1, height=2,text=row, relief=tk.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    subframe1.pack(fill=tk.BOTH, expand=tk.TRUE)
    hscrollbar1.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
    vscrollbar1.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
    sizegrip1.pack(in_=hscrollbar1, side=tk.BOTTOM, anchor="se")
    canvas1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=tk.TRUE)
    frame2.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

    canvas1.create_window(0, 0, window=subframe1)
    consulta_ferramentas.update_idletasks()
    canvas1.config(scrollregion=canvas1.bbox("all"))
    canvas1.xview_moveto(0)
    canvas1.yview_moveto(0)

    #consulta_ferramentas.maxsize(width= 900, height=600) # dimensões máximas
    #consulta_ferramentas.minsize(width= 400, height= 300) # dimensões mínimas
