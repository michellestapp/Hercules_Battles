class Hercules:
    def __init__(self, attack_name) -> None:
        self.name = "Hercules"
        self.attack_power = 15
        self.attack_name = attack_name
        self.health = 100

    def attack(self,foe):
        print()
        print('f" Hercules has attacked {foe.name} with his {self.attack_name}')
        foe.health -= self.attack_power
        print(f" {foe.name}'s health is now {foe.health}")

