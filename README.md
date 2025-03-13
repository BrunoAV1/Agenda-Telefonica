# Agenda de Contatos - Python

## 🚀 Visão Geral

A **Agenda de Contatos** é uma aplicação simples e funcional desenvolvida em **Python**, com interface gráfica utilizando a biblioteca **Tkinter**. O projeto tem como objetivo fornecer uma plataforma para o gerenciamento de contatos pessoais, com a capacidade de adicionar, editar, excluir e buscar contatos, tudo isso com validações automáticas para garantir a qualidade e integridade dos dados inseridos.

Foi desenvolvido com foco em aprendizado, experimentação e prática das melhores práticas de programação, manipulação de arquivos e desenvolvimento de interfaces gráficas.

---

## 🛠 Tecnologias Utilizadas

### **Python 3.13.2**
A linguagem principal do projeto. O Python é uma linguagem de alto nível, amplamente utilizada por sua sintaxe simples e fácil de entender, além de sua grande comunidade de desenvolvedores.

### **Tkinter**
- **Tkinter** é a biblioteca padrão de Python para criar interfaces gráficas. Foi utilizada para desenvolver a interface da agenda de contatos de forma prática e acessível.
- Com Tkinter, foi possível criar janelas, botões, campos de texto e outros componentes gráficos de forma rápida e funcional.

### **JSON**
- **JSON (JavaScript Object Notation)** foi escolhido como formato para armazenamento dos dados da agenda. A utilização do JSON permite salvar os contatos de forma simples e legível, além de ser fácil de manipular.
- Ao salvar os dados em formato JSON, garantimos que a agenda é persistente e os contatos não se perdem ao fechar o programa.

### **phonenumbers**
- Biblioteca para validar e formatar números de telefone de acordo com padrões internacionais.
- Usada para garantir que os números inseridos pelos usuários sigam um formato correto e utilizável, sem erros de digitação ou formatação.

### **re (Expressões Regulares)**
- **re** é uma biblioteca do Python que permite trabalhar com expressões regulares, ideal para validar o formato do e-mail de maneira precisa.
- Com ela, foi possível implementar uma validação robusta para os endereços de e-mail inseridos pelos usuários.

---

## 📋 Funcionalidades Implementadas

- **Adicionar Contato**
  - Permite que o usuário adicione um novo contato à agenda.
  - Campos obrigatórios: nome, telefone e e-mail.
  - Validação do telefone e e-mail para garantir que os dados inseridos sejam válidos.
  
- **Editar Contato**
  - O usuário pode alterar os dados de um contato já existente.
  - A edição é feita de maneira simples e intuitiva, permitindo ao usuário alterar qualquer um dos campos (nome, telefone e e-mail).
  - PS: Ao editar o número, retire os carácters especiais, coloque apenas os números partindo do DD+9+restante do número. Uma possivel melhoria nesse campo virá.

- **Excluir Contato**
  - Oferece a funcionalidade de excluir um contato da lista, removendo permanentemente o contato da agenda.

- **Buscar Contato**
  - Possibilita a busca de contatos por nome. Ao digitar o nome de um contato, a lista de contatos exibirá apenas aqueles que correspondem ao critério de pesquisa.


- **Exibição de Contatos**
  - Exibe a lista completa de contatos armazenados, mostrando os campos de nome, telefone e e-mail em uma tabela simples e limpa.

- **Validação de Dados**
  - O projeto inclui validações automáticas para os campos de telefone e e-mail:
    - **Telefone**: Verificação de formato utilizando a biblioteca `phonenumbers`.
    - **E-mail**: Verificação do formato do e-mail com expressões regulares, garantindo que os dados inseridos estejam corretos.

---

## 💡 Como Rodar o Projeto

### Pré-requisitos
- **Python 3.13.2**: Este projeto foi desenvolvido utilizando o Python 3. Verifique se você tem o Python instalado em sua máquina. Se não, você pode baixar [aqui](https://www.python.org/downloads/).

### Passos para Executar

1. **Clone o repositório** para o seu computador:
   ```bash
   git clone https://github.com/BrunoAV1/Agenda-de-Contatos.git

2. **Instale** as dependências necessárias (bibliotecas externas):
    * A biblioteca phonenumbers é necessária para a validação dos números de telefone. Instale-a utilizando o **pip**:
     ```bash
    pip install phonenumbers

3. **Execute o arquivo** agenda.py para iniciar a aplicação:
    ```bash
    python agenda.py

---

## 📈 Estrutura do Projeto
#### O projeto possui a seguinte estrutura de arquivos:

```
agenda-contatos/
│
├── agenda.py            # Arquivo principal da aplicação
├── contatos.json        # Arquivo JSON onde os dados da agenda são armazenados
└── README.md            # Este arquivo
``` 

**agenda.py**: Arquivo que contém toda a lógica do programa e a interface gráfica com Tkinter.

**contatos.json**: Arquivo que armazena os contatos adicionados na agenda em formato JSON.

**README.md**: Este arquivo, que fornece informações sobre o projeto, como executá-lo, tecnologias utilizadas e contribuições.

---

## 🤝 Contribuições
Este projeto foi criado com fins educacionais e de aprendizado. O objetivo principal foi praticar conceitos fundamentais de programação e explorar as bibliotecas e ferramentas utilizadas. Embora o projeto esteja funcional, ele pode ser significativamente melhorado e expandido com novas funcionalidades.

Se você deseja contribuir, sinta-se à vontade para fazer um fork deste repositório e realizar as melhorias que desejar. Algumas ideias de melhorias incluem:

Implementar a funcionalidade de pesquisa por telefone ou e-mail.<br>
Adicionar funcionalidades extras, como importar/exportar contatos para diferentes formatos (CSV, vCard, etc.).<br>
Melhorar a interface gráfica para torná-la mais moderna e interativa.

---

## 🧑‍💻 Desenvolvedor
### Bruno Araujo de Vasconcellos
  Este projeto foi desenvolvido por um estudante de Análise e Desenvolvimento de Sistemas (ADS), com foco em aprender e explorar tecnologias de programação. Como estudante de tecnologia, o objetivo é construir projetos que sirvam de aprendizado, sem a preocupação com perfeição.
