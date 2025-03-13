import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

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
    nome = simpledialog.askstring("Adicionar Contato", "Nome:")
    telefone = simpledialog.askstring("Adicionar Contato", "Telefone:")
    email = simpledialog.askstring("Adicionar Contato", "E-mail:")
    
    if nome and telefone:
        contatos = carregar_contatos()
        contatos.append({"nome": nome, "telefone": telefone, "email": email})
        salvar_contatos(contatos)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Nome e telefone são obrigatórios!")

def listar_contatos():
    contatos = carregar_contatos()
    lista.delete(0, tk.END)
    for contato in contatos:
        lista.insert(tk.END, f"{contato['nome']} - {contato['telefone']} - {contato['email']}")

def buscar_contato():
    nome_busca = simpledialog.askstring("Buscar Contato", "Digite o nome do contato:")
    contatos = carregar_contatos()
    lista.delete(0, tk.END)
    resultados = [c for c in contatos if nome_busca.lower() in c['nome'].lower()]
    
    if resultados:
        for contato in resultados:
            lista.insert(tk.END, f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
    else:
        messagebox.showinfo("Resultado", "Contato não encontrado.")

def excluir_contato():
    nome_excluir = simpledialog.askstring("Excluir Contato", "Digite o nome do contato que deseja excluir:")
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
janela.geometry("400x500")

# Lista de contatos
lista = tk.Listbox(janela, width=50, height=15)
lista.pack(pady=10)

# Botões
btn_add = tk.Button(janela, text="Adicionar Contato", command=adicionar_contato)
btn_add.pack(pady=5)

btn_list = tk.Button(janela, text="Listar Contatos", command=listar_contatos)
btn_list.pack(pady=5)

btn_search = tk.Button(janela, text="Buscar Contato", command=buscar_contato)
btn_search.pack(pady=5)

btn_delete = tk.Button(janela, text="Excluir Contato", command=excluir_contato)
btn_delete.pack(pady=5)

# Carregar contatos ao iniciar
atualizar_lista()

# Iniciar a interface
tk.mainloop()
