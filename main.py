

class Characeter_sheet():
    def __init__(self, name, speed, strenght, dexteriti, constitution, wisdom, inteligenc, charisma) -> None:
        self.name: str = name
        self.speed: int = speed
        self.strenght: int = strenght
        self.dexteriti: int = dexteriti
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.inteligenc: int = inteligenc
        self.charisma: int = charisma
        
    def print_stats(self):
        for arg in [1, 2]:
            print(arg)
        return self.name, self.speed


def main():
    pass


if __name__ == "__main__":
    new_char = Characeter_sheet(name = "Chriss", speed = 40, strenght = 10, dexteriti=10, constitution=10, wisdom=10, inteligenc=10, charisma=10)
    for args in vars(new_char).items():
        print(args)
