class Command:
    commands = None

    def __init__(self, commands: list = None):
        self.commands = commands

    def clean(self):
        self.commands = list()
