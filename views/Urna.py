import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image


class UrnaController():
    def __init__(self, view):
        self.view = view



class Urna(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # self.controller = UrnaController(self)
        self.title('Votação segura com BlockChain!')

        ############ CRIANDO A WINDOW ############
        window_width = 980
        window_heigth = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_heigth/2)
        self.geometry(f'{window_width}x{window_heigth}+{center_x}+{center_y}')
        self.resizable(False, False)

        # Setando imagem do background
        self.image_bg = tk.PhotoImage(file=r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\urna-vista-cima.png')
        self.label = tk.Label(self, image=self.image_bg)
        self.label.place(x=0, y=0)

        # Criando os botões
        self.btn_confirmar = tk.Button(self, border=0, width=8, height=2, text='confirmar', )
        self.btn_confirmar.place(x=810, y=475)

        ############ FIM DA CRIAÇÃO DA WINDOW ############

        ############ CRIANDO FRAME INCIAL ############
        # frame_voto = tk.Frame(self, bd=5, width=510, height=297, background="grey")
        # frame_voto.place(x=84, y=215)

        # Criando Label de texto presidente do grifo
        # font_presidente = font.Font(family='Helvetica', size=24)
        # label_presidente = tk.Label(frame_voto, text="PRESIDENTE DO GRIFO", bg='grey')
        # label_presidente['font'] = font_presidente
        # label_presidente.place(x=70, y=25)

        # # Criando primeiro número a ser capturado
        # font_entry = font.Font(family='Helvetica', size=20)
        # entry_number1 = tk.Entry(frame_voto, border=1, width=2, justify='center', )
        # entry_number1['font'] = font_entry
        # entry_number1.place(x=208, y=80)

        # # Criando segundo número a ser capturado
        # entry_number2 = tk.Entry(frame_voto, border=1, width=2, justify='center')
        # entry_number2['font'] = font_entry
        # entry_number2.place(x=242, y=80)
        ############ FIM DO FRAME INICIAL ############

        ############ CRIANDO FRAME COM FOTO DO CANDIDATO ############
        # frame_candidato_foto = tk.Frame(self, bd=5, width=510, height=297, background="grey")
        # frame_candidato_foto.place(x=84, y=215)

        # # Criando Label de texto SEU VOTO PARA
        # font_seuVoto = font.Font(family='Helvetica', size=14)
        # label_seuVoto = tk.Label(frame_candidato_foto, text="Seu voto para:", bg='grey')
        # label_seuVoto['font'] = font_seuVoto
        # label_seuVoto.place(x=20, y=10)

        # # Criando Label de texto PRESIDENTE DO GRIFO
        # font_presidente_grifo = font.Font(family='Helvetica', size=18)
        # label_presidente_grifo = tk.Label(frame_candidato_foto, text="PRESIDENTE DO GRIFO", bg='grey')
        # label_presidente_grifo['font'] = font_presidente_grifo
        # label_presidente_grifo.place(x=50, y=50)

        # # Criando Label de texto NOME
        # font_nome = font.Font(family='Helvetica', size=12)
        # label_nome = tk.Label(frame_candidato_foto, text="Nome:", bg='grey')
        # label_nome['font'] = font_nome
        # label_nome.place(x=5, y=125)

        # # Criando Label de texto NÚMERO
        # font_numero = font.Font(family='Helvetica', size=12)
        # label_numero = tk.Label(frame_candidato_foto, text="Número:", bg='grey')
        # label_numero['font'] = font_numero
        # label_numero.place(x=5, y=150)

        # # Criando Label de texto PARTIDO
        # font_partido = font.Font(family='Helvetica', size=12)
        # label_partido = tk.Label(frame_candidato_foto, text="Partido:", bg='grey')
        # label_partido['font'] = font_partido
        # label_partido.place(x=5, y=175)

        # # Colocando Label da foto do candidato
        # foto_candidato = ImageTk.PhotoImage(Image.open(r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\candidatos\ivo_lin.jpg'))
        # label_foto_candidato = tk.Label(frame_candidato_foto, image=foto_candidato)
        # label_foto_candidato.place(x=354, y=4)

        # # Colocando SEPARATOR
        # separator = tk.Frame(frame_candidato_foto,bg="black", height=1, bd=0)
        # separator.place(x=2, y=200, width=500)

        # # Criando Label de texto APERTE A TECLA
        # font_aperte_tecla = font.Font(family='Helvetica', size=12)
        # label_aperte_tecla = tk.Label(frame_candidato_foto, text="APERTE A TECLA:", bg='grey')
        # label_aperte_tecla['font'] = font_aperte_tecla
        # label_aperte_tecla.place(x=5, y=215)

        # # Criando Label de texto VERDE PARA CONFIRMAR
        # font_confirmar = font.Font(family='Helvetica', size=12)
        # label_confirmar = tk.Label(frame_candidato_foto, text="VERDE para Confirmar", bg='grey')
        # label_confirmar['font'] = font_confirmar
        # label_confirmar.place(x=30, y=240)

        # # Criando Label de texto LARANJA PARA CORRIGIR
        # font_corrigir = font.Font(family='Helvetica', size=12)
        # label_corrigir = tk.Label(frame_candidato_foto, text="LARANJA para Corrigir", bg='grey')
        # label_corrigir['font'] = font_corrigir
        # label_corrigir.place(x=30, y=265)

        ############ FIM DO FRAME COM FOTO DO CANDIDATO ############

        ############ CRIANDO FRAME FIM ############
        # frame_fim = tk.Frame(self, bd=5, width=510, height=297, background="grey")
        # frame_fim.place(x=84, y=215)

        # # Criando Label de FIM
        # font_fim = font.Font(family='Helvetica', size=38)
        # label_fim = tk.Label(frame_fim, text='FIM', bg='grey')
        # label_fim['font'] = font_fim
        # label_fim.place(x=200, y=110)

        ############ FIM DO FRAME FIM ############

        ############ CRIANDO FRAME BRANCO ############
        self.frame_branco = tk.Frame(self, bd=5, width=510, height=297, background="grey")
        self.frame_branco.place(x=84, y=215)

        # Criando Label de texto SEU VOTO PARA
        self.font_seuVoto = font.Font(family='Helvetica', size=14)
        self.label_seuVoto = tk.Label(self.frame_branco, text="Seu voto para:", bg='grey')
        self.label_seuVoto['font'] = self.font_seuVoto
        self.label_seuVoto.place(x=20, y=10)

        # Criando Label de texto PRESIDENTE DO GRIFO
        self.font_presidenteGrifo = font.Font(family='Helvetica', size=18)
        self.label_presidente_grifo = tk.Label(self.frame_branco, text="PRESIDENTE DO GRIFO", bg='grey')
        self.label_presidente_grifo['font'] = self.font_presidenteGrifo
        self.label_presidente_grifo.place(x=50, y=50)

        # Criando Label de texto VOTO EM BRANCO
        self.font_voto_branco = font.Font(family='Helvetica', size=38)
        self.label_voto_brancco = tk.Label(self.frame_branco, text="VOTO EM BRANCO", bg='grey')
        self.label_voto_brancco['font'] = self.font_voto_branco
        self.label_voto_brancco.place(x=14, y=100)

        # Colocando SEPARATOR
        self.separator = tk.Frame(self.frame_branco,bg="black", height=1, bd=0)
        self.separator.place(x=2, y=200, width=500)

        # Criando Label de texto APERTE A TECLA
        self.font_aperte_tecla = font.Font(family='Helvetica', size=12)
        self.label_aperte_tecla = tk.Label(self.frame_branco, text="APERTE A TECLA:", bg='grey')
        self.label_aperte_tecla['font'] = self.font_aperte_tecla
        self.label_aperte_tecla.place(x=5, y=215)

        # Criando Label de texto VERDE PARA CONFIRMAR
        self.font_confirmar = font.Font(family='Helvetica', size=12)
        self.label_confirmar = tk.Label(self.frame_branco, text="VERDE para Confirmar", bg='grey')
        self.label_confirmar['font'] = self.font_confirmar
        self.label_confirmar.place(x=30, y=240)

        # Criando Label de texto LARANJA PARA CORRIGIR
        self.font_corrigir = font.Font(family='Helvetica', size=12)
        self.label_corrigir = tk.Label(self.frame_branco, text="LARANJA para Corrigir", bg='grey')
        self.label_corrigir['font'] = self.font_corrigir
        self.label_corrigir.place(x=30, y=265)

        ############ FIM DO FRAME BRANCO ############
        
        self.mainloop()
        


if __name__ == '__main__':
    app = Urna()
    



