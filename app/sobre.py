import tkinter as tk


class sobre():
    def janela_sobre(self):
            
            self.sobre = tk.Toplevel()
            self.sobre.title('Sobre')
            self.sobre.iconphoto(False, tk.PhotoImage(file='../ico/info.png'))
            self.sobre.configure(background='#B9B7BD')
            self.sobre.geometry('1000x700')
            self.sobre.resizable(True, True)
            self.sobre.minsize(width=600, height=400)

            self.frame_sobre = tk.Frame(self.sobre, bd= 4, bg='#fff',
                                      highlightbackground='#fff',
                                      highlightthickness=2)
            self.frame_sobre.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.90)
            
# Logotipo ----------------------------------------------------------------------

            self.logo_estacio = tk.PhotoImage(file='../ico/logo1.png')
            self.label_logo = tk.Label(self.frame_sobre, image=self.logo_estacio,  bg='#fff')

            self.label_logo.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.15)

            
# Nome do curso --------------------------------------------------------------


            self.label_nome = tk.Label(self.frame_sobre, text="Nome do Curso:", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_nome.place(relx=0.2, rely=0.35, relwidth=0.2, relheight=0.05)
            self.label_nome_valor = tk.Label(self.frame_sobre, text="Desenvolvimento Full Stack", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_nome_valor.place(relx=0.4, rely=0.35, relwidth=0.5, relheight=0.05)
            
# Mundo --------------------------------------------------------------------------

            self.label_mundo = tk.Label(self.frame_sobre, text="Mundo:", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_mundo.place(relx=0.2, rely=0.41, relwidth=0.15, relheight=0.05)
            self.label_mundo_valor = tk.Label(self.frame_sobre, text="1", bg='#fff', font=('poppins', 14, 'bold'),
                                        anchor="w")
            self.label_mundo_valor.place(relx=0.4, rely=0.41, relwidth=0.15, relheight=0.05)
            
# Turma --------------------------------------------------------------------------

            self.label_turma = tk.Label(self.frame_sobre, text="Turma:", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_turma.place(relx=0.2, rely=0.47, relwidth=0.15, relheight=0.05)
            self.label_turma_valor = tk.Label(self.frame_sobre, text="9001", bg='#fff', font=('poppins', 14, 'bold'),
                                        anchor="w")
            self.label_turma_valor.place(relx=0.4, rely=0.47, relwidth=0.15, relheight=0.05)

            
# Semestre ----------------------------------------------------------------------

            self.label_semestre = tk.Label(self.frame_sobre, text="Semestre:", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_semestre.place(relx=0.2, rely=0.53, relwidth=0.15, relheight=0.05)
            self.label_semestre_valor = tk.Label(self.frame_sobre, text="1º", bg='#fff', font=('poppins', 14, 'bold'),
                                           anchor="w")
            self.label_semestre_valor.place(relx=0.4, rely=0.53, relwidth=0.15, relheight=0.05)
            
# Grupo ---------------------------------------------------------------------------

            self.label_grupo = tk.Label(self.frame_sobre, text="Grupo:", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_grupo.place(relx=0.2, rely=0.59, relwidth=0.15, relheight=0.05)
            self.label_grupo_valor = tk.Label(self.frame_sobre, text="DevTeam13", bg='#fff', font=('poppins', 14, 'bold'),
                                        anchor="w")
            self.label_grupo_valor.place(relx=0.4, rely=0.59, relwidth=0.15, relheight=0.05)
            
# Integrantes --------------------------------------------------------------------

            self.label_integ = tk.Label(self.frame_sobre, text="Integrantes:", bg='#fff', font=('poppins', 14, 'bold'), anchor="w")
            self.label_integ.place(relx=0.2, rely=0.65, relwidth=0.15, relheight=0.05)
            self.label_integ_1 = tk.Label(self.frame_sobre, text="Daniel Portella de Souza Nepomuceno - 202205063186", bg='#fff', font=('poppins', 14, 'bold'),
                                        anchor="w")
            self.label_integ_1 .place(relx=0.4, rely=0.65, relwidth=0.6, relheight=0.05)
            self.label_integ_2 = tk.Label(self.frame_sobre, text="Francisco Ferreira de Queiroz Neto - 202205164951",
                                          bg='#fff', font=('poppins', 14, 'bold'),
                                          anchor="w")
            self.label_integ_2.place(relx=0.4, rely=0.7, relwidth=0.5, relheight=0.05)
            self.label_integ_3 = tk.Label(self.frame_sobre, text="Maiara Accacio Machado - 202204268183",
                                          bg='#fff', font=('poppins', 14, 'bold'),
                                          anchor="w")
            self.label_integ_3.place(relx=0.4, rely=0.75, relwidth=0.5, relheight=0.05)
            self.label_integ_4 = tk.Label(self.frame_sobre, text="Rafael Leal Altero - 202205021882",
                                          bg='#fff', font=('poppins', 14, 'bold'),
                                          anchor="w")
            self.label_integ_4.place(relx=0.4, rely=0.8, relwidth=0.5, relheight=0.05)

            
            

# Botão encerrar -----------------------------------------------------------------
           
            self.bt_fechar = tk.Button(self.sobre, text="Encerrar", bd=5, command=self.sobre.destroy)
            self.bt_fechar.place(relx=0.40, rely=0.93, relwidth=0.20, relheight=0.05)

           
