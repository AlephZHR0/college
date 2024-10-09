<!-- # Prova

# Conceitos

1. Nas suas palavras por que é importante saber SQL?

Para manipular dados em um banco de dados, seja para inserir, atualizar, deletar ou consultar dados, além de ser uma ferramenta muito poderosa e útil dentro e fora de empresas, é muito requisitada no mercado de trabalho.

2. Explique com suas suas palavras o que faz a query abaixo:
    
    ```sql
    	SELECT last_name, first_name, city FROM customer WHERE city LIKE "S%";
    ```

Exibe os campos last_name, first_name e city da tabela customer onde o campo city começa com a letra S.
    
3. O que são queries?

    1. Consultas no banco de dados
    2. Formas de armazenar dados
    3. Comandos para modificar bancos de dados
    4. Um sistema de banco de dados

Alternativa 1

4. Nas suas palavras, quando você usaria a função COALESCE?

Para o caso em que eu for fazer uma consulta ou operação e souber que algum campo pode ter valores nulos, e eu quiser que o valor nulo seja substituído por algum outro valor.

5. Se criarmos uma coluna com a multiplicação de uma coluna com outra e alguma linha neste processo tiver nulos, qual será o resultado da multiplicação para estas linhas?

    1. NULL
    2. ZERO
    3. INFINITO
    4. STRING VAZIA
    6. ""

Alternativa 1

6. Qual operador busca qualquer caractere mas apenas uma vez?

    1. *
    2. _
    3. LIKE
    4. %
    5. #

Alternativa 2

# Problemas de Queries / Estudo de caso

## Cenário:

A empresa Freitas Laminados é uma organização que deseja criar um sistema para gerenciar informações de funcionários. Eles coletam dados sobre seus funcionários. Eles coletam dados sobre seus funcionários, incluindo nome, ID, salário, data de admissão, nota de avaliação, departamento e cargo. A Empresa Freitas Laminados deseja usar SQL para criar e gerenciar uma tabela de funcionários para manter essas informações de maneira eficaz.

## Desafio:

O desafio é criar uma tabela de funcionários que possa armazenar informações relevantes e, em seguida, executar consultas SQL para adicionar, atualizar e consultar esses dados.

Exercício 1: Criar uma tabela de funcionários. Escrever query abaixo da tabela.

| Id_Empregado | Nome_Empregado | Departamento | Cargo | Salario | Data_Admissao | Aval. |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

CREATE TABLE funcionarios (
    Id_Empregado INT NOT NULL,
    Nome_Empregado VARCHAR(255) NOT NULL,
    Departamento VARCHAR(255) NOT NULL,
    Cargo VARCHAR(255) NOT NULL,
    Salario INT NOT NULL,
    Data_Admissao DATE NOT NULL,
    Aval INT NOT NULL
);

Exercício 2: Inserir dados na tavela de funcionários. Escrever query abaixo da tabela.

| Id_Empregado | Nome_Empregado | Departamento | Cargo | Salario | Data_Admissao | Aval. |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Joao | RH | Analista | 5000 | “2022-01-01” | 4 |
| 2 | Maria | Financas | Analista | 6000 | “2023-01-01” | 5 |
| 3 | Carlos | TI | Desenvolvedor | 5500 | “2024-01-01” | 4 |
| 4 | Ana | Vendas | Gerente | 5200 | "2025-01-01” | 3 |

INSERT INTO funcionarios (Id_Empregado, Nome_Empregado, Departamento, Cargo, Salario, Data_Admissao, Aval) VALUES
(1, "Joao", "RH", "Analista", 5000, "2022-01-01", 4),
(2, "Maria", "Financas", "Analista", 6000, "2023-01-01", 5),
(3, "Carlos", "TI", "Desenvolvedor", 5500, "2024-01-01", 4),
(4, "Ana", "Vendas", "Gerente", 5200, "2025-01-01", 3);

Exercício 3: Escreva uma query para trazer todas as informações da tabela de funcionários.

SELECT * FROM funcionarios;

Exercício 4 Escreva uma query para: ordenar os empregados por ordem de salário do maior para o menor;

SELECT * FROM funcionarios ORDER BY Salario DESC;

Exercício 5: Crie uma consulta para trazer todos os funcionários cujo o nome começa com “M”

SELECT * FROM funcionarios WHERE Nome_Empregado LIKE "M%";

Exercício 6: Escreva uma query para: mostrar todos os Cargos diferentes da tabela funcionários sem repetição.

SELECT DISTINCT Cargo FROM funcionarios;

Exercício 7: Escreva uma query para: Trazer todos os empregados que recebem por dia mais do que 200. Considere 22 dias úteis.

SELECT * FROM funcionarios WHERE Salario / 22 > 200;

Exercício 8: Escreva uma query para: criar uma nova coluna chamada Bonus. O Bônus dos funcionários será calculado como: funcionários com nota 4 ou maior receberão R$10.000 de Bônus e os demais receberão nenhum Bônus.

SELECT *, CASE WHEN Aval >= 4 THEN 10000 ELSE 0 END AS Bonus FROM funcionarios;

Exercício 9: Crie uma nova coluna: Tempo_de_Casa, que receberá “Antigo” caso o funcionário tenha o ID_Empregado menor que 3 caso contrário escreva “Novo”.

SELECT *, CASE WHEN Id_Empregado < 3 THEN "Antigo" ELSE "Novo" END AS Tempo_de_Casa FROM funcionarios;

 -->