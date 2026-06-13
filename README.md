# API REST - Sistema Escolar

Aplicaçao simples feita com **Flask** e **Faker** para ensinar **HTTP Methods** (GET, POST, PUT, DELETE) e **operaçoes CRUD** (Create, Read, Update, Delete).

Os dados sao gerados automaticamente com a biblioteca Faker -- nao precisa de banco de dados.

---

## Requisitos

- Python 3.8+
- pip

## Instalaçao

```bash
cd sistema-escolar
pip install flask faker
```

## Executar

```bash
python3 app.py
```

O servidor inicia em `http://localhost:5000`.

---

## Endpoints

| Metodo HTTP | Rota               | CRUD   | Descriçao              |
|-------------|--------------------|--------|------------------------|
| `GET`       | `/`                | -      | Home com lista de rotas |
| `GET`       | `/alunos`          | **R**ead | Listar todos os alunos |
| `GET`       | `/alunos/{id}`     | **R**ead | Obter um aluno pelo ID |
| `POST`      | `/alunos`          | **C**reate | Criar um novo aluno  |
| `PUT`       | `/alunos/{id}`     | **U**pdate | Atualizar um aluno   |
| `DELETE`    | `/alunos/{id}`     | **D**elete | Remover um aluno     |

---

## Como testar com curl

### Listar todos os alunos

```bash
curl http://localhost:5000/alunos
```

### Obter um aluno pelo ID

```bash
curl http://localhost:5000/alunos/1
```

### Criar um novo aluno

```bash
curl -X POST http://localhost:5000/alunos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ana Souza", "curso": "Medicina", "email": "ana@email.com"}'
```

### Atualizar um aluno

```bash
curl -X PUT http://localhost:5000/alunos/1 \
  -H "Content-Type: application/json" \
  -d '{"nome": "Nome Alterado", "curso": "Direito"}'
```

### Deletar um aluno

```bash
curl -X DELETE http://localhost:5000/alunos/1
```

---

## Modelo do Aluno

| Campo            | Tipo    | Exemplo                      |
|------------------|---------|------------------------------|
| `id`             | int     | 1                            |
| `nome`           | string  | "Joao Silva"                 |
| `email`          | string  | "joao@email.com"             |
| `matricula`      | string  | "20264001"                   |
| `curso`          | string  | "Ciencia da Computaçao"     |
| `data_nascimento`| string  | "2000-05-12"                 |
| `telefone`       | string  | "+55 (011) 99999-8888"       |
| `ativo`          | boolean | true                         |

---

## Codigos de Status

| Codigo | Significado              | Quando ocorre                     |
|--------|--------------------------|-----------------------------------|
| 200    | OK                       | GET, PUT, DELETE com sucesso      |
| 201    | Created                  | POST com sucesso                  |
| 400    | Bad Request              | Corpo vazio ou campos obrigatorios faltando |
| 404    | Not Found                | Aluno com ID inexistente          |

---

## Mapa: HTTP Methods x CRUD

| HTTP Method | CRUD Operation | Uso |
|-------------|---------------|-----|
| `GET`       | **R**ead      | Consultar dados (sem efeito colateral) |
| `POST`      | **C**reate    | Criar um novo recurso                |
| `PUT`       | **U**pdate    | Atualizar um recurso existente       |
| `DELETE`    | **D**elete    | Remover um recurso                   |

---

## Estrutura do Projeto

```
sistema-escolar/
  app.py              # Codigo principal da API
  requirements.txt    # Dependencias (flask, faker)
  README.md           # Este arquivo
```
