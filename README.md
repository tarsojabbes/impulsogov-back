# Teste técnico - ImpulsoGov - Backend

Esta API utiliza do Poetry para gerenciamento de dependências. Portanto, para executá-la é necessário ter o Poetry instalado. Você pode saber como por [aqui](https://python-poetry.org/docs/)

## Como rodar a API

- Abra um terminal e acesse o diretório raiz do projeto.

- Ative o shell do Poetry executando o seguinte comando:
    ```sh
    poetry shell
    ```

- Instale as dependências do projeto executando o seguinte comando:
    ```sh
    poetry install
    ```

- Execute o projeto com o Uvicorn executando o seguinte comando:
    ```sh
    uvicorn main:app
    ```
Com isso, a API estará rodando na porta 8000 do seu localhost. Você pode acessar a API em seu navegador da web visitando o endereço http://localhost:8000.

