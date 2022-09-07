import tkinter as tk


def janela_sobre():
            
            sobre = tk.Tk()
            sobre.title('Sobre')
            sobre.configure(background='#B9B7BD')
            sobre.geometry('800x700')
            sobre.resizable(True, True)
            sobre.minsize(width=600, height=400)
            

            bt_fechar = tk.Button(sobre, text="Encerrar Manual", bd=5, command=sobre.destroy)
            bt_fechar.place(relx=0.40, rely=0.93, relwidth=0.20, relheight=0.05)

            

           

        
