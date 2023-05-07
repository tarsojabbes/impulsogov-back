# Teste técnico - ImpulsoGov - Backend

Esta API utiliza do Poetry para gerenciamento de dependências. Portanto, para executá-la é necessário ter o Poetry instalado. Você pode saber como por [aqui](https://python-poetry.org/docs/).

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

## Rotas e Parâmetros

- A rota <code>localhost:8000</code> retornará ambos os horários atuais em GMT -3 e GMT -5. Caso seja informado a query parameter <code>gmt</code> (ex: <code>localhost:8000/?gmt=-3</code>), será retornado o GMT somente para aquele fuso horário.

- Caso o GMT informado seja diferente de -3 e -5, a API retornará um erro 400 (Bad Request) e uma mensagem de erro informando que não o GMT informado não é suportado.

- A rota <code>localhost:8000/docs</code> fornece uma interface gráfica com a documentação da API e um ambiente de execução de chamadas à API.
