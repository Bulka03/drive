from pygame import * 
window = display.set_mode((700, 500))
background = transform.scale(image.load("New Piskel.png"), (700, 500))

clock = time.Clock()
FPS = 60

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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

main_player = Player("New Piskel (1).png", 300, 400, 70, 70, 25)

sprite1 = GameSprite("New Piskel (2).png", 150, 200, 70, 70, 25)

sprite2 = GameSprite("New Piskel (3).png", 480, 200, 70, 70, 25)
game = True
finish = False
while game:
    if finish != True:
        window.blit(background,(0, 0))
        main_player.update()
        main_player.reset()
        sprite1.update()
        sprite1.reset()
        sprite2.update()
        sprite2.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)










