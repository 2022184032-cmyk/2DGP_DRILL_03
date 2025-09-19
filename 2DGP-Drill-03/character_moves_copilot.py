import pygame
import math

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("캐릭터 운동 반복")

# 캐릭터 이미지 로드
character = pygame.image.load("character.png")
char_rect = character.get_rect()

# 운동 파라미터
center_x, center_y = WIDTH // 2, HEIGHT // 2
size = 200  # 운동 크기
speed = 2   # 속도

# 사각형 경로 좌표
square_points = [
    (center_x - size//2, center_y - size//2),
    (center_x + size//2, center_y - size//2),
    (center_x + size//2, center_y + size//2),
    (center_x - size//2, center_y + size//2)
]

# 삼각형 경로 좌표
triangle_points = [
    (center_x, center_y - size//2),
    (center_x - size//2, center_y + size//2),
    (center_x + size//2, center_y + size//2)
]

clock = pygame.time.Clock()

# 상태
mode = 0  # 0: 사각, 1: 원, 2: 삼각
step = 0
progress = 0.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # 사각운동
    if mode == 0:
        start = square_points[step % 4]
        end = square_points[(step + 1) % 4]
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        dist = math.hypot(dx, dy)
        if dist != 0:
            progress += speed / dist
        x = start[0] + dx * progress
        y = start[1] + dy * progress
        if progress >= 1.0:
            progress = 0.0
            step = (step + 1) % 4
            if step == 0:
                # 사각형 경로가 끝나면 원운동 시작점으로 순간이동
                mode = 1
                progress = 0.0
                step = 0
                x = center_x + size//2
                y = center_y

    # 원운동
    elif mode == 1:
        angle = progress * 2 * math.pi
        x = center_x + size//2 * math.cos(angle)
        y = center_y + size//2 * math.sin(angle)
        progress += speed / (2 * math.pi * size//2)
        if progress >= 1.0:
            progress = 0.0
            # 원운동이 끝나면 삼각운동 시작점으로 순간이동
            mode = 2
            step = 0
            x, y = triangle_points[0]

    # 삼각운동
    elif mode == 2:
        start = triangle_points[step % 3]
        end = triangle_points[(step + 1) % 3]
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        dist = math.hypot(dx, dy)
        if dist != 0:
            progress += speed / dist
        x = start[0] + dx * progress
        y = start[1] + dy * progress
        if progress >= 1.0:
            progress = 0.0
            step = (step + 1) % 3
            if step == 0:
                # 삼각운동이 끝나면 사각운동 시작점으로 순간이동
                mode = 0
                step = 0
                x, y = square_points[0]

    char_rect.center = (int(x), int(y))
    screen.blit(character, char_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
