import math
import sys
import pygame.gfxdraw

pygame.init()
pygame.font.init()

width = 680
height = 460

FPS = 100
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 30)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fourier series visualization')

angle = 0
curve = []
iterations = 0
PI = 3.14159
x = 0
flag = False

while True:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                flag = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                flag = False

    text = font.render(f"Iterations = {iterations}", True, (0, 128, 0))
    screen.blit(text, (2, 0))

    if flag:
        x = pygame.mouse.get_pos()[0] - 10

    pygame.gfxdraw.box(screen, (0, height - 30, width, 30), (255, 255, 255))

    if x > width - 20:
        x = width - 20
    elif x < 0:
        x = 0

    iterations = x // 5
    pygame.gfxdraw.box(screen, (int(x), height - 50, 20, 50), (210, 0, 120))

    diameter = 100
    lx = 180
    ly = 250

    for i in range(0, iterations):
        prevX = lx
        prevY = ly
        n = i * 2 + 1
        radius = ((diameter / 2) * (4 / (n * PI)))

        lx += radius * math.cos(n * angle)
        ly += radius * math.sin(n * angle)

        pygame.gfxdraw.circle(screen, int(prevX), int(prevY), int(radius), (50, 180, 0))

        pygame.gfxdraw.line(screen, int(prevX), int(prevY), int(lx), int(ly), (255, 255, 255))

    curve.insert(0, ly)
    pygame.gfxdraw.line(screen, int(lx), int(ly), int(360), int(curve[0]), (255, 255, 255))
    pygame.gfxdraw.filled_circle(screen, int(360), int(curve[0]), 8, (210, 0, 120))

    for i in range(0, len(curve)):
        pygame.gfxdraw.pixel(screen, int(((i / 2) + 360)), int(curve[i]), (255, 255, 255))
        if i < len(curve) - 1:
            pygame.gfxdraw.line(screen, int((i / 2) + 360), int(curve[i]), int((i / 2 + 1) + 360), int(curve[i + 1]),
                                (255, 255, 255))

    if len(curve) > 500:
        curve.pop()

    pygame.display.update()
    angle += 0.01
    clock.tick(FPS)
