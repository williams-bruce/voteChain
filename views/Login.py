import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from PIL import ImageTk, Image
from models.ConnectDB import ConnectDB as db


class LoginController:
    def __init__(self, view)->None:
        self.view = view
    
    
    def btnSubimit(nao_sei, code):
        model = db()
        resultado = model.search('eleitores', codigo=code)
        if resultado:
            print(f'Fui pressionado: {resultado[0]}')
            showinfo('Autenticação de eleitores', f'Aluno {resultado[0][0]} autenticado!')
        else:
            showerror('Eleitor não encontrado', f'Eleitor não encontrado: {code}')



class Login(tk.Tk):
    '''Classe que representa um objeto do tipo view Login'''

    def __init__(self) -> None:
        super().__init__()
        self.controller = LoginController(self)
        self.title('Votação segura com BlockChain!')

        # Posicionando a Tela no centro
        window_width = 500
        window_heigth = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.center_x = int(screen_width/2 - window_width/2)
        self.center_y = int(screen_height/2 - window_heigth/2)
        self.geometry(f'{window_width}x{window_heigth}+{self.center_x}+{self.center_y}')

        # Setando imagem de background
        self.image_bg = tk.PhotoImage(file=r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\ricardo-franco.png')
        self.label_image_bg = tk.Label(self, image=self.image_bg)
        self.label_image_bg.place(x=-2, y=0)

        # Setando imagem logo grifo
        self.logo_grifo = ImageTk.PhotoImage(Image.open(r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\grifo-logo-login.png'))
        self.label_logo_grifo = tk.Label(self, image=self.logo_grifo)
        self.label_logo_grifo.place(x=160, y=30)

        # Criando label do código do aluno
        self.label_codigo_aluno = tk.Label(self, text='Código do aluno', font=('Helvetica', 22))
        self.label_codigo_aluno.place(x=160, y=300)

        # Criando input text
        self.text_code_aluno = tk.StringVar()
        self.input_code = ttk.Entry(self, font=('Helvetica', 24), justify='center', width=10, textvariable=self.text_code_aluno)
        self.input_code.place(x=170, y=400)
        self.input_code.focus()

        # Criando botão submit
        btn_font = font.Font(family='Helvetica', size=20, weight='bold')
        self.submit_button = tk.Button(self, text='Submit', width=10, bg='blue', fg='white', command=lambda: self.controller.btnSubimit(self.text_code_aluno.get()))
        self.submit_button['font'] = btn_font
        self.submit_button.place(x=160, y=500)

        self.resizable(False, False)
    


if __name__ == '__main__':
    login = Login()
    login.mainloop()
