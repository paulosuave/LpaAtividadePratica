import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, ):
        match entity_name:

            case 'Level1Bg':
                list_bg = []
                for i in range(5):  # CARREGA IMAGENS LEVEL 1
                    list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(4):  # CARREGA IMAGENS LEVEL 2
                    list_bg.append(Background(f'Level2Bg{i}', position=(0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_WIDTH - 60)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_WIDTH - 60)))
