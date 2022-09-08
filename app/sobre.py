import tkinter as tk
from tecnico import TK

# janela_sobre =  tk.Tk()
class sobre():
    def janela_sobre(self):
            
            self.sobre = tk.Toplevel()
            self.sobre.title('Sobre')
            self.sobre.iconphoto(False, tk.PhotoImage(file='../ico/info.png'))
            self.sobre.configure(background='#B9B7BD')
            self.sobre.geometry('800x700')
            self.sobre.resizable(True, True)
            self.sobre.minsize(width=600, height=400)

            self.frame_sobre = tk.Frame(self.sobre, bd= 4, bg='#fff',
                                      highlightbackground='#868B8E',
                                      highlightthickness=2)
            self.frame_sobre.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.92)
            
# Logotipo ----------------------------------------------------------------------

            self.logo_estacio = tk.PhotoImage(file='../ico/logo1.png')
            self.label_logo = tk.Label(self.frame_sobre, image=self.logo_estacio)
            self.label_logo.place(relx=0.01, rely=0.10, relwidth=0.385, relheight=0.35)
            
# Nome do curso --------------------------------------------------------------

            self.label_nome = tk.Label(self.frame_sobre, text="Nome do Curso", bg='#fff', font=('poppins', 14, 'bold'))
            self.label_nome.place(relx=0.2, rely=0.40, relwidth=0.15, relheight=0.05)
            
# Mundo --------------------------------------------------------------------------

            self.label_mundo = tk.Label(self.frame_sobre, text="Mundo", bg='#fff', font=('poppins', 14, 'bold'))
            self.label_mundo.place(relx=0.2, rely=0.50, relwidth=0.15, relheight=0.05)
            
# Turma --------------------------------------------------------------------------

            self.label_turma = tk.Label(self.frame_sobre, text="Turma", bg='#fff', font=('poppins', 14, 'bold'))
            self.label_turma.place(relx=0.2, rely=0.60, relwidth=0.15, relheight=0.05)
            
# Semestre ----------------------------------------------------------------------

            self.label_semestre = tk.Label(self.frame_sobre, text="Semestre", bg='#fff', font=('poppins', 14, 'bold'))
            self.label_semestre.place(relx=0.2, rely=0.70, relwidth=0.15, relheight=0.05)
            
# Grupo ---------------------------------------------------------------------------

            self.label_grupo = tk.Label(self.frame_sobre, text="Grupo", bg='#fff', font=('poppins', 14, 'bold'))
            self.label_grupo.place(relx=0.2, rely=0.80, relwidth=0.385, relheight=0.35)
            
# Integrantes --------------------------------------------------------------------

            self.label_integ = tk.Label(self.frame_sobre, text="Integrantes", bg='#fff', font=('poppins', 14, 'bold'))
            self.label_integ.place(relx=0.2, rely=0.90, relwidth=0.15, relheight=0.05)

            
            

# Botão encerrar -----------------------------------------------------------------
           
            self.bt_fechar = tk.Button(self.sobre, text="Encerrar", bd=5, command=self.sobre.destroy)
            self.bt_fechar.place(relx=0.40, rely=0.93, relwidth=0.20, relheight=0.05)

           
