from typing import Tuple, List
from primePy import primes
from random import choice

LISTA_PRIMOS = None


def gerar_numero_primo_aleatorio_entre(a: int = 10, b: int = 100) -> int:
    global LISTA_PRIMOS
    if not LISTA_PRIMOS:
        LISTA_PRIMOS = primes.between(a, b)
    primo_aleatorio = choice(LISTA_PRIMOS)
    return primo_aleatorio


def verificar_se_numero_e_primo(num: int) -> bool:
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def encontrar_maior_divisor_comum(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def encontrar_inverso_multiplicativo(e: int, phi: int) -> int:
    def maior_Divisor_Comum_estendido(a: int, b: int) -> tuple:
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = maior_Divisor_Comum_estendido(b % a, a)
            return (g, y - (b // a) * x, x)

    g, x, _ = maior_Divisor_Comum_estendido(e, phi)
    if g != 1:
        raise Exception('Inverso modular não existe')
    else:
        return x % phi


def gerar_par_chaves(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (verificar_se_numero_e_primo(p) and verificar_se_numero_e_primo(q)):
        raise ValueError('Ambos os números devem ser primos.')
    elif p == q:
        raise ValueError('p e q não podem ser iguais')
    # n é o módulo para as chaves pública e privada
    n: int = p * q

    # Phi é o totiente de n (Euler)
    phi: int = (p-1) * (q-1)

    for e in [3, 65537]:
        if encontrar_maior_divisor_comum(e, phi) == 1:
            break
    else:
        raise ValueError('Nenhum valor adequado de e encontrado.')

    # Algoritmo de Euclides Estendido para gerar a chave privada
    d: int = encontrar_inverso_multiplicativo(e, phi)

    # Retornar o par de chaves pública e privada
    return ((e, n), (d, n))


def criptografar_mensagem(public_key: Tuple[int, int], texto_claro: str) -> List[int]:
    chave, n = public_key
    cifra = [(ord(char) ** chave) % n for char in texto_claro] # ord() retorna um inteiro representando o caractere Unicode
    return cifra



def descriptografar_mensagem(private_key: Tuple[int, int], texto_cifrado: List[int]) -> str:
    chave, n = private_key
    texto_claro = [chr((char ** chave) % n) for char in texto_cifrado] # chr() retorna uma string representando um caractere cujo ponto de código Unicode é o inteiro
    return ''.join(texto_claro)


def converter_para_string(lst):
    return ''.join(map(str, lst)) # map() retorna um iterador que aplica a função a cada item iterável, produzindo os resultados


limite_min = 1000
limite_max = 10000

p = gerar_numero_primo_aleatorio_entre(limite_min, limite_max)
print("p:", p)
q = gerar_numero_primo_aleatorio_entre(limite_min, limite_max)
print("q:", q)

while p == q:
    q = gerar_numero_primo_aleatorio_entre(limite_min, limite_max)

publico, privado = gerar_par_chaves(p, q)

print(f"""Chave privada:
    d: {privado[0]}
    n: {privado[1]}""")

print(f"""Chave pública: 
    e: {publico[0]}
    n: {publico[1]}""")

mensagem = "Budaibes é um lindo!"

mensagem_cifrada = criptografar_mensagem(publico, mensagem)

print("Mensagem cifrada:", converter_para_string(mensagem_cifrada))

mensagem_descriptografada = descriptografar_mensagem(privado, mensagem_cifrada)
print("Mensagem descriptografada:", mensagem_descriptografada)
