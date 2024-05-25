import tkinter as tk
from tkinter import messagebox

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def verificar_aprovacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"

def adicionar_nota():
    try:
        nota = float(entry_nota.get())
        notas.append(nota)
        listbox_notas.insert(tk.END, f"{nota:.2f}")
        entry_nota.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def calcular_resultado():
    if not notas:
        messagebox.showwarning("Aviso", "Nenhuma nota foi inserida.")
        return

    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)
    label_resultado.config(text=f"Média: {media:.2f}\nSituação: {situacao}")

# Inicializa a lista de notas
notas = []

# Configuração da janela principal
root = tk.Tk()
root.title("Cálculo de Média dos Alunos")

# Frame para entrada de notas
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

label_nota = tk.Label(frame_entrada, text="Digite a nota do aluno:")
label_nota.pack(side=tk.LEFT)

entry_nota = tk.Entry(frame_entrada)
entry_nota.pack(side=tk.LEFT, padx=5)

button_adicionar = tk.Button(frame_entrada, text="Adicionar Nota", command=adicionar_nota)
button_adicionar.pack(side=tk.LEFT)

# Listbox para exibir as notas
listbox_notas = tk.Listbox(root)
listbox_notas.pack(pady=10)

# Botão para calcular a média
button_calcular = tk.Button(root, text="Calcular Média", command=calcular_resultado)
button_calcular.pack(pady=5)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Inicia a aplicação Tkinter
root.mainloop()