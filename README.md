# Projeto Calculadora Aritmética Avançada

Este projeto é uma calculadora aritmética avançada, que permite cálculos complexos, obedecendo os princípios da matemática. Tendo vista isso, foi utilizado o conceito de design pattern comportamental Visitor, no qual possibilitou a criação de uma árvore de sintaxe abstrata utilizando o módulo **ast** do *Python*, no qual possibilitou a leitura de expressões matemáticas.

Para esse projeto foi utilizada a framework *Django*, que possibilitou criar um aplicação *Full Stack*, que contempla **Front End** ( Templates ) e **Back End** ( Models e Views ). Foi desenvolvido e pensado com a intenção de atender todos os requisitos da atividade, de acordo com o protótipo. 

## Funcionalidades  
- Possui um redirecionador de página, caso seja acessado sem o caminho da URL;
- Possui um sistema de autenticação personalizado, utilizando **AbstractBaseUser**;
- Possui um *form* de cadastro para o usuário;
- Possui uma calculadora avançada com histórico;
- Possui integração direta com números e operadores do teclado;
- Possui um botão para limpar o histórico caso o usuário queira;
- Possui tratamento de erros para operações inválidas ( Por exemplo, divisão por zero );
- Possui um botão de LogOut caso o usuário queira sair.
  

## Tecnologias Utilizadas
- Python
- JavaScript
- Django
- SQLite
- HTML
- CSS

## Documentação
- 👉 [decisões técnicas](https://github.com/ThomasNicholas21/ProjetoCalculadora/blob/main/docs/technical_decisions.md)
- 👉 [desafios encontrados](https://github.com/ThomasNicholas21/ProjetoCalculadora/blob/main/docs/challenges.md)

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone https://github.com/ThomasNicholas21/ProjetoSympla.git
```

### 2. Criar ambiente virtual
Crie um ambiente virtual.
```bash
python -m venv venv
```

### 3. Instalar dependências do projeto
```bash
pip install -r requirements.txt
```

### 4. Fazer migrações
Primeiro execute: 
```bash
python manage.py makemigrations
```
Depois:
```bash
python manage.py migrate
```
### 5. Criar Super Usuário
```bash
python manage.py createsuperuser
```
### 6. Acessar a Aplicação
- **Frontend**: `http://localhost:8000`
- **Admin**: `http://localhost:8000/admin`
- **Login** `http://127.0.0.1:8000/login/`
- **SignUp** `http://127.0.0.1:8000/signup/`
- **Calculator** `http://127.0.0.1:8000/calculator/`

## Como executar testes
```bash
python manage.py tests
```
ou
```bash
pytest
```

## Autor
Projeto desenvolvido por **Thomas Nicholas**.

