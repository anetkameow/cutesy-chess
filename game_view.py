import pygame

bialy_pion = pygame.image.load('obrazy/bialy_P.png')
bialy_wieza = pygame.image.load('obrazy/bialy_W.png')
bialy_skoczek = pygame.image.load('obrazy/bialy_S.png')
bialy_goniec = pygame.image.load('obrazy/bialy_G.png')
bialy_krol = pygame.image.load('obrazy/bialy_K.png')
biala_dama = pygame.image.load('obrazy/bialy_D.png')

czarny_pion = pygame.image.load('obrazy/czarny_P.png')
czarna_wieza = pygame.image.load('obrazy/czarny_W.png')
czarny_skoczek = pygame.image.load('obrazy/czarny_S.png')
czarny_goniec = pygame.image.load('obrazy/czarny_G.png')
czarny_krol = pygame.image.load('obrazy/czarny_K.png')
czarna_dama = pygame.image.load('obrazy/czarny_D.png')


def odswiezanie(screen, biale_figury, czarne_figury):
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen, (255, 153, 204), (i*60, j*60, 60, 60))
            else:
                pygame.draw.rect(screen, (255, 0, 127), (i*60, j*60, 60, 60))

    for figura in biale_figury:
        if figura[0] == 'P' and figura[1] == 1:
            screen.blit(bialy_pion, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'W' and figura[1] == 1:
            screen.blit(bialy_wieza, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'S' and figura[1] == 1:
            screen.blit(bialy_skoczek, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'G' and figura[1] == 1:
            screen.blit(bialy_goniec, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'K' and figura[1] == 1:
            screen.blit(bialy_krol, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'D' and figura[1] == 1:
            screen.blit(biala_dama, (figura[2]*60, figura[3]*60))

    for figura in czarne_figury:
        if figura[0] == 'P' and figura[1] == 1:
            screen.blit(czarny_pion, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'W' and figura[1] == 1:
            screen.blit(czarna_wieza, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'S' and figura[1] == 1:
            screen.blit(czarny_skoczek, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'G' and figura[1] == 1:
            screen.blit(czarny_goniec, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'K' and figura[1] == 1:
            screen.blit(czarny_krol, (figura[2]*60, figura[3]*60))
        elif figura[0] == 'D' and figura[1] == 1:
            screen.blit(czarna_dama, (figura[2]*60, figura[3]*60))
