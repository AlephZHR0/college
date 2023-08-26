
# #Aula 03 - Revisão de manipulação básica de dados
# 
# 
# Ao final desta tarefa, você será capaz de manipular enormes dados tabulares:
# 
# *   Calcular estatísticas de diferentes colunas (mín., máx., média, quantis, etc.);
# *   Selecionar observações/características por condição/índice;
# *   Criar novas combinações não lineares das colunas (engenharia de recursos);
# *   Executar limpeza automatizada de dados;
# *   e mais.
# 
# <br>
# 
# ---
# 
# <br>
# 
# Estaremos usando dados de preços de venda de casas de King County, Wahington, EUA. Este conjunto de dados é de domínio público e pode ser obtido no Kaggle: https://www.kaggle.com/harlfoxem/housesalesprediction
# 
# <br>
# 
# Você precisará do arquivo ` kc_house_data.csv`.

import pandas as pd
import numpy as np
# ##Carregando dados
# 
# Como sempre, em Data Science, você começa carregando os dados:
# 
# *   Comece carregando o arquivo `house_data.csv` usando a função `pd.read_csv()`.
# *   Você também pode querer aumentar o máximo de colunas de pandas exibidas: defina` pd.options.display.max_columns` para 30
# *   Imprima as 10 principais observações na tabela. `.head()`
# *   Imprima as últimas 10 observações na tabela. `.tail()`
# *   Imprima todos os nomes das colunas de dados usando o método `.columns`
# *   Imprima o tamanho dos dados (número de linhas e colunas). Este é forma (`.shape`) dos dados.

# Carregue os dados
df = pd.read_csv('C:/Users/jpjoa/OneDrive/Documents/college/4th semester/data science/kc_house_data.csv')

# Observe as 10 primeiras observações (int)

# Q1.1 Qual é o preço de uma casa com `id` == 7237550310?
df.query('id == 7237550310')["price"]
# Q1.2 Quantos quartos tem uma casa com `id` == 7237550310?
df.query('id == 7237550310')["bedrooms"]
# Q1.3 Quando a casa com `id` == 2414600126 foi construída (`yr_built`)?
df.query('id == 2414600126')["yr_built"]
# Q1.4 Qual é a `grau` de uma casa com `id` == 5631500400?
df.query('id == 5631500400')["grade"]
# Q1.5 Quando a casa com `id` == 6414100192 foi reformada (`yr_renovated`)?
df.query('id == 6414100192')["yr_renovated"]

# Q1.1 Qual é o preço de uma casa com `id` == 7237550310?
df.query('id == 7237550310')["price"]
# Q1.2 Quantos quartos tem uma casa com `id` == 7237550310?
df.query('id == 7237550310')["bedrooms"]
# Q1.3 Quando a casa com `id` == 2414600126 foi construída (`yr_built`)?
df.query('id == 2414600126')["yr_built"]
# Q1.4 Qual é a `grau` de uma casa com `id` == 5631500400?
df.query('id == 5631500400')["grade"]
# Q1.5 Quando a casa com `id` == 6414100192 foi reformada (`yr_renovated`)?
df.query('id == 6414100192')["yr_renovated"]

# Observe as últimas 10 observações (int)
df.tail(10)
# Q2.1 Qual é o preço de uma casa com `id` == 263000018?
df.query('id == 263000018')["price"]
# Q2.2 Quantos quartos tem uma casa com `id` == 291310100?
df.query('id == 291310100')["bedrooms"]
# Q2.3 Quando a casa com `id` == 1523300141 foi construída (`yr_built`)?
df.query('id == 1523300141')["yr_built"]
# Q2.4 Quantos andares tem uma casa com `id` == 2997800021?
df.query('id == 2997800021')["floors"]
# Q2.5 Qual é o CEP da casa com `id` == 7852140040?
df.query('id == 7852140040')["zipcode"]

# Aumente o máximo de colunas exibidas
pd.set_option('display.max_columns', 21)

# Observe as 10 principais observações novamente
df.head(10)
# Há alguma nova coluna exibida?
"condition"

# Imprima todos os nomes de colunas/recursos (int)
df.columns
# Q3.1 Quantas colunas têm o prefixo `yr_`?
count = 0
for column in df.columns:
    if column.startswith("yr_"):
        count += 1
print(f"{count} colunas têm o prefixo `yr_`")
# Q3.2 Quantas colunas têm o prefixo `sqft_`?
count = 0
for column in df.columns:
    if column.startswith("sqft_"):
        count += 1
print(f"{count} colunas têm o prefixo `sqft_`")
# Q3.3 Quantas colunas associadas às coordenadas terrestres da casa existem nos dados?
count = 0
for column in df.columns:
    if column.startswith("lat") or column.startswith("long"):
        count += 1
print(f"{count} colunas associadas às coordenadas terrestres da casa existem nos dados")
# Q3.4 Quantas colunas têm 'rooms' em seus nomes?
count = 0
for column in df.columns:
    if "rooms" in column:
        count += 1
print(f"{count} colunas têm 'rooms' em seus nomes")

# Imprima o tamanho dos dados (int)
df.shape
# Q4.1 Quantas observações existem nos dados?
df.shape[0]
# Q4.2 Quantos características existem nos dados?
df.shape[1]
# ##Exploração de dados básicos
# 
# Vamos fazer algumas noções básicas:
# 
# *   Conte (`.count()`) número de não NaN's em cada coluna.
# *   Há algum valor ausente nos dados?
# *   Conte o número de valores únicos em cada coluna `.nunique()`.
# *   O que isso diz sobre os recursos, que são provavelmente categóricos e numéricos?
# *   Use o `.describe()` do pandas para exibir estatísticas básicas sobre os dados.
# *   Use o `.value_counts()` do pandas para contar o número de valores únicos em uma coluna específica.
# *   Use o `.min()`, `.max()`, `.mean()`, `.std()` do pandas para exibir estatísticas específicas sobre os dados.
# *   Use o campo `.dtypes` do pandas para exibir tipos de dados em colunas.
# 
# **Dica:**  Você pode usar `.sort_index()` ou `.sort_values()` para classificar o resultado de `.value_counts()`

# Mostre o número de não NaN's em cada coluna (int)
df.count()
# Q5.1 Quantos valores NA existem na coluna `floors`?
df.shape[0] - df.count()["floors"]
# Q5.2 Quantos valores NA existem na coluna `grade`?
df.shape[0] - df.count()["grade"]
# Q5.3 Quantos valores de NA existem na coluna `bedrooms`?
df.shape[0] - df.count()["bedrooms"]
# Q5.4 Quantos valores NA existem na coluna `yr_built`?
df.shape[0] - df.count()["yr_built"]
# Q5.5 Quantos valores NA (não zeros, mas valores vazios e ausentes) existem na coluna `yr_renovated`?
df.shape[0] - df.count()["yr_renovated"]

# Conte o número de valores únicos em cada coluna (int)
df.nunique()
# Q6.1 Quantos valores exclusivos existem na coluna `bedrooms`?
df.nunique()["bedrooms"]
# Q6.2 Quantos valores únicos existem na coluna `grade`?
df.nunique()["grade"]
# Q6.3 Quantos valores únicos existem na coluna `yr_renovated`?
df.nunique()["yr_renovated"]
# Q6.4 Quantos valores exclusivos existem na coluna `bathrooms`?
df.nunique()["bathrooms"]
# Q6.5 Quantos valores únicos existem na coluna `long`?
df.nunique()["long"]

# Conte a frequência dos valores em diferentes colunas (lista de ints em ordem crescente)
for column in df.columns:
    print(df[column].value_counts().sort_index())
# Você pode selecionar uma coluna usando a mesma sintaxe para selecionar uma chave de um dicionário: `data[colname]`

# Q7.1 Para cada valor exclusivo de `floors`, forneça seu número de ocorrências.
df["floors"].value_counts()
# Q7.2 Para cada valor `condition` exclusivo, forneça seu número de ocorrências.
df["condition"].value_counts()
# Q7.3 Para cada valor exclusivo de 'bedrooms', forneça seu número de ocorrências.
df["bedrooms"].value_counts()
# Q7.4 Para cada valor único de `grade`, forneça seu número de ocorrências.
df["grade"].value_counts()
# Q7.5 Para cada valor `view` exclusivo, forneça seu número de ocorrências.
df["view"].value_counts()

# Exiba estatísticas básicas de dados usando .describe()

# Exiba algumas estatísticas de coluna (lista de floats, arredondado para 3 dígitos, por exemplo, 1.234)

# Q8.1 Quais são o máximo, o mínimo, a média e o padrão da coluna 'floors'?
round(df["floors"].describe(), 3)
# Q8.2 Quais são o máximo, mínimo, médio e padrão da coluna `bedrooms`?
round(df["bedrooms"].describe(), 3)
# Q8.3 Quais são o máximo, mínimo, médio e padrão da coluna `sqft_living`?
round(df["sqft_living"].describe(), 3)
# Q8.4 Quais são o máximo, o mínimo, a média e o padrão da coluna `price`?
round(df["price"].describe(), 3)
# Q8.5 Quais são o máximo, mínimo, médio e padrão da coluna `long`?
round(df["long"].describe(), 3)

# Exiba os tipos de dados de todas as colunas (int)
# Q9.1 Quantas colunas têm o tipo de dados `object`?
count = 0
for type in df.dtypes:
    if type == "object":
        count += 1
print(f"{count} colunas têm o tipo de dados `object`")
# Q9.2 Quantas colunas têm o tipo de dados `int64`?
count = 0
for type in df.dtypes:
    if type == "int64":
        count += 1
print(f"{count} colunas têm o tipo de dados `int64`")
# Q9.3 Quantas colunas têm o tipo de dados `float64`?
count = 0
for type in df.dtypes:
    if type == "float64":
        count += 1
print(f"{count} colunas têm o tipo de dados `float64`")

# Exibe os tipos de dados de todas as colunas (lista de str)
# Q9.4 Quais são as colunas com dtype == `float64`?
for column in df.columns:
    if df[column].dtype == "float64":
        print(column)
# Q9.5 Quais são as colunas com dtype == `int64`?
for column in df.columns:
    if df[column].dtype == "int64":
        print(column)
# ## Seleção de dados
# 
# Em um `pandas.DataFrame` você pode selecionar
# 
# 1. Linha/s por posição (número inteiro [0 .. número de linhas - 1]) .iloc ou por DataFrame.index .loc:
# ```
# dados.loc[0]
# dados.loc[5:10]
# dados.iloc[0]
# dados.iloc[5:10]
# ```
# No entanto, esta é provavelmente a pior maneira de manipular linhas.
# 
# 2. Colunas por nome
# ```
# dados[nome da coluna]
# ```
# 
# 3. Linhas e colunas
# ```
# dados.loc[10, nome da coluna]
# dados.iloc[10, nome da coluna]
# ```
# 4. Usando máscara booleana
# ```
# máscara = dados[nome da coluna] > valor
# dados[máscara]
# ```
# Você pode combinar várias condições usando `&` `ou` | (`and`, `or`)
# ```
# cond1 = dados[coluna1] > valor1
# cond2 = dados[coluna2] > valor2
# dados[cond1 & cond2]
# ```
# 5. Usando consultas .query():
# ```
# valor = 5
# dados.query("nome da coluna > valor")
# ```
# Você pode combinar várias condições usando `and`, `or`
# ```
# dados.query("(nome da coluna1 > valor1) and (nome da coluna2 > valor2)")
# ```
# <br>entre outros.
# 
# Consulte https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html para obter mais exemplos.<br><br>
# Lembre-se de usar diferentes aspas " ou ' para nome da coluna dentro de uma consulta.

# configurando o índice do DataFrame para ser uma coluna `id`, agora .loc e .iloc terão comportamento diferente
df.index = df.id

# # descartando a coluna `id`, já que agora é um índice
df.drop('id', axis=1, inplace=True)

# # ordena dados por índice para maior clareza
df.sort_index(inplace=True)

# Seleciona linhas por posição (int)

# Q10.1 Quantos quartos tem uma casa na linha 777?
print(f"{df.iloc[777]['bedrooms'] } quartos")
# Q10.2 Quando foi construída uma casa na linha 9999?
print(f"foi construída em {df.iloc[9999]['yr_built']}")
# Q10.3 Quantos andares tem uma casa na linha 1337?
print(f"{df.iloc[1337]['floors']} andares")
# Q10.4 Quantos banheiros tem uma casa na linha 314?
print(f"{df.iloc[314]['bathrooms']} banheiros")
# Q10.5 Qual é o grau de uma casa na linha 2718?
print(f"grau {df.iloc[2718]['grade']}")

# Selecione as linhas por índice (int)

# Q11.1 Quantas vezes a casa com índice 1000102 foi vendida?
print(f"foi vendida {df.query('id == 1000102')['date'].count()} vezes")
# Q11.2 Qual é o preço da casa com índice 9842300095?
print(df.query('id == 9842300095')['price'].values[0])
# Q11.3 Quando foi construída a casa com índice 104510440?
print(f"foi construída em {df.query('id == 104510440')['yr_built'].values[0]}")
# Q11.4 Qual é a condição de uma casa com índice 252000300?
print(f"condição {df.query('id == 252000300')['condition'].values[0]}")
# Q11.5 Qual é a área habitável (em pés quadrados) da casa com índice 1225069038?
print(f"área habitável {df.query('id == 1225069038')['sqft_living'].values[0]}")

# Usando máscara ou a sintaxe .query, selecione linhas/colunas (int)

# Q12.1 Quantas casas foram construídas durante a Grande Depressão Americana (1929–1939)? Incluindo os anos inicial e final.
condition_1 = df["yr_built"] >= 1929
condition_2 = df["yr_built"] <= 1939
print(f"{df[condition_1 & condition_2].shape[0]} casas foram construídas durante a Grande Depressão Americana (1929–1939)")
# Q12.2 Quando foi construída a única casa com área de porão (basement) = 1024 pés quadrados?
condition = df["sqft_basement"] == 1024
print(f"foi construída em {df[condition]['yr_built'].values[0]}")
# Q12.3 Quantas casas estão com a nota mais alta possível?
nota_mais_alta = df["grade"].max()
condition = df["grade"] == nota_mais_alta
print(f"{df[condition]['grade'].count()} casas estão com a nota mais alta possível")
# Q12.4 Quando foi construída uma casa com número máximo de quartos?
max_quartos = df["bedrooms"].max()
condition = df["bedrooms"] == max_quartos
print(f"foi construída em {df[condition]['yr_built'].values[0]}")
# Q12.5 Quantas casas foram vendidas por 256.000 dólares?
condition = df["price"] == 256000
print(f"{df[condition]['price'].count()} casas foram vendidas por 256.000 dólares")

# Usando máscara ou a sintaxe .query, selecione linhas/colunas (int)

# Q13.1 Quantas casas à beira-mar (waterfront == 1) foram construídas durante a presidência de Nixon (1969—1974)? Incluindo os anos inicial e final.
conditions = df.query('yr_built >= 1969 and yr_built <= 1974 and waterfront == 1').shape[0]
print(f"{conditions} casas à beira-mar foram construídas durante a presidência de Nixon (1969—1974)")
# Q13.2 Quantas casas, construídas antes do primeiro ser humano no espaço (< 1961), têm boas condições (= 5)?
print("{} casas foram construidas antes do primeiro ser humano no espaço".format(df.query("yr_built < 1961 and condition == 5").shape[0]))
# Q13.3 Quantas casas têm 6 quartos e menos de 2.000 pés quadrados de área útil?
print("{} casas têm 6 quartos e menos de 2.000 pés quadrados de área útil".format(df.query("bedrooms == 6 and sqft_living < 2000").shape[0]))
# Q13.4 Qual era o preço de uma casa com 5 casas de banho, construída em 1998 e com nota 10?
print("O preço de uma casa com 5 casas de banho, construída em 1998 e com nota 10 é ${}".format(df.query("bathrooms == 5 and yr_built == 1998 and grade == 10")["price"].values[0]))
# Q13.5 Quantos andares tem uma casa construída em 1999 com 5 quartos e 3400 pés quadrados de área útil?
"Uma casa construída em 1999 com 5 quartos e 3400 pés quadrados de área tem {} andares".format(df.query("yr_built == 1999 and bedrooms == 5 and sqft_living == 3400")["floors"].values[0])

# Usando máscara ou a sintaxe .query, selecione linhas/colunas e calcule estatísticas simples (float)

# Q14.1 Qual foi o preço médio (vendido) de uma casa construída no ano da Crise dos Mísseis de Cuba (1962)?
print("O preço médio (vendido) de uma casa construída no ano da Crise dos Mísseis de Cuba (1962) é ${:,.2f}".format(df.query("yr_built == 1962")["price"].mean()))
# Q14.2 Qual foi o preço da casa mais cara vendida, construída entre 1991 e 2000?
print("O preço da casa mais cara vendida, construída entre 1991 e 2000 é ${:,.2f}".format(df.query("yr_built >= 1991 and yr_built <= 2000")["price"].max()))
# Q14.3 Qual foi o preço da casa mais barata vendida, construída entre 1991 e 2000?
print("O preço da casa mais cara vendida, construída entre 1991 e 2000 é ${:,.2f}".format(df.query("yr_built >= 1991 and yr_built <= 2000")["price"].min()))
# Q14.4 Qual é a mediana do número de casas de banho em habitações com nota superior a 9 (10 e superior)?
print("A mediana do número de casas de banho em habitações com nota superior a 9 é {}".format(df.query("grade > 9")["bathrooms"].median()))
# Q14.5 Qual é a classificação média das casas com o valor do código postal mais popular?
zipcode = df["zipcode"].value_counts(0).idxmax()
print("A classificação média das casas com o valor do código postal mais popular é {:.2f}".format(df.query("zipcode == @zipcode")["grade"].mean()))


# ##Criando novas colunas
# 
# Criar uma nova coluna de pandas.DataFrame é tão fácil quanto:
# ```
# dados['nova_coluna'] = []
# ```
# é isso. Mas tal coluna é relativamente inútil. Normalmente, você calcularia algo novo com base nos dados existentes e salvaria em uma nova coluna. Por exemplo, pode-se querer calcular a área total da casa como uma soma de todas as colunas `sqft_` ou criar uma coluna booleana se a casa tiver `grade` > 2 ou qualquer outra coisa:
# 
# ```
# dados['area_total'] = dados[col1] + dados[col2] + ...
# dados['alto_valor'] = dados[col] > 5
# ```
# 
# O Pandas também fornece outra ferramenta poderosa: os métodos `.apply`, `.map()`, `.applymap()` (eles são quase iguais, mas não exatamente). https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas . Eles permitem que você aplique alguma função a cada valor na(s) coluna(s) (no sentido da linha) ou linha (no sentido da coluna) ou célula (no sentido do elemento). Por exemplo, os mesmos cálculos de `area_total` e `alto_valo` usando `.apply()`:
# ```
# dados['area_total'] = dados[[col1, col2, col3]].apply(sum, axis=1)
# ```
# você não está restrito a funções existentes, `.apply()` aceita qualquer função (incluindo funções lambda):
# ```
# dados['area_total'] = dados[[col1, col2, col3]].apply(lambda x: x[0]+x[1]+x[2], axis=1)
# ```
# ou uma função python comum (se o valor tiver um comportamento complexo):
# ```
# def _soma(x):
#      total = 0
#      para elem em x:
#          total += elemento
#      retorno total
# 
# data['area_total'] = data[[col1, col2, col3]].apply(_soma, axis=1)
# ```
# Muitos métodos pandas têm o parâmetro `axis`, com `axis = 0` referindo-se a linhas, `axis = 1` referindo-se a colunas.
# 
# **Aviso:** *Você nunca deve usar loops for para somar elementos numéricos do contêiner.*

# Crie a coluna `foi_reformada`. Coluna Bool (0, 1) indicando se a casa foi reformada.
df["foi_reformada"] = df["yr_renovated"].apply(lambda x: 1 if x > 0 else 0)

# Crie novas colunas usando as antigas (nova coluna no seu DataFrame)

# Q15.1 Crie uma coluna `area_total_sqft` (soma de todas as colunas com o prefixo `sqft_`) usando qualquer método acima
sqft_columns = []
for column in df.columns:
    if column.startswith("sqft_"):
        sqft_columns.append(column)
df["area_total_sqft"] = df[sqft_columns].apply(sum, axis=1)
# Q15.2 Crie uma nova coluna `area_total_sqm` usando `area_total_sqft` e o fato de que 1 pé(ft) = 0,3048 metros
df["area_total_sqm"] = df["area_total_sqft"].apply(lambda x: x * 0.3048)
# Q15.3 Crie uma nova coluna `area_útil_media_sqm` dividindo a área total (em metros) pelo número de andares
df["area_útil_media_sqm"] = df["area_total_sqm"] / df["floors"]
# Q15.4 Crie uma nova coluna `cat_preco` dividindo cada `price` em 5 ([1..5]) intervalos distintos: 0 < x <=20%,
#       20% < x <= 40%, ... 80% < x <= 100% percentis. Você pode usar `.quantile()` para calcular percentis.

# Calculate the percentiles of the `price` column
percentiles = df["price"].quantile([0, 0.2, 0.4, 0.6, 0.8, 1])

# Create a function to map the price to its category
def map_price_to_category(price):
    if price <= percentiles[0.2]:
        return 1
    elif price <= percentiles[0.4]:
        return 2
    elif price <= percentiles[0.6]:
        return 3
    elif price <= percentiles[0.8]:
        return 4
    else:
        return 5

# Apply the function to create the new `cat_preco` column
# Não entendi o que é para fazer
# Q15.5 Crie uma nova coluna bool `classe_alta` que é True se a casa tiver nota >= 9 e condição >= 4
df["classe_alta"] = df.apply(lambda x: True if x["grade"] >= 9 and x["condition"] >= 4 else False, axis=1)
# Usando máscara ou sintaxe .query, selecione linhas/colunas (float)

# Q16.1 Qual é o preço médio da casa de classe_alta(=True)?
df.query("classe_alta == True")["price"].mean()
# Q16.2 Qual é a média total_area (em metros) da casa da categoria de preço mais alto?
max_price = df["price"].value_counts().idxmax()
df.query("price == @max_price")["area_total_sqm"].mean()
# Q16.3 Qual é o número máximo de andares entre as casas com a categoria de preço mais baixo?
min_price = df["price"].value_counts().idxmin()
df.query("price == @min_price")["floors"].max()
# Q16.4 Qual é o CEP (zipcode) mais frequente entre as casas com a categoria de preço mais baixo?
df.query("price == @min_price")["zipcode"].value_counts().idxmax()
# Q16.5 Qual é o número mínimo de banheiros em casas com classe_alta=True?
df.query("classe_alta == True")["bathrooms"].min()
# ## Processamento básico de data
# Você descobriu que a coluna `date` é muito difícil para manipular, então decidiu convertê-la em um formato mais fácil:
# 
# - Use o método `to_datetime()` do pandas para converter a data em um bom formato.
# - Extraia `year`, `month`, `day` e `weekday` (dia da semana) de sua nova coluna de data. Salve-os em colunas separadas.
# - Quantas colunas tem seus dados agora?
# - Apague a coluna `date`, e lembre-se de definir o parâmetro `inplace` como True.
# 
# **Dica:** para data formatada você pode extrair o `year` da seguinte forma:
# ```
# data.data.dt.ano
# ```
# Muitas vezes, a data pode ser um recurso ridiculamente rico, às vezes são os feriados que importam, às vezes os fins de semana, às vezes alguns dias especiais como a **black friday**.
# 
# Aprenda a trabalhar com datas em Python

# Cria novas colunas com base na coluna `date`
# Q17.1 Converta date para formato de data e hora
df["date"] = pd.to_datetime(df["date"])
# Q17.2 Extraia e armazene `year`
df["year"] = df["date"].dt.year
# Q17.3 Extraia e armazene `month`
df["month"] = df["date"].dt.month
# Q17.4 Extraia e armazene `day`
df["day"] = df["date"].dt.day
# Q17.5 Extraia e armazene `weekday`
df["weekday"] = df["date"].dt.weekday
# Q17.6 Crie uma nova coluna `idade_casa_10` - a idade da casa em décadas completas (por exemplo, casa de 9 anos - 0, casa de 21 anos - 2),
df["idade_casa_10"] = df["yr_built"].apply(lambda x: x // 10)
# usando as colunas `yr_built` e 'year'

# Apague a coluna `date`
df.drop("date", axis=1, inplace=True)
# Encontre alguma informação relacionada à data dos dados (int, domingo tem índice 0)


# Q18.1 Qual é o dia da semana mais vendido?
df["weekday"].value_counts().idxmax()
# Q18.2 Qual é o mês de vendas mais popular?
df["month"].value_counts().idxmax()
# Q18.3 Qual é o dia da semana de venda menos popular?
df["weekday"].value_counts().idxmin()
# Q18.4 Qual é a idade mediana da casa (na primeira data de venda disponível)? (float)
df["house_age"] = df["year"] - df["yr_built"]
df["house_age"].median()
# Q18.5 Quantas casas foram vendidas no Dia da Independência dos Estados Unidos (4 de julho)?
df.query("month == 7 and day == 4")["price"].count()
# ## Agrupar por (Groupby)
# 
# A parti da documentação https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
# 
# Por “agrupar por” nos referimos a um processo que envolve uma ou mais das seguintes etapas:
# 
#     - Divisão dos dados em grupos com base em alguns critérios.
#     - Aplicando uma função a cada grupo de forma independente.
#     - Combinando os resultados em uma estrutura de dados.
# ---
# `.groupby()` é uma das ferramentas mais poderosas para engenharia de recursos. Muitas vezes, é usado para agrupar objetos com as mesmas características categóricas e calcular algumas estatísticas (por exemplo, média, máximo, etc.) de suas características numéricas.
# 
# Em vez de calcular a área média das casas com alto grau, você pode calcular as áreas médias das casas para cada grau em um único comando:
# ```
# `data.groupby('grade')['sqm_tot_area'].mean()`
# ```
# Você também pode criar grupos com várias colunas:
# 
# ```
# data.groupby(['dia da semana','nota'])['preço'].min()
# ```
# 
# em seguida, você pode calcular várias funções de agregação:
# ```
# data.groupby(['dia da semana','nota'])['preço'].agg([min, max])
# ```
# em vez de usar funções internas, você pode calcular funções personalizadas usando apply:
# ```
# import numpy as np
# dados.groupby(['condition','grade'])['bathrooms'].apply(lambda x: np.quantile(x, .5))
# ```
# 
# e o mais legal agora é que você pode mapear os resultados do groupby de volta no seu DataFrame!
# ```
# grupo = dados.groupby(['condition'])['bathrooms'].median()
# dados['feature_grupo'] = dados['condition'].map(grupo)
# ```
# Agora, se alguma casa tiver `condição == 2`, seu `feature_grupo` será igual ao número médio de banheiros entre todas as casas com `condição == 2`.
# 
# Leia mais exemplos na documentação https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

# Crie alguns recursos de agrupamento

# Q19.1 `preco_por_classe` agrupado por `classe_alta` e calcula o `price` mediano.
preco_por_classe = df.groupby("classe_alta")["price"].median()
# Q19.2 `preco_por_+ano` agrupa por `year` e calcula o preço mediano.
preco_por_ano = df.groupby("year")["price"].median()
# Q19.3 `preco_por_dia_semana` agrupa por `weekday` e calcula o preço mediano.
preco_por_dia_semana = df.groupby("weekday")["price"].median()
# Q19.4 `area_por_preco` agrupado por `price_cat` e calcula a média `sqft_living`.
# area_por_preco = df.groupby("price_cat")["sqft_living"].mean() # "price_cat" não existe
# Q19.5 `andares_por_idade` agrupa por `floors` e calcula a idade média de uma casa.
andares_por_idade = df.groupby("floors")["house_age"].mean()

# Crie alguns outros recursos de agrupamento
# para esta tarefa confira esta resposta:
# https://stackoverflow.com/questions/47913343/how-to-groupby-and-map-by-two-columns-pandas-dataframe

# Q20.1 `n_casas_CEP` agrupa por `zipcode` e conta o número de ocorrências de cada CEP único
n_casas_CEP = df.groupby("zipcode")["zipcode"].count()
# Q20.2 `n_casas_ano_construcao` agrupado por `yr_built` e conta o número de casas construídas em cada ano
n_casas_ano_construcao = df.groupby("yr_built")["yr_built"].count()
# Q20.3 `preco_por_ano_mes_`(mediana, desvio) agrupado por `year`, `month` e calcula mediana e desvio padrão de `price`.
preco_por_ano_mes_ = df.groupby(["year", "month"])["price"].agg([np.median, np.std])
# Q20.4 `preco_por_grade_idade_`(mediana, desvio) agrupado por `grade`, `house_age` e calcula mediana e desvio padrão de `price`.
preco_por_grade_idade_ = df.groupby(["grade", "house_age"])["price"].agg([np.median, np.std])
# Q20.5 `living_por_cond_`(mediana, desvio) agrupado por `waterfront`, `view`, `condição` e calcula mediana e desvio padrão de `sqft_living`.
living_por_cond_ = df.groupby(["waterfront", "view", "condition"])["sqft_living"].agg([np.median, np.std])


