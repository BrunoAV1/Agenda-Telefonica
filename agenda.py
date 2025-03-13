import json
import os
import tkinter as tk
from tkinter import messagebox, ttk
import phonenumbers
from tkinter import font as tkfont
import re

# Nome do arquivo onde os contatos ficarão salvos:
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

def formatar_telefone(telefone):
    try:
        telefone_obj = phonenumbers.parse(telefone, "BR")
        if phonenumbers.is_valid_number(telefone_obj):
            return phonenumbers.format_number(telefone_obj, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            return telefone
    except phonenumbers.phonenumberutil.NumberParseException:
        return telefone

def validar_telefone(telefone):
    telefone = telefone.replace(" ", "").replace("-", "")
    if len(telefone) == 11 and telefone.isdigit() and telefone[2] == '9':
        return True
    return False

def validar_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        if email.endswith(('.com', '.br')):
            return True
    return False

def verificar_email():
    email = entry_email.get()
    if not validar_email(email):
        messagebox.showwarning("Erro", "E-mail inválido. Certifique-se de que possui '@' e termina com '.com' ou '.br'.")
        return

    contatos = carregar_contatos()
    if any(contato['email'] == email for contato in contatos):
        messagebox.showwarning("Erro", "Este e-mail já está cadastrado!")
        return

    entry_nome.config(state="normal")
    entry_telefone.config(state="normal")
    btn_add.config(state="normal")

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    
    if nome and telefone:
        if not validar_telefone(telefone):
            messagebox.showwarning("Erro", "O número de telefone deve conter 11 dígitos e começar com o número 9 após o DDD.")
            return

        contatos = carregar_contatos()

        if any(contato['telefone'] == telefone for contato in contatos):
            messagebox.showwarning("Erro", "Já existe um contato com este número de telefone!")
            return

        telefone_formatado = formatar_telefone(telefone)
        contatos.append({"nome": nome, "telefone": telefone_formatado, "email": email})
        salvar_contatos(contatos)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_nome.config(state="disabled")
        entry_telefone.config(state="disabled")
        btn_add.config(state="disabled")
    else:
        messagebox.showwarning("Erro", "Nome e telefone são obrigatórios!")

def atualizar_lista():
    contatos = carregar_contatos()
    lista.delete(*lista.get_children())
    for contato in contatos:
        lista.insert("", tk.END, values=(contato['nome'], contato['telefone'], contato['email']))

# Criar janela principal
janela = tk.Tk()
janela.title("Agenda Telefônica")
janela.geometry("600x500")
janela.configure(bg="#e3f2fd")

font_padrao = tkfont.Font(family="Arial", size=10)

frame_campos = tk.Frame(janela, bg="#e3f2fd")
frame_campos.pack(pady=20)

tk.Label(frame_campos, text="E-mail:", bg="#e3f2fd", font=font_padrao).grid(row=0, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_campos, width=30, font=font_padrao)
entry_email.grid(row=0, column=1, padx=5, pady=5)
btn_verificar_email = tk.Button(frame_campos, text="Verificar Email", command=verificar_email, bg="#03A9F4", fg="white", font=font_padrao)
btn_verificar_email.grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame_campos, text="Nome:", bg="#e3f2fd", font=font_padrao).grid(row=1, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_campos, width=30, font=font_padrao, state="disabled")
entry_nome.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_campos, text="Telefone:", bg="#e3f2fd", font=font_padrao).grid(row=2, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_campos, width=30, font=font_padrao, state="disabled")
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

btn_add = tk.Button(frame_campos, text="Adicionar Contato", command=adicionar_contato, bg="#4CAF50", fg="white", font=font_padrao, state="disabled")
btn_add.grid(row=3, columnspan=2, pady=10)

frame_lista = tk.Frame(janela)
frame_lista.pack(pady=10, padx=10, fill='both', expand=True)

colunas = ("Nome", "Telefone", "E-mail")
lista = ttk.Treeview(frame_lista, columns=colunas, show="headings", height=8)
for col in colunas:
    lista.heading(col, text=col)
    lista.column(col, width=150)
lista.pack(fill='both', expand=True)

scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista.yview)
lista.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

atualizar_lista()
janela.mainloop()
