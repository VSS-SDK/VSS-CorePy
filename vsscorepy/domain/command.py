from random import randint

from vsscorepy.domain.wheels_command import WheelsCommand


class Command:
    wheels_commands = None

    def __init__(self, wheels_commands: list = list()):
        self.wheels_commands = wheels_commands

    def clean(self):
        self.wheels_commands = list()

    @classmethod
    def random(cls):
        qtd = randint(2, 10)

        wheels_commands = [WheelsCommand.random() for i in range(1, qtd)]

        return cls(wheels_commands=wheels_commands)
