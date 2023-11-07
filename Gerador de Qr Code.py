##GERADOR DE QR CODE##
import qrcode
from PIL import Image, ImageTk
import tkinter as tk

def gerando_qrcode():
    texto = entrada.get() #Obtem o texto do usuario
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=1) #com configurações específicas, como versão, correção de erros, tamanho da caixa e borda
    qr.add_data(texto) # adiciona o texto inserido pelo usuário ao objeto QRCode.
    qr.make(fit=True) # gera o QR Code com base nas configurações e no texto fornecido.
    qr_img = qr.make_image(fill_color="black", back_color="white") # é a imagem do QR Code gerada.
    img = ImageTk.PhotoImage(image=qr_img) # converte a imagem do QR Code em um formato compatível com o tkinter.
    imagem_qr_label.config(image=img) # configura o rótulo imagem_qr_label para exibir a imagem do QR Code.
    imagem_qr_label.img = img #garante que a imagem seja mantida em memória para evitar que ela seja destruída imediatamente

# titulo,icone,window
root = tk.Tk()
root.title("Gerador")
root.wm_iconbitmap(r"C:\Users\estor\OneDrive\Documentos\Projeto Qr Code\qrcode.ico") #colocação do icon
root.wm_resizable(0, 0) #tirar o botão de maximizar
# entrada de texto
entrada = tk.Entry(root)
entrada.pack(padx=50, pady=50)

# botão para gerar o QR Code
botao = tk.Button(root, text="Gerar QR Code", command=gerando_qrcode)
botao.pack(padx=10, pady=10)

# área para exibir o QR Code
imagem_qr_label = tk.Label(root)
imagem_qr_label.pack()

root.mainloop()