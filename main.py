import pygame

pygame.init()
window = pygame.display.set_mode(size=(600, 480))  # criando janela

while True:
    # (Check for all events) checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() # (end pygame) fechando pygame

