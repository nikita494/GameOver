import pygame
import sys
import os


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class GameOverScreen(pygame.sprite.Sprite):
    image = load_image('gameover.png')

    def __init__(self, group=None):
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.rect.left = -self.image.get_width()

    def update(self):
        if self.rect.right < width:
            self.rect.move_ip(200 / fps, 0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Game over')
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    running = True
    fps = 60
    screen.fill(pygame.Color('blue'))
    gameOverScreen = pygame.sprite.Group()
    GameOverScreen(gameOverScreen)
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color('blue'))
        gameOverScreen.draw(screen)
        gameOverScreen.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
