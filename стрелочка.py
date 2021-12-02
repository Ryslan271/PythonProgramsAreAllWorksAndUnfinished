import os
import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


clock = pygame.time.Clock()

# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

# изображение должно лежать в папке data
cursor_image = load_image("cur.png")

cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = cursor_image
cursor.rect = cursor.image.get_rect()

# скрываем системный курсор
pygame.mouse.set_visible(False)

running = True
dist = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            hero.rest.top += dist
        elif key[pygame.K_UP]:
            hero.rect.top -= dist
        if key[pygame.K_RIGHT]:
            hero.rect.left += dist
        elif key[pygame.K_LEFT]:
            hero.rect.left -= dist
    screen.fill(pygame.Color("white"))
    # рисуем курсор только если он в пределах окна
    if pygame.mouse.get_focused():
        all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
