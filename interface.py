from tkinter import *
from tkinter import messagebox
from geradorQrcode import Qrcode
import customtkinter

class Application:
    def __init__(self, janela=None):

        # Configuração de uma célula extra no início e no final da coluna para centralizar os elementos
        janela.grid_columnconfigure(0, weight=1)
        janela.grid_rowconfigure(0, weight=1)
        janela.grid_rowconfigure(5, weight=1)

        self.titulo = customtkinter.CTkLabel(janela, text='Bem-Vindo')
        self.titulo.grid(row=1, column=0, pady=(20, 0)) 

        self.link = customtkinter.CTkEntry(janela, placeholder_text='Digite o link')
        self.link.grid(row=2, column=0, pady=10)

        self.nome = customtkinter.CTkEntry(janela, placeholder_text='Nome do arquivo')
        self.nome.grid(row=3, column=0, pady=10)

        # Adicionando uma subframe para conter as CheckBoxes
        checkbox_frame = Frame(janela,bg=janela.cget('bg'))
        checkbox_frame.grid(row=5, column=0, pady=10)

        self.png = customtkinter.CTkCheckBox(checkbox_frame,text='PNG')
        self.png.grid(row=0, column=0)

        self.svg = customtkinter.CTkCheckBox(checkbox_frame, text='SVG')
        self.svg.grid(row=0, column=1)

        self.buttonGerar = customtkinter.CTkButton(janela, text='Gerar', command=self.gerarQrcode)
        self.buttonGerar.grid(row=6, column=0, pady=(10, 20))  

        self.gerador = Qrcode()

    def gerarQrcode(self):
        self.links = self.link.get()
        if self.links:
            self.nome_arquivo = self.nome.get()
            if self.nome_arquivo:
                if self.png.get() == 1 and self.svg.get()!=1:
                    qrcode = self.gerador.salvarPng(self.links, f'{self.nome_arquivo}.png')
                    messagebox.showinfo('Sucesso', 'QrCode gerado!')
                elif self.svg.get()==1 and self.png.get() != 1:
                    qrcode = self.gerador.salvarSVG(self.links,f'{self.nome_arquivo}.svg')
                    messagebox.showinfo('Sucesso', 'QrCode gerado!')
                else:
                    qrcode1 = self.gerador.salvarPng(self.links, f'{self.nome_arquivo}.png')
                    qrcode2 = self.gerador.salvarSVG(self.links, f'{self.nome_arquivo}.svg')
                    messagebox.showinfo('Sucesso', 'QrCode gerado!')
            else:
                messagebox.showwarning('Erro', 'Digite o nome do arquivo')
        else:
            messagebox.showwarning('Erro', 'Digite o link')


root = customtkinter.CTk()
root.title('Gerador de QrCode')
root.geometry('500x300')
Application(root)
root.mainloop()
