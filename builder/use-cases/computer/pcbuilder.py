from random import randint

from computer import Computer

class PcBuilder:
    def __init__(self):
        serial = '-'.join(str(randint(1, 9)) for _ in range(10))
        self.computer = Computer(serial)

    def set_hdd(self, hdd):
        self.computer.hdd = hdd

    def set_gpu(self, gpu):
        self.computer.gpu = gpu

    def set_memory(self, memory):
        self.computer.memory = memory