# ProjetoSD-API

## Pre-requisitos
MySQL, MySQLServer, Python 3

## Installation

Use o package manager [pip](https://pip.pypa.io/en/stable/) para a instalação do packages da API.

Crie um database com o nome projetoSD
```
mysql > create database "projetoSD"
```

Primeiramente rode o comando:
```bash
pip install -r requirements.txt --no-index
```
Após a instalação do packages, rode os seguintes comandos:
```bash
flask db init
flask db migrate
flask db upgrade
```


## Usage

Rode o comando para iniciar a API

```bash
flask run
```


## Rotas criadas

#### cadastro:

- Tipo - POST
- Nome - /singin 
- form-data
```javascript
{
  "email" : "teste@xxx.com",
  "password" : "12132",
  "cnpj" : "",
  "ramo" : "",
}
```

#### login:

- Tipo - POST
- Nome - /singup 
- form-data
```javascript
{
  "email" : "teste@xxx.com",
  "password" : "12132",
}
```


#### listagem de clientes da empresa:

- Tipo - GET
- Nome - /client
- querryParams : 
> search = campo de busca 


#### cadastro de clientes de um empresa:

- Tipo - POST
- Nome - /client 
- form-data
```javascript
{
  "email" : "teste@xxx.com",
  "name" : "nomeDoCliente",
}
```
