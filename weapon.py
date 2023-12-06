import random

class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


    # INSTANCES OF WEAPONS CLASS
Fists = Weapons(name = "Fists", damage = random.randint(5,10))
Rusted_Sword = Weapons("Rusted Sword", damage = random.randint(10, 15))
Broken_Dagger = Weapons("Broken Dagger", damage = random.randint(15, 25))
Conditioned_Blade = Weapons("Conditioned Blade", damage = random.randint(40, 65))
Skirmished_Scimitar = Weapons("Skirmished Scimitar", damage = random.randint(35, 55))
Oathkeeper = Weapons("Oathkeeper", damage = random.randint(45, 70))
Spiked_Gauntlets = Weapons("Spiked Gauntlets", damage = random.randint(15, 35))
Defiler = Weapons("Defiler", damage = random.randint(40, 100))

    # FOR ENEMIES
Mucus_Fingers = Weapons("Mucus Fingers", damage = random.randint(1, 10))
Solid_Teardrop = Weapons("Solid Teardrop", damage = random.randint(10, 20))
Membrane_Screech = Weapons("Membrane Screech", damage = random.randint(20, 50))
Black_Breath = Weapons("Black Breath", damage = random.randint(20, 50))
Cavity_Eyes = Weapons("Cavity Eyes", damage = random.randint(25, 40))
Deformed_Fetus = Weapons("Deformed Fetus", damage = random.randint(20, 50))
Splitstreak = Weapons("Splitstreaker", damage = random.randint(30, 45))