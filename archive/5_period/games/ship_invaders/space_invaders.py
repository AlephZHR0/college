import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações da tela
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Limites verticais do mar
PLAYER_SEA_TOP_LIMIT = 210
PLAYER_SEA_BOTTOM_LIMIT = 760
ENEMY_SEA_TOP_LIMIT = 260
ENEMY_SEA_BOTTOM_LIMIT = 800

# Título e Ícone
pygame.display.set_caption("Pirate Invaders")

def load_image(file_path, width, height):
    image = pygame.image.load(file_path)
    return pygame.transform.scale(image, (width, height))

def load_and_flip_image(file_path, width, height):
    image = pygame.image.load(file_path)
    image = pygame.transform.scale(image, (width, height))
    return pygame.transform.flip(image, True, False)  # Espelhamento horizontal

# Carregar as imagens
playerImg = load_and_flip_image('./Player Ship.webp', 128, 128)
enemyImg = [load_image('./Pirate.webp', 64, 64) for _ in range(6)]
bulletImg = load_image('./Ally bomb.webp', 32, 32)
enemy_bulletImg = load_image('./Enemy Bomb.webp', 32, 32)
backgroundImg = load_image('./Background.webp', SCREEN_WIDTH, SCREEN_HEIGHT)

# Jogador
playerX = 50
playerY = 320
playerY_change = 0
bullet_cooldown = 500  # Tempo de espera entre tiros (em milissegundos)
last_bullet_time = 0

# Inimigos
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyX.append(random.randint(SCREEN_WIDTH - 100, SCREEN_WIDTH))
    enemyY.append(random.randint(ENEMY_SEA_TOP_LIMIT, ENEMY_SEA_BOTTOM_LIMIT - 64))
    enemyY_change.append(4)  # Velocidade intermediária dos inimigos
    enemyX_change.append(40)

# Tiros
bullets = []
enemy_bullets = []

# Pontuação
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# FPS (Frames por segundo)
clock = pygame.time.Clock()

# Carregar a música de fundo
pygame.mixer.music.load('music_fx_drone_synth_with_subtle_almost_imperceptible.mp3')
pygame.mixer.music.play(-1)  # Tocar indefinidamente

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, RED)
    screen.blit(over_text, (200, 250))

def retry_button():
    button_font = pygame.font.Font('freesansbold.ttf', 32)
    button_text = button_font.render("Tentar novamente", True, WHITE)
    button_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    screen.blit(button_text, button_rect)
    return button_rect

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    bullets.append([x + 64, y + 64])  # Tiro saindo do centro do barco

def fire_enemy_bullet(x, y):
    enemy_bullets.append([x - 16, y + 32])

def is_collision(objX, objY, bulletX, bulletY, obj_width, obj_height):
    return objX < bulletX < objX + obj_width and objY < bulletY < objY + obj_height

def reset_game():
    global playerY, playerY_change, score_value, bullets, enemy_bullets
    playerY = 320
    playerY_change = 0
    score_value = 0
    enemyX.clear()
    enemyY.clear()
    enemyY_change.clear()
    enemyX_change.clear()
    for i in range(num_of_enemies):
        enemyX.append(random.randint(SCREEN_WIDTH - 100, SCREEN_WIDTH))
        enemyY.append(random.randint(ENEMY_SEA_TOP_LIMIT, ENEMY_SEA_BOTTOM_LIMIT - 64))
        enemyY_change.append(4)
        enemyX_change.append(40)
    bullets.clear()
    enemy_bullets.clear()

def game():
    global playerY, playerY_change, score_value, last_bullet_time
    running = True
    game_over = False

    while running:
        screen.fill(BLACK)  # Cor do fundo
        screen.blit(backgroundImg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Verificação de tecla pressionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerY_change = -5  # Velocidade do jogador ajustada
                if event.key == pygame.K_s:
                    playerY_change = 5  # Velocidade do jogador ajustada
                if event.key == pygame.K_SPACE:
                    if game_over:
                        game_over = False
                        reset_game()
                    else:
                        current_time = pygame.time.get_ticks()
                        if current_time - last_bullet_time > bullet_cooldown:
                            fire_bullet(playerX, playerY)
                            last_bullet_time = current_time

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    playerY_change = 0

            # Verificação de clique no botão "Tentar novamente"
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if retry_button().collidepoint(mouse_pos):
                    game_over = False
                    reset_game()

        if not game_over:
            # Atualização da posição do jogador
            playerY += playerY_change
            playerY = max(PLAYER_SEA_TOP_LIMIT, min(playerY, PLAYER_SEA_BOTTOM_LIMIT - 128))

            # Movimento dos inimigos
            for i in range(num_of_enemies):
                if enemyX[i] < 0:
                    for j in range(num_of_enemies):
                        enemyX[j] = 1024
                    game_over_text()
                    game_over = True
                    break

                enemyY[i] += enemyY_change[i]
                if enemyY[i] <= ENEMY_SEA_TOP_LIMIT:
                    enemyY_change[i] = 4  # Velocidade intermediária dos inimigos
                    enemyX[i] -= enemyX_change[i]
                elif enemyY[i] >= ENEMY_SEA_BOTTOM_LIMIT - 64:
                    enemyY_change[i] = -4  # Velocidade intermediária dos inimigos
                    enemyX[i] -= enemyX_change[i]

                # Colisão com o jogador
                if is_collision(playerX, playerY, enemyX[i], enemyY[i], 128, 128):
                    game_over_text()
                    game_over = True
                    break

                # Colisão com o tiro do jogador
                for bullet in bullets:
                    if is_collision(enemyX[i], enemyY[i], bullet[0], bullet[1], 64, 64):
                        score_value += 1
                        enemyX[i] = random.randint(SCREEN_WIDTH - 100, SCREEN_WIDTH)
                        enemyY[i] = random.randint(ENEMY_SEA_TOP_LIMIT, ENEMY_SEA_BOTTOM_LIMIT - 64)
                        bullets.remove(bullet)

                enemy(enemyX[i], enemyY[i], i)

            # Movimento dos tiros do jogador
            for bullet in bullets:
                bullet[0] += 10  # Velocidade do tiro ajustada
                screen.blit(bulletImg, (bullet[0], bullet[1]))
                if bullet[0] >= SCREEN_WIDTH:
                    bullets.remove(bullet)

            # Tiro inimigo aleatório baseado na pontuação
            enemy_fire_rate = max(1, score_value // 5)  # Aumenta a frequência conforme a pontuação
            if len(enemy_bullets) < enemy_fire_rate:
                shooter = random.choice(range(num_of_enemies))
                fire_enemy_bullet(enemyX[shooter], enemyY[shooter])

            # Movimento dos tiros dos inimigos
            for enemy_bullet in enemy_bullets:
                enemy_bullet[0] -= 10  # Velocidade do tiro ajustada
                screen.blit(enemy_bulletImg, (enemy_bullet[0], enemy_bullet[1]))
                if enemy_bullet[0] <= 0:
                    enemy_bullets.remove(enemy_bullet)
                elif is_collision(playerX, playerY, enemy_bullet[0], enemy_bullet[1], 128, 128):
                    game_over_text()
                    game_over = True
                    break

            player(playerX, playerY)
            show_score(textX, textY)
        else:
            retry_button()
        
        pygame.display.update()
        
        # Controlar o FPS
        clock.tick(60)

game()
pygame.quit()
