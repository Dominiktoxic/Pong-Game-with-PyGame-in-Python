import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960

FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
title = "Pong - A Remake"
pygame.display.set_caption(title)

running = True

def Player():
    player = pygame.Rect(10, SCREEN_HEIGHT / 2 - 100, 5, 200)
    pygame.draw.rect(screen, (255, 255, 255), player)
    return player

def Ball():
    ball = pygame.Rect(SCREEN_WIDTH / 2 - 7, SCREEN_HEIGHT / 2 - 7, 14, 14)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    return ball

def Opponent():
    opponent = pygame.Rect(SCREEN_WIDTH - 10, SCREEN_HEIGHT / 2 - 100, 5, 200)
    pygame.draw.rect(screen, (255, 255, 255), opponent)
    return opponent

player = Player()
ball = Ball()
opponent = Opponent()

ballSpeedX = 10
ballSpeedY = 10

scorePlayer = 0
scoreOpponent = 0

font = pygame.font.SysFont("arialblack", 75)

index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]:
        player.y -= 9
    elif key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]:
        player.y += 9
    
    if opponent.y < ball.y:
        opponent.y += 10
    elif opponent.y > ball.y:
        opponent.y -= 10

    screen.fill((0, 0, 0))
    
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    if ball.x <= 0:
        index += 1
        ball.x, ball.y = SCREEN_WIDTH / 2 - 7, SCREEN_HEIGHT / 2 - 7
        if index % 2 == 0:
            ballSpeedX *= -1
            ballSpeedY *= -1
        scoreOpponent += 1
        print(f"Score: {scorePlayer} | {scoreOpponent}")
    elif ball.x >= SCREEN_WIDTH:
        index += 1
        ball.x, ball.y = SCREEN_WIDTH / 2 - 7, SCREEN_HEIGHT / 2 - 7
        if index % 2 != 0:
            ballSpeedX *= -1
            ballSpeedY *= -1
        scorePlayer += 1
        print(f"Score: {scorePlayer} | {scoreOpponent}")
    elif ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
        ballSpeedY *= -1
    
    if ball.colliderect(player):
        ballSpeedX *= -1
    if ball.colliderect(opponent):
        ballSpeedX *= -1
    
    pygame.draw.line(screen, (255, 255, 255), (SCREEN_WIDTH / 2 + 3, 115), (SCREEN_WIDTH / 2 + 3, SCREEN_HEIGHT), 6)
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), opponent)
    scoreText = font.render(f"{scorePlayer} : {scoreOpponent}", True, (255, 255, 255))
    screen.blit(scoreText, (SCREEN_WIDTH / 2 - 84, 0))

    clock.tick(FPS)
    pygame.display.update()