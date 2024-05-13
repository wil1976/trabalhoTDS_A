import os
import pandas as pd
from tkinter import *


def calcular_situacao(media):
    if media >= 7:
        return 'BOA!'
    elif media >= 5:
        return 'Razoável'
    else:
        return 'Ruim'


def salvar_dados():
    nome = nome_entry.get()
    notas = [float(nota) for nota in notas_entry.get().split(',')]
    media = sum(notas) / len(notas)
    situacao = calcular_situacao(media)
    novos_dados = pd.DataFrame([[nome, notas, media, situacao]], columns=['Nome', 'Notas', 'Média', 'Situação'])
    arquivo = 'C:/Users/Gustavo Oliveira/Desktop/trabalhoNelson1/alunos.xlsx'  #criar uma planilha excel para receber os dados
    if os.path.isfile(arquivo):
        dados_existentes = pd.read_excel(arquivo)
        dados = pd.concat([dados_existentes, novos_dados])
    else:
        dados = novos_dados

    dados.to_excel(arquivo, index=False)
    nome_entry.delete(0, 'end')
    notas_entry.delete(0, 'end')


root = Tk()

Label(root, text='Nome').grid(row=0)
Label(root, text='Notas (separadas por vírgulas)').grid(row=1)

nome_entry = Entry(root)
notas_entry = Entry(root)

nome_entry.grid(row=0, column=1)
notas_entry.grid(row=1, column=1)

Button(root, text='Salvar', command=salvar_dados).grid(row=2, column=1, pady=4)

root.mainloop()
