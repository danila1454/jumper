from pygame import *
from random import randint

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Jumper')
game = True

FPS = 60
clock = time.Clock()

fon = transform.scale(image.load('fon_1.jpg'), (700, 500))

amount_proiden = 0

font.init()
font1 = font.SysFont('Arial', 30)
score_proiden = font1.render(f'Ваш счёт: '+ str(amount_proiden), True, (100, 100, 100))

amount_jump = 0
jump = False

class Platform (sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, rect_x, rect_y):
        super().__init__()
        self.color_1 = color_1
        self.color_3 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        

    def update(self):
        self.rect.y += 1
        if self.rect.y >= 490:
            self.rect.y = 0
            self.rect.x = randint(10, 690)
    #    window.blit(self.image, (self.rect.x, self.rect.y))

    # def reset(self):
    #     self.rect.y -= 5

    
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed_x, player_speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
    def jump(self):
        global amount_jump, jump
        if amount_jump <= 100:
            amount_jump += 1
            self.rect.y -= 2
        else:
            jump = False
            amount_jump = 0
        


player = GameSprite('ball_stal.png', 50, 400, 50, 30, 3, 3)



platforms = sprite.Group()

platform = Platform(100, 80, 0, 100, 10, 50, 450)
platforms.add(platform)
for i in range(5):
    platform = Platform(100, 80, 0, 100, 10, randint(0,700), randint(0,450))
    platforms.add(platform)








finish = False


while game:
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == False:

        window.blit(fon, (0, 0))
        platforms.draw(window)
        #platforms.update()
        player.reset()
        score_proiden = font1.render(f'Вы уничтожили: '+ str(amount_proiden), True, (100, 100, 100))

        window.blit(score_proiden, (0, 30))
    
        # if keys[K_SPACE]:
        #     player.jump()
        
        if keys[K_LEFT]:
            player.rect.x -= player.speed_x
        
        if keys[K_RIGHT]:
            player.rect.x += player.speed_x
        
        if jump == False:
            player.rect.y += 2
        else:
            player.jump()
        
        
        if sprite.spritecollide(player, platforms, False) and jump == False:
            jump = True
        

        if player.rect.y < 150:
            amount_proiden += 1
            platforms.update()
            player.rect.y += 1
            





    clock.tick(FPS)
    display.update()















