# Bem vindo a API de contatos

### Como rodar o projeto

#### Instalar requisitos

- Execute o comando `pip install -r requirements.txt` para instalar as dependências do projeto

#### Configurar o banco de dados

- O projeto utiliza tortoise-orm com banco de dados postgresql, caso deseje utilizar MySQL, altere a variável `DATABASE_URL` no arquivo `.env` para a url do banco de dados desejado.
  - Exemplo: `DATABASE_URL=mysql://user:password@localhost:3306/database`

#### Subir a API

- Execute o comando `uvicorn main:app --reload` para subir a API

```
Para acessar a API utilize a url http://127.0.0.1:8000
```

## Rotas

```
Documentação completa da API em http://127.0.0.1:8000/docs
```

- GET /contacts

  - Retorna todos os contatos
  - Exemplo de retorno:

  ```json
  [
    {
      "con_id": "a2112317-5cca-43fd-b004-bc0e6244f296",
      "con_name": "João",
      "con_email": "joao@email.com",
      "con_phone": "12345678910",
      "con_updated": "2024-10-06T19:37:59.628506+00:00",
      "con_created": "2024-10-06T19:37:59.628506+00:00"
    },
    {
      "con_id": "bff80f2b-2684-4330-bae4-c04673e49660",
      "con_name": "Maria",
      "con_email": "maria@email.com",
      "con_phone": "10987654321",
      "con_updated": "2024-10-06T19:37:59.628506+00:00",
      "con_created": "2024-10-06T19:37:59.628506+00:00"
    }
  ]
  ```

- GET /contacts/:id

  - Retorna um contato específico pelo id
  - Exemplo de retorno:

  ```json
  {
    "con_id": "a2112317-5cca-43fd-b004-bc0e6244f296",
    "con_name": "João",
    "con_email": "joao@email.com",
    "con_phone": "12345678910",
    "con_updated": "2024-10-06T19:37:59.628506+00:00",
    "con_created": "2024-10-06T19:37:59.628506+00:00"
  }
  ```

- POST /contacts

  - Cria um novo contato
  - Exemplo de corpo para a requisição:

  ```json
  {
    "con_name": "João",
    "con_email": "joao@email.com",
    "con_phone": "12345678910"
  }
  ```

- PUT /contacts/:id

  - Atualiza um contato pelo id
  - Exemplo de corpo para a requisição:

  ```json
  {
    "con_name": "João",
    "con_email": "",
    "con_phone": "12345678910"
  }
  ```

- DELETE /contacts/:id

  - Deleta um contato pelo id
  - Exemplo de retorno:

  ```json
  {
    "message": "Contact deleted"
  }
  ```
