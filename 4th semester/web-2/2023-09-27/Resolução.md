# Questão 1

1. Falso. A view é responsável pela apresentação e pela interface com o usuário.

2. Verdadeiro. O controller é o componente que faz a ponte entre o model e a view, garantindo que a lógica de negócio e a apresentação sejam separadas.

3. Falso. O model é responsável pela lógica de negócio e pelo acesso aos dados, mantendo os dados e o estado da aplicação.

4. Verdadeiro. Uma das vantagens do padrão MVC é a divisão clara de responsabilidades entre os componentes, o que facilita a manutenção e escalabilidade da aplicação.

# Questão 3

1. Falso. A camada web é responsável por receber as requisições HTTP e enviar as respostas HTTP. A camada de negócios é a responsável pela lógica de negócios e a camada de persistência é a responsável pela persistência de dados.

2. Verdadeiro. A camada de serviço é a responsável por tratar da lógica de negócios, sem se preocupar diretamente com detalhes de persistência ou protocolos HTTP.

3. Verdadeiro. A camada de persistência é a responsável por lidar com os detalhes específicos da conexão e operações em bancos de dados, como inserções, atualizações e consultas.

4. Falso. É na camada web que as requisições HTTP são inicialmente recebidas e tratadas antes de serem passadas para outras camadas.

# Questão 5

```python
def update_user(User, dados: dict):
    user = db.query.get(User.id)
    for key, value in dados.items():
        user[key] = value
    user[key] = value
    db.save(user)
    db.session.commit()
```
