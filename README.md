![twitter_header_1500x500](https://github.com/user-attachments/assets/95aa6c44-13b4-410d-a3fd-cc0a566da9f0)
## BACK-END
Este projeto é um site onde é possível cadastrar cães para adoção. Ele permite que os usuários adicionem informações sobre cães disponíveis para adoção e visualizem os cães cadastrados.

Obs.: As fotos dos animais são meramente ilustrativas e fazem parte de uma requisição REST para uma API Externa (explicado ao longo deste documento)

## Descrição

Este repositório contém o código fonte do backend para o projeto de adoção de cães utilizando Flask como framework web e SQLite como banco de dados.

## Funcionalidades

- Cadastro e atualização de pets para adoção.
- Exibição e remoção de pets cadastrados.
- Integração com uma API externa para obter informações adicionais sobre os pets.

## Instruções de Instalação

Siga as etapas abaixo para configurar o ambiente local e instalar as dependências necessárias:

### Pré-requisitos

Certifique-se de ter o Docker instalado em sua máquina. Você pode verificar se o Docker está instalado executando o seguinte comando:

```sh
docker --version
```

Se o Docker não estiver instalado, siga as instruções de instalação na [documentação oficial do Docker](https://docs.docker.com/)

## Passo a passo para a instalação

1. **Clone o repositório:**
```sh
git clone https://github.com/raquelwainfas/pjt_maqp_backend.git
cd seu-repositorio
```
2. **Construa a imagem Docker:**

Navegue até o diretório do projeto e execute o comando abaixo para construir a imagem Docker:
```sh
docker build -t backend:1.0 .
```
3. **Execute o contêiner Docker:**

Depois que a imagem for construída, será informado o ID da imagem. Execute o seguinte comando para iniciar o contêiner:
```sh
docker run --rm -d -p 5000:5000 <id da imagem>
```
Este comando irá executar o contêiner em segundo plano (-d) e mapear a porta 5000 do contêiner para a porta 5000 do host, tornando o site acessível em `http://localhost`

## Comandos de Parada do Contêiner

* **Para para a execução do contêiner:**
 
Primeiro, liste os contêineres em execução para encontrar o ID ou nome do contêiner:
```sh
docker ps
```
Em seguida, pare o contêiner usando o ID ou nome do contêiner:
```bash
docker stop <container_id_or_name>
```

## Estrutura do Back-end do Projeto
```sh
/pjt_maqp_backend
│   app.py
│   Dockerfile
│   requirements.txt
└───instance
    └───animais.db
```
## Arquitetura

![Arquitetura_fdbranco](https://github.com/user-attachments/assets/4c8036fe-9d99-44aa-a614-a071cf772917)

### Detalhamento dos Componentes

<details>
<summary>Usuário</summary>
Interage com a aplicação através de um navegador web.
</details>

<details>
<summary>Camada de Apresentação</summary>

* **HTML:** Estrutura da página.
* **CSS:** Estilização da página.
* **JavaScript:** Comportamento dinâmico e interatividade.
* **Bootstrap:** Framework CSS para estilização responsiva e componentes prontos.
</details>

<details>
<summary>Camada de Aplicação</summary>

* **Flask:** Gerencia rotas, lógica de negócio e renderização de templates.
* **app.py:** Arquivo principal onde a aplicação Flask é configurada e executada.
</details>

<details>
<summary>Camada de Dados</summary>

**SQLite:** Banco de dados relacional para armazenar informações sobre os pets disponíveis para adoção.
</details>

<details>
<summary>Infraestrutura</summary>

**Docker:** Ferramenta para criar contêineres que encapsulam a aplicação e suas dependências.
</details>

## Entendendo o Fluxo de Interação
1. **Usuário** acessa a aplicação através do navegador.
2. **Camada de Apresentação** envia requisições HTTP para o servidor
3. **Camada de Aplicação** processa as requisições, interage com o banco de dados (se necessário) e retorna as respostas apropriadas
4. **Camada de Dados** armazena e recupera dados conforme solicitado pela aplicação.
5. **Infraestrutura Docker** garante que a aplicação e suas dependências rodem de forma consistente e isolada.
6. **API Externa** a camada de aplicação é responsável por processar a requisição para essa API. O endpoint utilizado: https://dog.ceo/api/breeds/image/random.

>Essa arquitetura modularizada ajuda a manter o código organizado, facilita a manutenção e possibilita a escalabilidade futura da aplicação.

***
## Rotas - API de dados
- / : Retorna informação de que a aplicação está no ar.
- GET /animais: Retorna todos os pets cadastrados.
- POST /animais: Cadastra um novo pet.
- PUT /animais/id_animal: Atualiza as informações de um pet existente.
- DELETE /animais/id_animal: Remove um pet do sistema.

## API EXTERNA
### Dog API
**Endpoint:**

`https://dog.ceo/api/breeds/image/random`

**Retorno:**

~~~json
{
    "message": "https://images.dog.ceo/breeds/retriever-golden/n02099601_5893.jpg",
    "status": "success"
}
~~~
A chave `message` retorna diretórios aleatórios que contem a imagem do pet. Esta URL fica armazenada no banco de dados `instance/animais.db` e é automaticamente associada a um animal no momento de sua criação (inserção).

Rota: `/animais`

Tipo de requisição: `POST`

###### Se tiver alguma dúvida ou encontrar algum problema, sinta-se à vontade para abrir uma issue no repositório.

***
#### Sprint: Arquitetura de Software - Pós Graduação em Engenharia de Software - PUC-RIO (2024)



