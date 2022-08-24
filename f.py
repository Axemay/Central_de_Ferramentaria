from msilib.schema import ComboBox
import tkinter as tk
from t import *



def janela_cadastro_ferramentas():

    global lista_ferramentas
    lista_ferramentas = []
    global contador
    contador = 0

    def codigo_ferramentas():
        codigo = ('Código: {}').format(vcodigo_ferramenta.get())
        descricao = ('Descrição da Ferramenta: {}').format(vdescricao_ferramenta.get())
        fabricante = ('Fabricante: {}').format(vfabricante.get())
        voltagem = ('Voltagem de Uso: {}').format(vvoltagem.get())
        part_number = ('Part Number: {}').format(vpart_number.get())
        tamanho = ('Tamanho da Ferramenta: {}').format(vtamanho.get())
        unidade_medida = ('Unidade de Medida: {}').format(vunidade_medida.get())
        tipo_ferramenta = ('Tipo de Ferramenta: {}').format(vtipo_ferramenta.get())
        material = ('Material: {}').format(vmaterial_ferramenta.get())
        lista_ferramentas.append((codigo, descricao, fabricante, voltagem, part_number, tamanho, unidade_medida, tipo_ferramenta, material))

#--------------------------------------------------------------------------------------------

        with open("ferramenta.csv", "a", newline="") as arquivo:
            campos = ["Codigo", "Descricao", "Fabricante", "Voltagem", "Partnumber","Tamanho","Unidade","Tipo","Material"]
            escrever = csv.DictWriter(arquivo, fieldnames=campos, delimiter=",", lineterminator="\n")
            # não consegui manter o cabeçalho, ele repetia. Inseri no csv e permiti apenas a inserção das linhas
            #escrever.writeheader()

            escrever.writerow({"Codigo": vcodigo_ferramenta.get(), "Descricao": vdescricao_ferramenta.get(), "Fabricante": vfabricante.get(), "Voltagem": vvoltagem.get(), "Partnumber": vpart_number.get(), "Tamanho": vtamanho.get(), "Unidade": vunidade_medida.get(), "Tipo": vtipo_ferramenta.get(), "Material": vmaterial_ferramenta.get()})
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
    #cadastro_ferramentas.iconphoto(False, tk.PhotoImage(file='ico/tools.png'))
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
    #consulta_ferramentas.iconphoto(False, tk.PhotoImage(file='ico/tools.png'))
    consulta_ferramentas.configure(background='#B9B7BD')
    consulta_ferramentas.geometry('700x500')
    consulta_ferramentas.resizable(True, True)
<<<<<<< Updated upstream
    consulta_ferramentas.maxsize(width= 1280, height=720) # dimensões máximas
    consulta_ferramentas.minsize(width= 1280, height= 720) # dimensões mínimas
    #combobox = ttk.Combobox(consulta_ferramentas, values= lista_ferramentas)
    #combobox.place(relx=0.02, rely=0.15, relwidth=0.98, relheight=0.05)

    frame2 = Frame(consulta_ferramentas,bd= 4, bg="#ffffff", highlightbackground="grey", highlightthickness=2)
    frame2.place(relx= 0.01, rely=0.02, relwidth=0.98, relheight=0.65)
    
=======
    #consulta_ferramentas.maxsize(width= 900, height=600) # dimensões máximas
    #consulta_ferramentas.minsize(width= 400, height= 300) # dimensões mínimas
>>>>>>> Stashed changes
