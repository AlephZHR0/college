# Documentação do Jogo "Reconquista"

## 1. Definição do Conceito

### Ideia Central
Criar um jogo de estratégia abstrato para dois jogadores em dispositivos de computador, combinando elementos de Onitama e Xadrez com mecânicas inovadoras. A história envolve uma guerra antiga onde dois territórios, A e B, se conquistaram mutuamente e agora buscam reconquistar suas terras natais.

### Gênero
- Estratégia Abstrata
- Turno-based
- Jogo de Tabuleiro Digital

### Temática
Reconquista de território em um mundo pós-guerra. Os mestres do time inimigo possuem a chave do templo local. O time A possui a chave do templo B e vice-versa. O objetivo é fazer com que dois líderes cheguem ao templo inimigo para provar sua superioridade e retomar sua terra de direito.

### Público-Alvo
Jogadores de jogos de tabuleiro estratégicos, familiarizados com jogos como Xadrez, Damas e Onitama, que buscam partidas rápidas e desafiadoras em dispositivos de computador.

### Resumo do Conceito
Em "Reconquista", dois jogadores lideram seus exércitos (Mestres e Aprendizes) em um tabuleiro 5x5, utilizando cartas de movimento para comandar suas peças. O objetivo é eliminar as peças inimigas ou conduzir seus dois Mestres aos santuários inimigos. A mecânica de troca de cartas, a informação aberta (cartas do oponente visíveis) e a ascensão dos Aprendizes a Mestres adicionam profundidade estratégica e imprevisibilidade à experiência.

## 2. Elaboração do GDD (Game Design Document)

### Visão Geral

**Título do Jogo:** "Reconquista"

**Gênero:** Estratégia Abstrata, Turno-based, Jogo de Tabuleiro Digital

**Plataforma:** Computador

**Público-Alvo:** Jogadores de jogos de tabuleiro estratégicos que buscam partidas rápidas e desafiadoras

### Mecânicas

**Tabuleiro:** Grade digital 5x5, com casas alternadas em cores creme e marrom.

**Peças:**
- **Mestres:** 2 por jogador, representados por círculos brancos ou pretos com base verde ou vermelha (distinguindo os jogadores). A distinção de cor é crucial para facilitar a semiótica, ajudando os jogadores a reconhecerem quais mestres e aprendizes estão ligados.
- **Aprendizes:** 2 por jogador, representados por círculos da mesma cor do Mestre, mas em tom mais claro, com base da mesma cor do Mestre. Aprendizes são promovidos a Mestres quando o Mestre é capturado ou chega ao santuário inimigo.

**Cartas de Movimento:** 16 cartas únicas, sem repetição, com fundo creme e detalhes marrom, exibindo um padrão de movimento (frente e trás) e o nome de um animal. Cada jogador possui duas cartas em mãos e há duas cartas no centro do tabuleiro. Após usar uma carta, o jogador deve trocá-la por uma das cartas do centro.
- Exemplos:
  - **Carta "Águia":** Movimento duas casas para frente ou uma casa para trás na diagonal.
  - **Carta "Serpente":** Movimento em "L", uma casa para frente e duas para o lado, ou o inverso para trás.

**Santuários:** Casas no fundo do tabuleiro inimigo, seguras para os Mestres (peças inimigas não podem entrar).

**Tempo:**
- **Tempo Total de Jogo:** 5 minutos por jogador.
- **Timer por Jogada:** 30 segundos, com penalidade de perda da vez caso o tempo se esgote.
- **Incremento por Jogada:** 2 segundos adicionados ao tempo total do jogador após cada jogada concluída.

### Regras

**Disposição Inicial:**
- Cada jogador começa com suas peças dispostas na linha mais próxima a eles.
- A disposição das peças é a seguinte (do canto esquerdo ao direito): Aprendiz, Mestre, casa vazia, Mestre, Aprendiz.
- As casas dos santuários ficam localizadas atrás dos Mestres.

**Turno:** Jogadores alternam turnos, realizando as ações de seleção de carta, seleção de peça, movimento e troca de cartas.

**Movimento:** As peças se movem de acordo com o padrão da carta selecionada.

**Captura:** Uma peça captura a inimiga ao ocupar a casa onde ela está.

**Ascensão do Aprendiz:** Um Aprendiz é promovido a Mestre quando seu Mestre original é capturado ou chega ao santuário inimigo.

**Condições de Vitória:**
- Eliminar todas as peças do oponente.
- Posicionar seus dois Mestres nos santuários inimigos.

### Dinâmicas

- **Estratégia e Planejamento:** O jogo incentiva o pensamento estratégico, a antecipação das jogadas do oponente e a gestão do tempo.
- **Informação Aberta:** As cartas do oponente são visíveis, permitindo blefe e leitura do jogo.
- **Controle de Território:** Dominar o centro do tabuleiro e capturar peças são elementos estratégicos importantes.
- **Gerenciamento de Risco:** Avançar os Mestres para os santuários envolve risco e recompensa.
- **Adaptação:** A aleatoriedade das cartas exige adaptação constante.

### Estética

**Visual:**
- **Paleta de cores:** tons de creme, marrom, branco, preto, verde, vermelho, rosa e roxo.
- **Estilo:** minimalista e clássico.

**Música:** Trilha sonora instrumental relaxante durante a partida e efeito sonoro especial para a vitória.

### Interface

**Disposição da tela:** Conforme descrito na seção "Visão Geral".

**Elementos:**
- **Botões:** “Iniciar Jogo”, “Pausar”, “Reiniciar”.
- **Indicador de Turno:** LED luminoso no canto da tela, indicando o jogador da vez.
- **Contador de Tempo:** Exibe o tempo restante do jogador em segundos.
- **Cartas de Movimento:** Exibem o nome do animal e o padrão de movimento.
- **Tabuleiro:** Exibe as peças e os santuários.
- **Área de Peças Capturadas:** Exibe miniaturas das peças capturadas por cada jogador.

**Interação:**
- Cliques do mouse para selecionar cartas, peças e casas de destino.

## 3. Prototipagem

**Ferramenta:** Utilizar o Pygame para criar um protótipo digital interativo.

**Objetivo:** Testar as mecânicas, a interface, o sistema de tempo, e a experiência do jogador.

**Etapas:**
1. Criar os assets básicos: tabuleiro, peças, cartas.
2. Implementar as regras do jogo: movimento, captura, ascensão do Aprendiz, condições de vitória.
3. Criar a interface do usuário: botões, indicadores, contadores, etc.
4. Implementar o sistema de tempo: relógio de jogo e timer por jogada.

**Playtests:**
- Convidar amigos, familiares e outros jogadores para testar o protótipo.
- Coletar feedback sobre a jogabilidade, a interface, a dificuldade, a diversão e o tempo de jogo.
- Ajustar o protótipo com base no feedback recebido.

## 4. Desenvolvimento

**Linguagem de Programação:** Python.

**Biblioteca:** Pygame.

**Ferramentas:** Pygame para desenvolvimento do jogo.

### Etapas:

1. Criar a estrutura do projeto: definir classes, pacotes e organização do código.
   - Exemplo de estrutura de classes:
     ```python
     # Classe para representar uma carta de movimento
     class Carta:
         def __init__(self, nome, movimentos):
             self.nome = nome
             self.movimentos = movimentos

     # Classe para representar uma peça no tabuleiro
     class Peca:
         def __init__(self, tipo, jogador):
             self.tipo = tipo
             self.jogador = jogador

     # Classe para representar o tabuleiro
     class Tabuleiro:
         def __init__(self):
             self.casas = [[None for _ in range(5)] for _ in range(5)]

     # Classe principal do jogo
     class Reconquista:
         def __init__(self):
             self.tabuleiro = Tabuleiro()
             # Lógica do jogo...
     ```

2. Implementar as mecânicas do jogo: traduzir as regras definidas no GDD para código.
   - Exemplo de código:
     ```python
     # Função para mover uma peça no tabuleiro
     def mover_peca(tabuleiro, peca, destino):
         # Verificar se o movimento é válido...
         # Atualizar a posição da peça no tabuleiro...
         # Retornar o tabuleiro atualizado
         pass
     ```

3. Criar os assets finais: arte das cartas, peças, tabuleiro, interface, efeitos sonoros.

4. Integrar a interface do usuário: conectar os elementos visuais com a lógica do jogo.

5. Implementar o sistema de tempo: integrar o relógio de jogo e o timer por jogada.

### Testes:

- Realizar testes unitários para validar o código.
- Realizar testes de integração para garantir que os diferentes módulos do jogo funcionem em conjunto.
- Realizar testes de usabilidade para garantir que a interface seja intuitiva e fácil de usar.

## 5. Lançamento

**Plataformas:** Computador (Windows, MacOS, Linux)

**Modelo de Negócios:** Free-to-play, com compras dentro do aplicativo (remoção de anúncios).

## 6. Manutenção

**Monitoramento:**
- Acompanhar as avaliações e comentários dos jogadores nas plataformas de distribuição.
- Utilizar ferramentas de análise para coletar dados sobre o uso do jogo: número de jogadores, tempo de jogo, compras, etc.

**Atualizações:**
- Corrigir bugs e erros reportados pelos jogadores.
- Melhorar o balanceamento do jogo.
- Adicionar novos conteúdos: cartas de movimento, modos de jogo, desafios, etc.
- Adaptar o jogo às novas versões dos sistemas operacionais.
