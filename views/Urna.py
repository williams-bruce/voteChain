import tkinter as tk

urna = tk.Tk()

urna.title('Votação segura com BlockChain!')

# Posicionando a Tela no centro
window_width = 980
window_heigth = 600
screen_width = urna.winfo_screenwidth()
screen_height = urna.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_heigth/2)
urna.geometry(f'{window_width}x{window_heigth}+{center_x}+{center_y}')
# Fim do posicionamento da Tela no centro
image_bg = tk.PhotoImage(file=r'D:\Documentos\programacao\eng_comp\python\voteChain\views\images\urna-vista-cima.png')
label = tk.Label(urna, image=image_bg)
label.place(x=0, y=0)
urna.resizable(False, False)

urna.mainloop()