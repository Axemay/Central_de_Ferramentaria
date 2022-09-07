import openpyxl
import pandas as pd
import os
from datetime import date, time, datetime, timedelta
import pathlib
from tkinter import messagebox


hoje = datetime.now()
aa = str(hoje)
bb = aa.split(" ")
global cc
cc = bb[0]
dd = bb[1]
ee = dd.split(":")
h = ee[0]
m = ee[1]
global ff
ff = f"{h}-{m}"


def exportxlsT():
    

    arquivo = pd.read_csv("tecnico.csv")
    arquivo.to_excel("tecnico.xlsx", sheet_name="Testing", index=False)

    novo = f"tecnico{cc}-{ff}hs.xlsx"
    caminho = os.path.abspath(os.getcwd())
    print(caminho)
    cam = caminho.replace("\\","/")
    cam2 = f"{cam}/"

    os.rename("tecnico.xlsx", novo)
    
    file_source = cam2
    file_destination = 'c:/Users/Public/Downloads/'
    file_destination2 = '/home/'
    
    g = novo

    try:
        os.replace(file_source + g, file_destination2 + g)
    except:
        os.replace(file_source + g, file_destination + g)

    messagebox.showinfo(title="ARQUIVO GERADO COM SUCESSO!", message="Disponível em 'Downloads Públicos' no Windows\nou em 'home' no Linux")

def exportxlsF():
    

    arquivo = pd.read_csv("ferramenta.csv")
    arquivo.to_excel("ferramenta.xlsx", sheet_name="Testing", index=False)

    novo = f"ferramenta{cc}-{ff}hs.xlsx"
    caminho = os.path.abspath(os.getcwd())
    print(caminho)
    cam = caminho.replace("\\","/")
    cam2 = f"{cam}/"
    os.rename("ferramenta.xlsx", novo)
    
    file_source = cam2
    file_destination = 'c:/Users/Public/Downloads/'
    file_destination2 = '/home/'
    
    g = novo

    try:
        os.replace(file_source + g, file_destination2 + g)
    except:
        os.replace(file_source + g, file_destination + g)

    messagebox.showinfo(title="ARQUIVO GERADO COM SUCESSO!", message="Disponível em 'Downloads Públicos' no Windows\nou em 'home' no Linux")

def exportxlsR():
    

    arquivo = pd.read_csv("reserva.csv")
    arquivo.to_excel("reserva.xlsx", sheet_name="Testing", index=False)

    novo = f"reserva{cc}-{ff}hs.xlsx"
    caminho = os.path.abspath(os.getcwd())
    print(caminho)
    cam = caminho.replace("\\","/")
    cam2 = f"{cam}/"
    
    os.rename("reserva.xlsx", novo)
    
    file_source = cam2
    file_destination = 'c:/Users/Public/Downloads/'
    file_destination2 = '/home/'
    
    g = novo

    try:
        os.replace(file_source + g, file_destination2 + g)
    except:
        os.replace(file_source + g, file_destination + g)

    messagebox.showinfo(title="ARQUIVO GERADO COM SUCESSO!", message="Disponível em 'Downloads Públicos' no Windows\nou em 'home' no Linux")

        
