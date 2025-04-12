from pygame import * 
from random import randint
window = display.set_mode((700, 500))
background = transform.scale(image.load("New Piskel.png"), (700, 500))

clock = time.Clock()
FPS = 60

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 85:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 535:
            self.rect.x += self.speed

count = 0

lost = 1

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = -100
            self.rect.x = randint(85, 535)
            lost = lost + 1

main_player = Player("New Piskel (1).png", 300, 400, 70, 70, 25)

sprite1 = Enemy("New Piskel (2).png", 150, 200, 70, 70, 10)

sprite2 = Enemy("New Piskel (3).png", 150, 200, 70, 70, 10)


font1 = font.Font(None, 90)
count_lifes = 3
text_loss = font1.render("YOU LOSE", True, (255, 0, 0))
game = True
finish = False
while game:
    if finish != True:
        window.fill((0, 0, 0))
        window.blit(background,(0, 0))
        main_player.update()
        main_player.reset()
        sprite1.update()
        sprite1.reset()
        sprite2.update()
        sprite2.reset()
        if main_player.colliderect(sprite1.rect) or main_player.colliderect(sprite2.rect):
            count_lifes -= 1
        if sprite.collide_rect(main_player, sprite1):
            finish = True
            window.blit(text_loss,(200, 200))
        if sprite.collide_rect(main_player, sprite2):
            finish = True
            window.blit(text_loss,(200, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)










