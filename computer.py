# inheritance vs composition 
class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size 

class SSD:
    def __init__(self, capacity) -> None:
        self.capacity = capacity 

# computer has a CPU
# computer has a RAM
# computer has a SSD
class Computer:
    def __init__(self, cores, size, capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(size)
        self.ssd = SSD(capacity) 


mac = Computer(12, 32, 1024)