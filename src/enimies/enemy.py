from abc import ABC, abstractmethod


class Enemy(ABC):

    def __init__(self, health: int, damage: int, name: str):
        self.health = health
        self.damage = damage
        self.name = name
        self.dead = False

    def attack(self):
        return self.damage

    def damaged(self, userDamage):
        self.health -= userDamage

        if self.health <= 0:
            self.dead = True

    def get_name(self):
        return self.name

    def is_dead(self):
        return self.dead

    @abstractmethod
    def enemy_phase(self, player):
        pass
