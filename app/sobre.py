import tkinter as tk
from app.tecnico import TK

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

            self.frame_sobre = tk.Frame(self.sobre, bd=4, bg='#fff',
                                         highlightbackground='#B9B7BD',
                                         highlightthickness=2)
            self.frame_sobre.place(relx=0.05, rely=0, relwidth=0.91, relheight=0.3)

            self.logo_estacio = tk.PhotoImage(file='../ico/logo1.png')
            self.label_logo = tk.Label(self.frame_sobre, image=self.logo_estacio)
            self.label_logo.place(relx=0.3, rely=0.1, relwidth=0.385, relheight=0.35)
            
            # label_estacio = tk.Label(frame_sobre, text="Universidade Estácio de Sá", bg='#fff', font=('poppins', 25, 'bold'))
            # logo.estacio = tk.PhotoImage(file='../ico/worker.png')
            # label_tec_Img = tk.Label(self.frame_tecnico, image=self.img_tec)
            # label_tec.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.2)
            # label_tec_Img.place(relx=0.29, rely=0.05, relwidth=0.4, relheight=0.4)



            self.bt_fechar = tk.Button(self.sobre, text="Encerrar", bd=5, command=self.sobre.destroy)
            self.bt_fechar.place(relx=0.40, rely=0.93, relwidth=0.20, relheight=0.05)

            

           

        
