import json
import os

# Nome do arquivo onde os contatos ficarão armazenados:
FILE_NAME = "contatos.json"

# Função para carregar os contatos do arquivo "contatos.json"
def carregar_contatos():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Função para salvar os contatos em "arquivos.json"
def salvar_contatos(contatos):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contatos, file, indent=4, ensure_ascii=False)

# Função para adicionar um contato
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)
    print("Contato adicionado com sucesso!\n")

# Função para listar todos os contatos
def listar_contatos():
    contatos = carregar_contatos()
    if not contatos:
        print("Nenhum contato salvo.\n")
        return
    
    for i, contato in enumerate(contatos, start=1):
        print(f"{i}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
    print()

# Função para buscar um contato por nome
def buscar_contato():
    nome_busca = input("Digite o nome do contato: ").lower()
    contatos = carregar_contatos()
    
    resultados = [c for c in contatos if nome_busca in c['nome'].lower()]
    if resultados:
        for contato in resultados:
            print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
    else:
        print("Contato não encontrado.\n")

# Função para excluir um contato
def excluir_contato():
    nome_excluir = input("Digite o nome do contato que deseja excluir: ").lower()
    contatos = carregar_contatos()
    
    contatos_filtrados = [c for c in contatos if nome_excluir not in c['nome'].lower()]
    
    if len(contatos) == len(contatos_filtrados):
        print("Contato não encontrado.\n")
    else:
        salvar_contatos(contatos_filtrados)
        print("Contato excluído com sucesso!\n")

# Função principal (menu)
def menu():
    while True:
        print("=== Agenda Telefônica ===")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Excluir contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            print("Saindo...\n")
            break
        else:
            print("Opção inválida!\n")

# Executar o menu
menu()
