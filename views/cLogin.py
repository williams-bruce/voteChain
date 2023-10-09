import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from PIL import ImageTk, Image

'''Classe que representa um objeto do tipo view Login'''
class Login(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # self.init_components()
        
    
        self.title('Votação segura com BlockChain!')

        # Posicionando a Tela no centro
        window_width = 500
        window_heigth = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_heigth/2)
        self.geometry(f'{window_width}x{window_heigth}+{center_x}+{center_y}')

        # Setando imagem de background
        image_bg = tk.PhotoImage(file=r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\ricardo-franco.png')
        label_image_bg = tk.Label(self, image=image_bg)
        label_image_bg.place(x=-2, y=0)

        # Setando imagem logo grifo
        logo_grifo = ImageTk.PhotoImage(Image.open(r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\grifo-logo-login.png'))
        label_logo_grifo = tk.Label(self, image=logo_grifo)
        label_logo_grifo.place(x=160, y=30)

        # Criando label do código do aluno
        label_codigo_aluno = tk.Label(self, text='Código do aluno', font=('Helvetica', 22))
        label_codigo_aluno.place(x=160, y=300)

        # Criando input text
        input_code = ttk.Entry(self, font=('Helvetica', 24), justify='center', width=10)
        input_code.place(x=170, y=400)

        # Criando botão submit
        btn_font = font.Font(family='Helvetica', size=20, weight='bold')
        submit_button = tk.Button(self, text='Submit', width=10, bg='blue', fg='white')
        submit_button['font'] = btn_font
        submit_button.place(x=160, y=500)

        self.resizable(False, False)
    

if __name__ == '__main__':
    login = Login()
    login.mainloop()
