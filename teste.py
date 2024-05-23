import tkinter as tk
from PIL import Image, ImageTk

# Cria a janela principal
root = tk.Tk()

# Carrega a imagem usando Pillow
image = Image.open("TelaLoginArvore.png")

# Converte a imagem para um objeto PhotoImage
photo = ImageTk.PhotoImage(image)

# Cria um label e adiciona a imagem a ele
label = tk.Label(root, image=photo)
label.image = photo  # Mantém uma referência da imagem para evitar que seja coletada pelo garbage collector
label.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()