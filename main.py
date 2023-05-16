import pygame
from menu import Menu, GameOver
from game import Game


class Main:

    def __init__(self):
        # Iniciando o pygame e criando a janela do jogo

        pygame.init()

        self.janela = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption("abelha_guerreira")
      
        # Definição de variáveis de estado do jogo

        self.loop = True
        self.fps = pygame.time.Clock()

              # Instalando classes Menu, Game e GameOver

        self.start_screen = Menu("tela de start")
        self.game = Game()
        self.gameover = GameOver("tela de gameover")

          # Capturando os eventos  atualiza as variáveis

    def evento(self):
        for event in pygame.evento.get():
            if evento.type == pygame.QUIT:
                self.loop = False
            if not self.start_screen.change_scene:
                self.start_screen.event(evento)
            elif not self.game.change_scene:
                self.game.abelha_guerreira(evento)
            else:
                self.gameover.event(evento)

        # Desenha as imagens na tela de acordo com o estado atual do jogo

    def draw(self):
        self.janela.fill([0, 0, 0])
        if not self.start_screen.change_scene:
            self.start_screen.draw(self.janela)
        elif not self.game.change_scene:
            self.game.draw(self.janela)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.janela)
        else:
            self.start_screen.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.abelha.life = 3
            self.game.abelha.pts = 0
        # Loop principal do jogo que atualiza a tela de acordo com os eventos capturados

    def updates(self):

        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.evento()
            pygame.display.update()


Main().updates()
