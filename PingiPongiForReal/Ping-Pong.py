#   Importing:
from pygame import *



#   Window:
window = display.set_mode((600, 400))
display.set_caption('Ping - Pong')

background = transform.scale(image.load('PingiPongiBG.png'),(600, 400))

window.blit(background, (0, 0))



#   FPS:
clock = time.Clock()
FPS = 100000000000000



#   Sprites:
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_lenght, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_lenght, player_width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_lenght, player_width):
        super().__init__(player_image, player_x, player_y, player_speed, player_lenght, player_width)
    def one_update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 311.5:
            self.rect.y += self.speed
    def two_update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 311.5:
            self.rect.y += self.speed



#   Objects:
playerone = Player('p_one.png', 10, 10, 5, 15, 75)
playertwo = Player('p_two.png', 575, 10, 5, 15, 75)

#   Game Cycle:
game_loop = True
while game_loop:
    window.blit(background, (0, 0))

    playerone.reset()
    playerone.one_update()
    playertwo.reset()
    playertwo.two_update()

    for e in event.get():
        if e.type == QUIT:
            game_loop = False

    clock.tick(FPS)

    display.update()