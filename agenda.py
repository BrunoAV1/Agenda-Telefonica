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
    """Formata o número de telefone no formato brasileiro."""
    try:
        telefone_obj = phonenumbers.parse(telefone, "BR")
        if phonenumbers.is_valid_number(telefone_obj):
            return phonenumbers.format_number(telefone_obj, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            return telefone
    except phonenumbers.phonenumberutil.NumberParseException:
        return telefone

def validar_telefone(telefone):
    """Verifica se o número de telefone possui 11 dígitos e começa com o número 9 após o DDD."""
    telefone = telefone.replace(" ", "").replace("-", "")
    if len(telefone) == 11 and telefone.isdigit() and telefone[2] == '9':
        return True
    return False

def validar_email(email):
    """Verifica se o e-mail é válido (contém '@' e termina com '.com' ou '.br')."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zAZ0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        if email.endswith(('.com', '.br')):
            return True
    return False

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    
    if nome and telefone:
        if not validar_telefone(telefone):
            messagebox.showwarning("Erro", "O número de telefone deve conter 11 dígitos e começar com o número 9 após o DDD.")
            return

        if not validar_email(email):
            messagebox.showwarning("Erro", "E-mail inválido. Certifique-se de que possui '@' e termina com '.com' ou '.br'.")
            return

        contatos = carregar_contatos()

        # Verificar se o número de telefone já existe
        if any(contato['telefone'] == telefone for contato in contatos):
            messagebox.showwarning("Erro", "Já existe um contato com este número de telefone!")
            return

        # Verificar se o nome já existe
        if any(contato['nome'].lower() == nome.lower() for contato in contatos):
            messagebox.showwarning("Erro", "Já existe um contato com este nome!")
            return

        telefone_formatado = formatar_telefone(telefone)
        contatos.append({"nome": nome, "telefone": telefone_formatado, "email": email})
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
    lista.delete(*lista.get_children())
    for contato in contatos:
        lista.insert("", tk.END, values=(contato['nome'], contato['telefone'], contato['email']))

def buscar_contato():
    nome_busca = entry_busca.get()
    contatos = carregar_contatos()
    lista.delete(*lista.get_children())
    resultados = [c for c in contatos if nome_busca.lower() in c['nome'].lower()]
    
    if resultados:
        for contato in resultados:
            item = lista.insert("", tk.END, values=(contato['nome'], contato['telefone'], contato['email']))
            if nome_busca.lower() in contato['nome'].lower():
                lista.item(item, tags='highlight')  
    else:
        messagebox.showinfo("Resultado", "Contato não encontrado.")

def excluir_contato():
    selected_item = lista.selection()
    if not selected_item:
        messagebox.showwarning("Erro", "Selecione um contato para excluir.")
        return
    
    nome_excluir = lista.item(selected_item, 'values')[0]  # Obter o nome do contato
    contatos = carregar_contatos()
    contatos_filtrados = [c for c in contatos if c['nome'] != nome_excluir]
    
    if len(contatos) == len(contatos_filtrados):
        messagebox.showwarning("Erro", "Contato não encontrado.")
    else:
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este contato?"):
            salvar_contatos(contatos_filtrados)
            atualizar_lista()
            messagebox.showinfo("Sucesso", "Contato excluído com sucesso!")

def editar_contato():
    selected_item = lista.selection()
    if not selected_item:
        messagebox.showwarning("Erro", "Selecione um contato para editar.")
        return
    
    nome_editar = lista.item(selected_item, 'values')[0]  # Obter o nome do contato
    contatos = carregar_contatos()
    for contato in contatos:
        if nome_editar.lower() == contato['nome'].lower():
            # Preencher os campos com os dados do contato selecionado
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, contato['nome'])
            entry_telefone.delete(0, tk.END)
            entry_telefone.insert(0, contato['telefone'])
            entry_email.delete(0, tk.END)
            entry_email.insert(0, contato['email'])

            
            def confirmar_edicao():
                novo_nome = entry_nome.get()
                novo_telefone = entry_telefone.get()
                novo_email = entry_email.get()

                if novo_telefone and not validar_telefone(novo_telefone):
                    messagebox.showwarning("Erro", "O número de telefone deve conter 11 dígitos e começar com 9 (padrão novo do Brasil).")
                    return

                if novo_email and not validar_email(novo_email):
                    messagebox.showwarning("Erro", "E-mail inválido. Certifique-se de que possui '@' e termina com '.com' ou '.br'.")
                    return

                # Atualizar o contato na lista
                contato['nome'] = novo_nome
                contato['telefone'] = formatar_telefone(novo_telefone) if novo_telefone else contato['telefone']
                contato['email'] = novo_email if novo_email else contato['email']
                salvar_contatos(contatos)
                atualizar_lista()
                messagebox.showinfo("Sucesso", "Contato editado com sucesso!")
                entry_nome.delete(0, tk.END)
                entry_telefone.delete(0, tk.END)
                entry_email.delete(0, tk.END)
                btn_add.config(text="Adicionar Contato", command=adicionar_contato)  # Resetar o botão para "Adicionar"

            btn_add.config(text="Salvar Alterações", command=confirmar_edicao)
            break

def atualizar_lista():
    listar_contatos()

# Criar janela principal
janela = tk.Tk()
janela.title("Agenda Telefônica")
janela.geometry("600x500")  # Ajuste do tamanho da janela
janela.configure(bg="#e3f2fd")

# Definir fonte para o texto
font_padrao = tkfont.Font(family="Arial", size=10)

# Criar frames para centralizar os campos
frame_top = tk.Frame(janela, bg="#e3f2fd")
frame_top.pack(pady=10, padx=10, fill='x')

frame_mid = tk.Frame(janela, bg="#e3f2fd")
frame_mid.pack(pady=20, padx=10, fill='x')

frame_bottom = tk.Frame(janela, bg="#e3f2fd")
frame_bottom.pack(pady=20, padx=10, fill='x')

# Campo de busca e botão
frame_busca = tk.Frame(frame_top, bg="#e3f2fd")
frame_busca.pack(pady=10, padx=10, fill='x')

entry_busca = tk.Entry(frame_busca, width=30, font=font_padrao)
entry_busca.grid(row=0, column=0, padx=5, pady=5)

btn_buscar = tk.Button(frame_busca, text="Buscar", command=buscar_contato, bg="#03A9F4", fg="white", font=font_padrao)
btn_buscar.grid(row=0, column=1, padx=5, pady=5)

# Campos de entrada (nome, telefone, e-mail)
frame_campos = tk.Frame(frame_mid, bg="#e3f2fd")
frame_campos.pack(pady=20)

tk.Label(frame_campos, text="Nome:", bg="#e3f2fd", font=font_padrao).grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_campos, width=30, font=font_padrao)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_campos, text="Telefone:", bg="#e3f2fd", font=font_padrao).grid(row=1, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_campos, width=30, font=font_padrao)
entry_telefone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_campos, text="E-mail:", bg="#e3f2fd", font=font_padrao).grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_campos, width=30, font=font_padrao)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Botão para Adicionar ou Editar dentro do frame_campos
btn_add = tk.Button(frame_campos, text="Adicionar Contato", command=adicionar_contato, bg="#4CAF50", fg="white", font=font_padrao)
btn_add.grid(row=3, columnspan=2, pady=10)

# Lista de contatos
frame_lista = tk.Frame(janela)
frame_lista.pack(pady=10, padx=10, fill='both', expand=True)

colunas = ("Nome", "Telefone", "E-mail")
lista = ttk.Treeview(frame_lista, columns=colunas, show="headings", height=8)
for col in colunas:
    lista.heading(col, text=col)
    lista.column(col, width=150)
lista.pack(fill='both', expand=True)

# Barra de rolagem
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista.yview)
lista.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Botões Excluir e Editar
btn_excluir = tk.Button(frame_bottom, text="Excluir", command=excluir_contato, bg="#F44336", fg="white", font=font_padrao)
btn_editar = tk.Button(frame_bottom, text="Editar", command=editar_contato, bg="#FFC107", fg="white", font=font_padrao)

btn_excluir.pack(side="left", padx=10, pady=5)
btn_editar.pack(side="left", padx=10, pady=5)

# Atualizar lista de contatos ao iniciar
atualizar_lista()

# Rodar o aplicativo
janela.mainloop()
