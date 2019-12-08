# 2019-games
# Alunos: Aristóteles Daniel, Alexsander Anulino e Bergson
Repositório para entra de jogo da turma de InfoWeb 2019
import sys

import pygame

import random

# bases da tela
black = (41, 36, 33)
largura = 900
altura = 400
x = largura / 4
y = altura / 4

fundo = pygame.display.set_mode((largura, altura))
imagemdefundo = pygame.image.load('espaçopng.png')
time = pygame.time.get_ticks() // 1000


# classe do tiro da nave
class projetil1(pygame.sprite.Sprite):
    # função self
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagemprojetil = pygame.image.load('projetilplayer2.png')
        self.imagemprojetil2 = pygame.image.load('projetilplayer2.png')

        self.rect = self.imagemprojetil.get_rect()
        self.rect = self.imagemprojetil2.get_rect()
        self.velocidadeprojetil = 5
        self.rect.y = y
        self.rect.x = x

    # função da trajetória do tiro da nave do player
    def trajetoria(self):
        self.rect.y = self.rect.y - self.velocidadeprojetil

    # função para colocar o tiro da nave do player
    def colocar(self, superficie):
        superficie.blit(self.imagemprojetil, self.rect)
        superficie.blit(self.imagemprojetil2, self.rect)


class enemyship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image2 = pygame.image.load('naveinimigatfo.png')
        self.rect = self.image2.get_rect()

        self.rect.y = y - 110
        self.rect.x = random.randrange(200, 600)
        # while pygame.sprite.spritecollideany(self):
        # self.rect.x = random.randrange(200, 600)

        self.shoot = []
        self.life = True

    def put(self):
        fundo.blit(self.image2, self.rect)


# classe da nave do player


class naveplayer(pygame.sprite.Sprite):
    def __init__(self):
        super(naveplayer, self).__init__()
        self.image = pygame.image.load('naveturbinaforte.png')
        self.rect = self.image.get_rect()

        self.rect.x = largura / 2
        self.rect.y = altura - 80

        self.disparo = []
        self.disparo2 = []
        self.playerlife = True

    def shoot(self, x, y):
        spartanshoot = projetil1(x - 15, y - 14)
        spartanshoot2 = projetil1(x - 48, y - 14)
        self.disparo.append(spartanshoot)
        self.disparo2.append(spartanshoot2)

    def put(self):
        fundo.blit(self.image, self.rect)


def SpartanShip():
    pygame.init()

    pygame.display.set_caption('Spartan Ship')
    player = naveplayer()
    enemy = enemyship()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)

    playing = True

    relogio = pygame.time.Clock()

    while playing:
        relogio.tick(60)
        # player.movimento()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x, y = player.rect.center
                    player.shoot(x, y)
        fundo.blit(imagemdefundo, (0, 0))
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            player.rect.x -= 4
            if player.rect.x <= 0:
                player.rect.x = 0
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            player.rect.x += 4
            if player.rect.x > 900:
                player.rect.x = 900

        enemy.rect.y += 2
        if enemy.rect.y == 80:
            enemy.rect.y -= 2

        if len(player.disparo) > 0:
            for x in player.disparo:
                x.colocar(fundo)
                x.trajetoria()
                if x.rect.y < -10:
                    player.disparo.remove(x)
        if len(player.disparo2) > 0:
            for x in player.disparo2:
                x.colocar(fundo)
                x.trajetoria()
                if x.rect.y < -10:
                    player.disparo2.remove(x)
        player.put()
        enemy.put()
        pygame.display.flip()


SpartanShip()
pygame.quit()
