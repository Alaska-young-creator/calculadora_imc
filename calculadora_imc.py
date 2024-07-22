'''
Calculadora de IMC com Interface Gráfica
Foco do projeto: Python
Nível do projeto: Iniciante
O que irá desenvolver?
Crie um programa em Python com uma interface gráfica que calcula o Índice de Massa
Corporal (IMC) de uma pessoa.
.
Funcionalidades que o projeto deve possuir:
1. Interface Gráfica:
○ Criar uma janela principal.
○ Adicionar campos de entrada para o peso (em kg) e altura (em metros(exemplo:
1.70, 1.80)
○ Adicionar um botão para calcular o IMC.
○ Adicionar um campo para exibir o resultado do IMC.
○ Adicionar um campo para exibir a categoria do IMC
i. Muito abaixo do peso
ii. Abaixo do peso
iii. Peso normal
iv. Acima do peso
v. Obesidade I
vi. Obesidade II
vii. Obesidade III
○ Personalize as cores da categoria para que tudo fique mais intuitivo(coloque
cores diferentes para cada nível
i. (ex:vá de branco para vermelho, de acordo com o nível de obesidade)
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura * altura)

        label_imc.config(text=f"IMC: {imc:.2f}")

        categoria = determinar_categoria(imc)
        label_categoria.config(text=f"Categoria: {categoria}", fg=cores[categoria])

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")

def determinar_categoria(imc):
    if imc < 18.5:
        return "Muito abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Acima do peso"
    elif 30 <= imc < 35:
        return "Obesidade I"
    elif 35 <= imc < 40:
        return "Obesidade II"
    else:
        return "Obesidade III"

# Cores para cada categoria
cores = {
    "Muito abaixo do peso": "white",
    "Peso normal": "green",
    "Acima do peso": "black",
    "Obesidade I": "orange",
    "Obesidade II": "red",
    "Obesidade III": "darkred"
}

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Cria os labels e campos de entrada
label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.grid(row=0, column=0)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1)

label_altura = tk.Label(janela, text="Altura (m):")
label_altura.grid(row=1, column=0)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1)

label_aviso_altura = tk.Label(janela, text="* Insira a altura em metros (ex: 1.70, 1.80)", fg="gray")
label_aviso_altura.grid(row=2, column=0, columnspan=2)

# Cria o botão de cálculo
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=3, column=0, columnspan=2)

# Cria os labels para exibir o resultado
label_imc = tk.Label(janela, text="")
label_imc.grid(row=4, column=0, columnspan=2)

label_categoria = tk.Label(janela, text="")
label_categoria.grid(row=5, column=0, columnspan=2)

janela.mainloop()