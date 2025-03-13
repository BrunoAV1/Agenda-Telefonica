import json
import os
import tkinter as tk
from tkinter import messagebox

# Nome do arquivo JSON
FILE_NAME = "contatos.json"

def carregar_contatos():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def salvar_contatos(contatos):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contatos, file, indent=4, ensure_ascii=False)

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    
    if nome and telefone:
        contatos = carregar_contatos()
        contatos.append({"nome": nome, "telefone": telefone, "email": email})
        salvar_contatos(contatos)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Nome e telefone são obrigatórios!")

def listar_contatos():
    contatos = carregar_contatos()
    lista.delete(0, tk.END)
    for contato in contatos:
        lista.insert(tk.END, f"{contato['nome']} - {contato['telefone']} - {contato['email']}")

def buscar_contato():
    nome_busca = entry_busca.get()
    contatos = carregar_contatos()
    lista.delete(0, tk.END)
    resultados = [c for c in contatos if nome_busca.lower() in c['nome'].lower()]
    
    if resultados:
        for contato in resultados:
            lista.insert(tk.END, f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
    else:
        messagebox.showinfo("Resultado", "Contato não encontrado.")

def excluir_contato():
    nome_excluir = entry_busca.get()
    contatos = carregar_contatos()
    contatos_filtrados = [c for c in contatos if nome_excluir.lower() not in c['nome'].lower()]
    
    if len(contatos) == len(contatos_filtrados):
        messagebox.showwarning("Erro", "Contato não encontrado.")
    else:
        salvar_contatos(contatos_filtrados)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Contato excluído com sucesso!")

def atualizar_lista():
    listar_contatos()

# Criar janela principal
janela = tk.Tk()
janela.title("Agenda Telefônica")
janela.geometry("450x550")
janela.configure(bg="#f0f0f0")

# Campos de entrada
frame_top = tk.Frame(janela, bg="#f0f0f0")
frame_top.pack(pady=10)

tk.Label(frame_top, text="Nome:", bg="#f0f0f0").grid(row=0, column=0)
entry_nome = tk.Entry(frame_top, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_top, text="Telefone:", bg="#f0f0f0").grid(row=1, column=0)
entry_telefone = tk.Entry(frame_top, width=30)
entry_telefone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_top, text="E-mail:", bg="#f0f0f0").grid(row=2, column=0)
entry_email = tk.Entry(frame_top, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

btn_add = tk.Button(janela, text="Adicionar Contato", command=adicionar_contato, bg="#4CAF50", fg="white")
btn_add.pack(pady=5)

# Lista de contatos
lista = tk.Listbox(janela, width=50, height=10)
lista.pack(pady=10)

# Campo de busca e botões
frame_bottom = tk.Frame(janela, bg="#f0f0f0")
frame_bottom.pack(pady=10)

tk.Label(frame_bottom, text="Buscar/Excluir:", bg="#f0f0f0").grid(row=0, column=0)
entry_busca = tk.Entry(frame_bottom, width=30)
entry_busca.grid(row=0, column=1, padx=5, pady=5)

btn_search = tk.Button(frame_bottom, text="Buscar", command=buscar_contato, bg="#2196F3", fg="white")
btn_search.grid(row=0, column=2, padx=5)

btn_delete = tk.Button(frame_bottom, text="Excluir", command=excluir_contato, bg="#f44336", fg="white")
btn_delete.grid(row=0, column=3, padx=5)

# Carregar contatos ao iniciar
atualizar_lista()

# Iniciar a interface
tk.mainloop()
