# 🩺 Sistema de Gerenciamento de Clínica Veterinária


## 👨‍🏫 Autor
- João Bernardo — Desenvolvedor Back-end e Modelagem de Dados  

## 📘 Visão Geral do Sistema

O **Sistema de Gerenciamento de Clínica Veterinária** foi desenvolvido para automatizar o controle das principais operações de uma clínica, oferecendo funcionalidades para **cadastro, gerenciamento e relacionamento** entre entidades como **clientes**, **pets**, **veterinários**, **pedidos**, **serviços** e **pagamentos**.

Através de uma **interface web moderna**, o sistema permite registrar informações completas de clientes e seus animais de estimação, além de gerenciar os atendimentos realizados, os serviços prestados e os valores correspondentes.

---

## ⚙️ Funcionalidades Principais

### 🏥 Cadastro de Clínicas
Armazena dados institucionais da clínica, como **nome**, **CNPJ**, **endereço** e **telefone**.

### 👨‍⚕️ Gerenciamento de Veterinários
Permite cadastrar veterinários vinculados a uma clínica, registrando **nome**, **telefone** e **especialidade**.

### 👤 Controle de Clientes
Gerencia os dados pessoais de cada cliente, incluindo **nome**, **telefone**, **e-mail** e **endereço**.

### 🐶 Cadastro de Pets
Cada cliente pode possuir vários pets cadastrados, com informações detalhadas como **nome**, **tipo**, **raça**, **sexo** e **data de nascimento**.

### 📋 Gestão de Pedidos (Atendimentos)
Relaciona **cliente**, **pet** e **veterinário**, armazenando a **data**, **anexos** e o **valor total** dos serviços prestados.

### 💉 Serviços e Itens de Serviço
Cada pedido pode conter múltiplos serviços, como **consultas**, **vacinas** ou **exames**.  
O sistema calcula automaticamente **subtotais** e **valores totais** de cada atendimento.

### 💳 Pagamentos
Cada pagamento é vinculado a um pedido e armazena **valor pago** e **forma de pagamento** (dinheiro, cartão, pix, etc.).

### 📎 Anexos
Permite associar **arquivos** e **informações complementares** aos pedidos, como **relatórios**, **exames** e **laudos**.

---

## 🧩 Estrutura e Relacionamentos

O sistema segue uma **modelagem relacional** conforme o diagrama de classes:

- Uma **Clínica** possui vários **Veterinários** e **Clientes**.  
- Cada **Cliente** pode possuir vários **Pets**.  
- Um **Pedido** está associado a um **Cliente**, a um **Pet** e a um **Veterinário**.  
- Um **Pedido** pode ter vários **Itens de Serviço**, **Pagamentos** e **Anexos**.  
- Cada **Serviço** pode aparecer em vários **Itens de Serviço**.

---

## 🧱 Dependências do Projeto

O projeto foi desenvolvido utilizando o framework **Django**, e depende dos seguintes pacotes Python:

| Pacote | Versão | Descrição |
|--------|---------|-----------|
| **asgiref** | 3.9.2 | Gerencia a interface assíncrona de servidores web para o Django. |
| **Django** | 5.2.7 | Framework principal usado no desenvolvimento do sistema. |
| **Pillow** | 12.0.0 | Biblioteca para manipulação e upload de imagens (usada para fotos de clinica, pets etc). |
| **sqlparse** | 0.5.3 | Utilizado internamente pelo Django para formatar e processar SQL. |
| **tzdata** | 2025.2 | Fornece informações de fuso horário, garantindo compatibilidade entre sistemas. |

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.2.7-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


---

## 🧭 Como o Sistema Funciona

O sistema foi estruturado em **aplicações Django** que se comunicam entre si.  
Cada app representa um módulo funcional (ex: clientes, pets, veterinários, pedidos).

A arquitetura **MVC (Model–View–Controller)** do Django é aplicada da seguinte forma:

- **Models:** Definem as tabelas e relacionamentos do banco de dados (conforme o diagrama).  
- **Views:** Processam as requisições HTTP e controlam a lógica de negócios.  
- **Templates:** Geram as páginas HTML dinâmicas que o usuário visualiza.  
- **URLs:** Fazem o mapeamento das rotas para cada view.

Imagens e arquivos enviados pelos usuários são armazenados dentro da pasta `media/`, configurada por:

```
pythonMEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## 🚀 Como Rodar o Projeto
1️⃣ Clonar o Repositório
```
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

2️⃣ Criar e Ativar o Ambiente Virtual
```
python -m venv venv
venv\Scripts\activate      # Windows
```
 ou
```
source venv/bin/activate   # Linux/Mac
```

3️⃣ Instalar as Dependências
```
pip install -r requirements.txt
```

Caso não tenha o arquivo requirements.txt, instale manualmente:
```
pip install Django==5.2.7 Pillow==12.0.0
```
4️⃣ Criar o Banco de Dados
```
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Criar um Superusuário (opcional)
```
python manage.py createsuperuser
```

6️⃣ Rodar o Servidor de Desenvolvimento
```
python manage.py runserver
```

Acesse no navegador:
👉 http://127.0.0.1:8000/

🗂️ Estrutura Simplificada de Pastas
```
clinica_veterinaria/
│
├── manage.py
├── clinica_veterinaria/        # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── apps/
│   ├── cliente/
│   ├── pet/
│   ├── veterinario/
│   ├── servico/
│   ├── pedido/
│   └── pagamento/
│
├── media/                      # Armazenamento de imagens e uploads
└── templates/                  # Páginas HTML
```
