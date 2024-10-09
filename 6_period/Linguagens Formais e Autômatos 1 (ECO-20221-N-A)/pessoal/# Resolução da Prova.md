# Resolução da Prova

## Questão 1

Considerando o alfabeto:
\[
\Sigma = \{\text{verde}, \text{amarelo}, \text{azul}, \text{branco}\}
\]

Precisamos determinar o comprimento (número de símbolos) de cada palavra fornecida. Aqui, cada símbolo é uma cor específica do alfabeto.

### a) \(|\text{branco}| =\)

A palavra "branco" é um símbolo único no alfabeto \(\Sigma\).

**Resposta:**
\[
|\text{branco}| = 1
\]

### b) \(|\text{azulamareloverde}| =\)

A palavra "azulamareloverde" pode ser decomposta nos símbolos do alfabeto:
\[
\text{azul} \quad \text{amarelo} \quad \text{verde}
\]
Isso totaliza 3 símbolos.

**Resposta:**
\[
|\text{azulamareloverde}| = 3
\]

### c) \(|\varepsilon| =\)

\(\varepsilon\) representa a palavra vazia, que não contém símbolos.

**Resposta:**
\[
|\varepsilon| = 0
\]

### d) \(|\text{azulverde}| =\)

A palavra "azulverde" pode ser decomposta em:
\[
\text{azul} \quad \text{verde}
\]
Totalizando 2 símbolos.

**Resposta:**
\[
|\text{azulverde}| = 2
\]

---

## Questão 2

Considerando o alfabeto:
\[
\Sigma = \{0, 1\}
\]

E as palavras:
\[
x = 0101 \quad y = 10101
\]

Vamos realizar as operações solicitadas.

### a) \(xy =\)

Concatenamos \(x\) e \(y\):
\[
xy = 0101 \, 10101 = 010110101
\]

**Resposta:**
\[
xy = 010110101
\]

### b) \(x^2 =\)

Elevando \(x\) ao quadrado (concatenando \(x\) com ele mesmo):
\[
x^2 = x \, x = 0101 \, 0101 = 01010101
\]

**Resposta:**
\[
x^2 = 01010101
\]

### c) \(\varepsilon y =\)

Concatenando a palavra vazia \(\varepsilon\) com \(y\):
\[
\varepsilon y = \varepsilon \, y = y = 10101
\]

**Resposta:**
\[
\varepsilon y = 10101
\]

### d) \(y^0 =\)

Qualquer palavra elevada a zero resulta na palavra vazia \(\varepsilon\).

**Resposta:**
\[
y^0 = \varepsilon
\]

---

## Questão 3

### Autômato Finito para \(L(M1)\)

**Definição da Linguagem:**
\[
L(M1) = \{ w \in \{0,1\}^* \mid w \text{ é a cadeia vazia ou termina com } 0 \}
\]

**Construção do Autômato:**

**Estados:**
- \(q_0\): Estado inicial e de aceitação.
- \(q_1\): Estado não final.

**Alfabeto:**
\[
\Sigma = \{0, 1\}
\]

**Funções de Transição:**

- Do estado \(q_0\):
  - Com entrada \(0\), permanece em \(q_0\).
  - Com entrada \(1\), transita para \(q_1\).

- Do estado \(q_1\):
  - Com entrada \(0\), transita para \(q_0\).
  - Com entrada \(1\), permanece em \(q_1\).

**Diagrama do Autômato:**

```
 [q0] --0--> [q0]
  |          |
 1|          |1
  v          v
 [q1] <--0-- [q0]
```

**Descrição:**

- O estado \(q_0\) é tanto inicial quanto de aceitação, permitindo que a palavra vazia \(\varepsilon\) seja aceita.
- Se a palavra termina com \(0\), o autômato estará em \(q_0\) após processar a entrada, portanto, será aceita.
- Se a palavra termina com \(1\), o autômato estará em \(q_1\), que é um estado não final, portanto, a palavra será rejeitada.

---

## Questão 4

### Autômato Finito para \(L(M2)\)

**Definição da Linguagem:**
\[
L(M2) = \{ w \in \{a,b\}^* \mid |w| > 0 \text{ e } w \text{ começa e termina com o mesmo símbolo} \}
\]

**Construção do Autômato:**

**Estados:**
- \(q_0\): Estado inicial.
- \(q_1\): Iniciou com 'a', último símbolo lido foi 'a' (estado de aceitação).
- \(q_2\): Iniciou com 'a', último símbolo lido foi 'b'.
- \(q_3\): Iniciou com 'b', último símbolo lido foi 'b' (estado de aceitação).
- \(q_4\): Iniciou com 'b', último símbolo lido foi 'a'.

**Alfabeto:**
\[
\Sigma = \{a, b\}
\]

**Funções de Transição:**

- Do estado \(q_0\):
  - Com entrada \(a\), transita para \(q_1\).
  - Com entrada \(b\), transita para \(q_3\).

- Do estado \(q_1\):
  - Com entrada \(a\), permanece em \(q_1\).
  - Com entrada \(b\), transita para \(q_2\).

- Do estado \(q_2\):
  - Com entrada \(a\), retorna para \(q_1\).
  - Com entrada \(b\), permanece em \(q_2\).

- Do estado \(q_3\):
  - Com entrada \(b\), permanece em \(q_3\).
  - Com entrada \(a\), transita para \(q_4\).

- Do estado \(q_4\):
  - Com entrada \(b\), retorna para \(q_3\).
  - Com entrada \(a\), permanece em \(q_4\).

**Estados de Aceitação:**
- \(q_1\) e \(q_3\)

**Diagrama do Autômato:**

```
          a           a
       +----+      +----+
       |    |      |    |
       v    |      |    v
     [q1] --b--> [q2]
      ^          |
      |          b
      |          v
[q0] -a-> [q1]   [q2]
 |              ^
b|              |
 v              |
[q3] --a--> [q4]
       |          ^
       b          |
       |          |
       +----------+
```

**Descrição:**

- O autômato distingue se a palavra inicia com 'a' ou 'b' e rastreia o último símbolo lido.
- Estados \(q_1\) e \(q_3\) são de aceitação e representam palavras que começam e terminam com o mesmo símbolo.
- O autômato rejeita a palavra vazia, pois não há transição do estado inicial \(q_0\) sem consumir um símbolo.

---

**Conclusão:**

As questões abordam conceitos fundamentais de Teoria da Computação, incluindo o cálculo do comprimento de palavras, operações com palavras, e a construção de autômatos finitos para reconhecer linguagens específicas. A compreensão desses conceitos é essencial para o estudo de linguagens formais e autômatos.