import random
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code import EntityMediator
from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, COLOR_GREEN2, COLOR_CYAN, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))  # 'Level1Bg0'
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        # self.entity_list.append(EntityFactory.get_entity('Player1'))

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
            # self.entity_list.append((EntityFactory.get_entity('Player2')))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # INSERIR MUSICA
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        running = True  # Variável para controlar o loop principal

        while running:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # VERIFICAR JOGADOR QUE VAI ATIRAR
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

                # PRINT SCORE
                if ent.name == 'Player1':
                    self.level_text(20, f'Player1 - LIFE:{ent.health} '
                                        f'| SCORE: {ent.score}', COLOR_GREEN2, (320, 7))
                if ent.name == 'Player2':
                    self.level_text(20, f'Player2 - LIFE:{ent.health} '
                                        f'| SCORE: {ent.score}', COLOR_CYAN, (320, 20))

            # VERIFICAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # EVENTO PARA INIMIGOS
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                # EVENTO PARA TEMPO
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

            # VERIFICAR SE O PLAYER ESTÁ VIVO
            found_player = any(isinstance(ent, Player) for ent in self.entity_list)

            if not found_player:
                self.show_game_over_screen()  # Exibir GAME OVER
                running = False  # Parar o loop

            # IMPRESSÃO DE INFORMAÇÕES NA TELA
            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    # GAME OVER
    def show_game_over_screen(self):
        game_over_image = pygame.image.load("./asset/gameOverBg.png")
        game_over_image = pygame.transform.scale(game_over_image, (self.window.get_width(), self.window.get_height()))

        pygame.mixer_music.stop()  # Para a música atual
        pygame.mixer.Sound("./asset/gameOver.mp3").play()

        self.window.blit(game_over_image, (0, 0))  # Desenha a imagem de Game Over

        self.level_text(30, "Pressione ESC para sair", COLOR_WHITE, (WIN_HEIGHT // 2 - 50, WIN_HEIGHT - 100))
        pygame.display.flip()

        # Aguarda ESC para sair
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False

            #  IMPRESSÃO DE INFORMAÇÕES NA TELA
            # self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            # self.level_text(20, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            # self.level_text(20, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            # pygame.display.flip()
            #
            # EntityMediator.verify_collision(entity_list=self.entity_list)
            # EntityMediator.verify_health(entity_list=self.entity_list)

    # FORMATAÇÃO DO TEXTO
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
