import pygame
# A linha 3 serve para iniciar a biblioteca
pygame.init()
# Na 5 linha é carregado a musica, coloque o arquivo da musica na pasta do projeto
pygame.mixer.music.load("nome da musica")
# Na 7 linha é iniciada a musica
pygame.mixer.music.play()
# Na 9 ele espera o evento acabar (a musica terminar)
pygame.event.wait()