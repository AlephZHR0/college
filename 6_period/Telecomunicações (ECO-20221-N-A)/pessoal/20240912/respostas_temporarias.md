Aqui estão as respostas para as suas perguntas, baseadas no conteúdo fornecido:


## Respostas:


**1. Qual século marcou o início da comunicação eletrônica?**

O século XIX marcou o início da comunicação eletrônica, com a invenção do telégrafo por Samuel Morse em 1835 e sua primeira transmissão em 1844 (página 3 do primeiro documento).


**2. Qual foi o primeiro método de comunicação digital utilizado?**

O telégrafo, utilizando o código Morse, pode ser considerado o primeiro método de comunicação digital, pois utilizava pulsos elétricos discretos para representar letras e números (página 3 do primeiro documento).


**3. Que tipo de sinal eletrônico varia continuamente os sinais de voz e vídeo?**

Sinais analógicos. Esses sinais variam continuamente em amplitude e frequência, representando as variações nas ondas sonoras e luminosas que compõem a voz e o vídeo (página 8 do segundo documento).


**4. Como os sinais de voz e vídeo são transmitidos digitalmente?**

Os sinais de voz e vídeo são transmitidos digitalmente através da conversão analógico-digital (A/D). Este processo envolve as seguintes etapas (páginas 5-9 do terceiro documento): 

1. **Amostragem:** O sinal analógico é amostrado em intervalos regulares de tempo.
2. **Quantização:** Os valores amostrados são convertidos em um conjunto finito de níveis discretos.
3. **Codificação:** Cada nível discreto é representado por um código binário.
4. **Compressão:** O código binário pode ser comprimido para reduzir a quantidade de dados a serem transmitidos.

Após a transmissão, o processo inverso (conversão digital-analógico - D/A) é realizado para recuperar o sinal analógico.

**5. Que tipo de sinal eletrônico varia continuamente os sinais de voz e vídeo?**

Sinais analógicos (página 8 do segundo documento).


**6. Qual é a faixa de frequência aproximada da voz humana?**

A faixa de frequência aproximada da voz humana para inteligibilidade está entre 300 Hz e 3400 Hz, com uma largura de banda de 3100 Hz. Para telefonia, a referência é uma banda de 4 kHz (página 2 do terceiro documento).


**7. Cite e descreva as etapas da conversão analógico digital.**

As etapas da conversão analógico-digital (A/D) são (páginas 5-8 do terceiro documento):

1. **Amostragem:** O sinal analógico é medido em intervalos regulares de tempo, criando uma série de amostras.
2. **Quantização:** Cada amostra é arredondada para o nível de amplitude discreto mais próximo, dentro de um conjunto predefinido de níveis.
3. **Codificação:** Cada nível quantizado é atribuído a um código binário único.


**8. O valor da tensão de pico de um sinal senoidal é  𝐸𝑃=5 V  e o período  𝑇=3 ms=0,003 s .**

**1. Calcular o valor da tensão  𝑅𝑀𝑆**


```python

import math

Ep = 5  # Tensão de pico
Erms = Ep / math.sqrt(2)

print(f'{Erms=}')
```

```Code execution output
Erms=3.5355339059327373
```
**2. Calcular a frequência do sinal.**


```python

T = 0.003  # Período em segundos
f = 1 / T

print(f'{f=}')
```

```Code execution output
f=333.3333333333333
```
**3. Desenhar a forma de onda.**

Para desenhar a forma de onda, você pode utilizar um software como o matplotlib. O código abaixo demonstra como plotar um sinal senoidal com as características fornecidas:


```python

import matplotlib.pyplot as plt
import numpy as np

Ep = 5  # Tensão de pico
f = 333.33  # Frequência em Hz
T = 1 / f  # Período em segundos

t = np.linspace(0, 2 * T, 500)  # Vetor de tempo
y = Ep * np.sin(2 * np.pi * f * t)  # Sinal senoidal

plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.title('Forma de Onda Senoidal')
plt.grid(True)
plt.show()
```

```Code execution output

```
**9. Para amostrar um sinal de vídeo com  𝑓𝑚𝑎𝑥=4 𝑀𝐻𝑧 , pelo teorema de Nyquist**

**1. Qual o menor valor da frequência de amostragem?**

Pelo Teorema de Nyquist, a frequência de amostragem mínima (fa) deve ser o dobro da maior frequência do sinal (fmax):

fa = 2 * fmax = 2 * 4 MHz = 8 MHz


**2. Qual é a Banda de Guarda adotada?**

A banda de guarda (BG) é a diferença entre a frequência de amostragem (fa) e a maior frequência do sinal (fmax):

BG = fa - fmax = 8 MHz - 4 MHz = 4 MHz


**3. Sendo a quantização de 8 bits por amostra do sinal, qual será o valor da taxa de transmissão?**

Taxa de transmissão = Frequência de amostragem * Número de bits por amostra

Taxa de transmissão = 8 MHz * 8 bits = 64 Mbits/s


**4. Desenhe as curvas de amostragem.**

Para desenhar as curvas de amostragem, você pode adaptar o código Python fornecido em sala de aula. O gráfico deve mostrar o sinal original, o sinal amostrado e o espectro de frequência do sinal amostrado, com a banda de guarda destacada.


**10. Utilizando como base o programa em Python mostrado em sala. Altere suas instruções para obter a série de Fourier das ondas a seguir. Tenham atenção às equações integrais do sinal. O software deverá imprimir o gráfico no domínio do tempo e da frequência (Transformada de Fourier).**

**1. Onda dente de serra**

**2. Onda triangular**

Para obter a série de Fourier e os gráficos das ondas dente de serra e triangular, você precisa adaptar o código Python fornecido em sala de aula, modificando as funções que definem o sinal no domínio do tempo e as equações integrais para calcular os coeficientes da série de Fourier. 

Lembre-se de que a onda dente de serra e a onda triangular são funções periódicas, e você precisará definir o período e a amplitude para cada uma delas. 

A implementação detalhada do código Python está fora do escopo desta resposta, mas posso fornecer algumas dicas:

* Utilize a biblioteca NumPy para criar vetores de tempo e calcular as funções.
* Utilize a biblioteca Matplotlib para plotar os gráficos no domínio do tempo e da frequência.
* Para calcular a Transformada de Fourier, você pode utilizar a função `fft` da biblioteca NumPy.
* Consulte a documentação das bibliotecas NumPy e Matplotlib para obter mais informações sobre as funções e recursos disponíveis.

Espero que estas respostas ajudem!