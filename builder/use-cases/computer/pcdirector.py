from pcbuilder import PcBuilder

class PcDirector:
    def __init__(self):
        self.builder = None

    def construct_pc(self, mem, hdd, gpu):
        self.builder = PcBuilder() 
        self.builder.set_gpu(gpu)
        self.builder.set_hdd(hdd)
        self.builder.set_memory(mem)

    @property
    def computer(self):
        return self.builder.computer