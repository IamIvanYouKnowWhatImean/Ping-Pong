#   Importing:
from pygame import *



#   Window:
window = display.set_mode((600, 400))
display.set_caption('Ping - Pong')

background = transform.scale(image.load('PingPongBackground.png'),(600, 400))

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
    def p_one_update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 311.5:
            self.rect.y += self.speed
    def p_two_update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 311.5:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_lenght, player_width, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, player_speed, player_lenght, player_width)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def ball_update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if sprite.collide_rect(ball, playerone) or sprite.collide_rect(ball, playertwo):
            self.speed_x *= -1
        elif self.rect.y <= 10 or self.rect.y >= 327:
            self.speed_y *= -1



#   Objects:
playerone = Player('PingPongPlayerSprite.png', 10, 10, 5, 15, 75)
playertwo = Player('PingPongPlayerSprite.png', 575, 10, 5, 15, 75)
ball = Ball('PingPongBallSprite.png', 50, 50, 2, 40, 40, 2, 2)

#   Game Cycle:
game_loop = True
while game_loop:
    window.blit(background, (0, 0))

    playerone.reset()
    playerone.p_one_update()
    playertwo.reset()
    playertwo.p_two_update()
    ball.reset()
    ball.ball_update()

    for e in event.get():
        if e.type == QUIT:
            game_loop = False

    clock.tick(FPS)

    display.update()