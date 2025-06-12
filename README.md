# **API de Blog com Django e Poetry**

Esta é uma API RESTful para um sistema de blog, desenvolvida com **Django REST Framework**. A API permite a criação, leitura, atualização e exclusão (CRUD) de postagens, categorias e tags.

O projeto utiliza **Poetry** para gerenciamento de dependências, **Docker** e **Docker Compose** para containerização, e é configurado para rodar com um banco de dados **PostgreSQL**.

## **Funcionalidades**

* ✅ Gerenciamento completo (CRUD) para **Postagens**.  
* ✅ Gerenciamento completo (CRUD) para **Categorias**.  
* ✅ Gerenciamento completo (CRUD) para **Tags**.  
* ✅ Relacionamento entre postagens, autores (usuários), categorias e tags.  
* ✅ API Navegável (Browsable API) fornecida pelo DRF para testes fáceis no navegador.

## **Tecnologias Utilizadas**

* **Backend:** Python, Django, Django REST Framework  
* **Banco de Dados:** PostgreSQL  
* **Gerenciador de Pacotes:** Poetry  
* **Containerização:** Docker, Docker Compose  
* **Variáveis de Ambiente:** python-dotenv

## **Configuração e Instalação**

Siga os passos abaixo para configurar e rodar o projeto.

### **Pré-requisitos**

* **Git**  
* **Docker**  
* **Docker Compose**  
* **Poetry** (para desenvolvimento local sem Docker)

### **Opção 1: Rodando com Docker (Recomendado)**

Este método containeriza a aplicação e o banco de dados, simplificando a configuração.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/blog-api.git
   
   cd blog-api
   ```

3. Configure as Variáveis de Ambiente:  
   Crie o arquivo .env a partir do exemplo. Os valores já estão, em sua maioria, alinhados com o docker-compose.yml.
   ```bash
   cp .env.example .env
   ```

5. Construa e inicie os containers:  
   Este comando irá construir a imagem Docker para a aplicação e iniciar os serviços da API e do banco de dados.  
   docker-compose up \--build

   A API estará disponível em http://127.0.0.1:8000/api/.

### **Opção 2: Rodando Localmente**

Use este método se preferir não usar Docker.

1. **Clone o repositório** e instale as **dependências com Poetry** (passos 1 e 2 da documentação anterior).  
2. **Configure o .env** para apontar para o seu servidor PostgreSQL local.  
3. **Aplique as migrações e inicie o servidor:**
```bash
   poetry run python manage.py migrate  
   poetry run python manage.py runserver
```

## **Estrutura do Projeto**

.  
├── api/             \# App da API (models, views, serializers)  
├── core/            \# App de configuração do projeto (settings, urls)  
├── .env.example     \# Arquivo de exemplo para variáveis de ambiente  
├── .gitignore       \# Arquivos ignorados pelo Git  
├── docker-compose.yml \# Orquestração dos containers  
├── Dockerfile       \# Definição do container da aplicação  
├── manage.py        \# Utilitário de linha de comando do Django  
├── poetry.lock      \# Arquivo de lock de dependências  
├── pyproject.toml   \# Arquivo de configuração do Poetry  
└── README.md        \# Este arquivo

## **Endpoints da API**

O prefixo base para todos os endpoints é /api/.

| Método HTTP | Endpoint | Descrição |
| :---- | :---- | :---- |
| GET | /posts/ | Lista todas as postagens. |
| POST | /posts/ | Cria uma nova postagem. |
| GET | /posts/{id}/ | Obtém os detalhes de uma postagem. |
| PUT/PATCH | /posts/{id}/ | Atualiza uma postagem. |
| DELETE | /posts/{id}/ | Exclui uma postagem. |
| GET | /categories/ | Lista todas as categorias. |
| POST | /categories/ | Cria uma nova categoria. |
| GET | /categories/{id}/ | Obtém os detalhes de uma categoria. |
| GET | /tags/ | Lista todas as tags. |
| POST | /tags/ | Cria uma nova tag. |
| GET | /tags/{id}/ | Obtém os detalhes de uma tag. |

## **Próximos Passos**

* \[ \] Implementar autenticação de usuário com JWT (JSON Web Tokens).  
* \[ \] Adicionar testes unitários e de integração.  
* \[ \] Implementar paginação nos endpoints de listagem.  
* \[ \] Adicionar filtros e busca aos endpoints.  
* \[ \] Otimizar a imagem Docker para produção (multi-stage builds).
