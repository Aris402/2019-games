import pygame

import random

height = 400
width = 900
background = pygame.display.set_mode((width, height))
bgimage = pygame.image.load('espaçopng.png')
time = pygame.time.get_ticks() // 1000
x = width / 4
y = height / 4
wave = 0


# Classe da bala do jogador, que reúne todas as funções dela
class Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Shoot, self).__init__()
        self.shot = pygame.image.load('projetilplayer2.png')
        self.shot2 = pygame.image.load('projetilplayer2.png')
        self.rect = self.shot.get_rect()
        self.rect2 = self.shot2.get_rect()
        self.speed = 5
        self.rect.y = y
        self.rect.x = x

    def trajectory(self):
        self.rect.y = self.rect.y - self.speed

    def put(self, surface):
        surface.blit(self.shot, self.rect)
        surface.blit(self.shot2, self.rect)


# Classe da nave do jogador, que reúne todas as suas funções
class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.player = pygame.image.load('naveturbinaforte.png')
        self.rect = pygame.Rect(0, 5, 24, 30)
        self.rect.y = height - 80
        self.rect.x = width / 2

        self.bullet = []
        self.bullet2 = []
        self.life = True

    def shott(self, x, y):
        spartan = Shoot(x + 5, y - 14)
        spartan2 = Shoot(x - 28, y - 14)
        self.bullet.append(spartan)
        self.bullet2.append(spartan2)

    def put(self):
        background.blit(self.player, self.rect)


class Shoot2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Shoot2, self).__init__()
        self.shot = pygame.image.load('Disparo Hunter.png')
        self.rect = self.shot.get_rect()
        self.speed = 5
        self.rect.y = y
        self.rect.x = x

    def trajectory(self):
        self.rect.y = self.rect.y - self.speed

    def put(self, surface):
        surface.blit(self.shot, self.rect)


# Classe do Inimigo, que reúne todas as funções do mesmo
class enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super(enemy, self).__init__()
        self.enemy = pygame.image.load('naveinimigatfo.png')
        self.rect = pygame.Rect(0, 5, 24, 30)
        self.rect.y = y - 110
        self.rect.x = random.randint(200, 600)
        while pygame.sprite.spritecollideany(self, group):
            self.rect.x = random.randint(200, 600)
        self.shoot = []
        self.life = True

    def put(self):
        background.blit(self.enemy, self.rect)

    def shott(self, x, y):
        hunter = Shoot2(x, y)
        self.shoot.append(hunter)


def SpartanShip():
    pygame.init()
    pygame.display.set_caption('Spartan Ship')
    Player = player()
    enemies = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    for e in range(5):
        Enemy = enemy(enemies)
        enemies.add(Enemy)

    playing = True

    clock = pygame.time.Clock()

    while playing:
        clock.tick(60)
        wave = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x, y = Player.rect.center
                    Player.shott(x, y)

        background.blit(bgimage, (0, 0))

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            Player.rect.x -= 4
            if Player.rect.x <= 0:
                Player.rect.x = 0
        elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            Player.rect.x += 4
            if Player.rect.x > 900:
                Player.rect.x = 900

        if wave == 1:
            for en in enemies:
                en.rect.y += 2
                if en.rect.y == 80:
                    en.rect.y -= 2
                en.put()
                enemies.add(en)
        if len(Player.bullet) > 0:
            for s1 in Player.bullet:
                s1.put(background)
                s1.trajectory()
                shoots.add(s1)
                if s1.rect.y < -10:
                    s1.kill()
        if len(Player.bullet2) > 0:
            for s2 in Player.bullet2:
                s2.put(background)
                s2.trajectory()
                shoots.add(s2)
                if s2.rect.y < -10:
                    s2.kill()
        hit = pygame.sprite.groupcollide(enemies, shoots, True, True)
        if hit:
            print('colidiu')
        Player.put()
        pygame.display.flip()


SpartanShip()
pygame.quit()
