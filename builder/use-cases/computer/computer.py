class Computer:
    def __init__(self, serial) -> None:
        self.serial = serial
        self.memory = None
        self.hdd = None
        self.gpu = None
    def __str__(self):
        return f'Serial: {self.serial}\nMemory: {self.memory}\nHard disk: {self.hdd}\nGraphic card: {self.gpu}'