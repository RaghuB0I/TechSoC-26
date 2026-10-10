class Bender:

    hp_t = 0

    def __init__(self, name, element, hp, attack, defense, speed, moves):
        self.name = name
        self.element = element
        self.hp = hp
        self.atk = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves
        self.hp_t = hp

    def display_stats(self):

        print(f"{self.name} ({self.element}) - HP:{self.hp}/{self.hp_t}, Attack = {self.atk}, Defense = {self.defense}, Speed = {self.speed}")
        for i in range(3):
            print(f"{self.moves[i][0]} ({self.moves[i][1]}),",end = " ")
        print(f"{self.moves[3][0]} ({self.moves[3][1]})")

        return " "

    def is_fainted(self):
        if self.hp <= 0:
            return True
        return False

    def attack(self, victim, move_n):

        self.victim = victim
        self.n = move_n

        if self.n < 0 or self.n >= 4:
            print("Invalid move number. Please choose one from 0 to 3.")
            return False

        move = self.moves[self.n]
        damage = round((move[1] * self.atk) / self.victim.defense)
        self.victim.hp -= damage

        print(f"{self.name} uses {move[0]}!")
        print(f"{self.victim.name} took {damage} damage.","\n")

#Example 1: Basic Bender Creation and Attack

print("-------------------------------------------------------------------------------------------")

kael = Bender("Kael", "Fire", 100, 58, 38, 88,
             [("Ember Slash", 40), ("Quick Jab", 30), ("Focus", 0), ("Flame Surge", 70)])

mira = Bender("Mira", "Water", 92, 50, 45, 60,
             [("Water Whip", 35), ("Tide Push", 25), ("Mist Veil", 0), ("Tidal Wave", 60)])

print(kael.display_stats())
print(mira.display_stats())

kael.attack(mira, 0)
print(mira.display_stats())

print(f"Mira fainted: {mira.is_fainted()}")
print("-------------------------------------------------------------------------------------------")

#Example 2: Bender Fainting

zephyr = Bender("Zephyr", "Air", 28, 12, 50, 95,
               [("Gust", 0), ("Wind Slap", 18), ("Tumble", 12), ("Cyclone", 22)])


doran = Bender("Doran", "Earth", 145, 80, 75, 40,
              [("Boulder Throw", 75), ("Rock Fist", 42), ("Tremor", 48), ("Mountain Crush", 85)])

print(zephyr.display_stats())
print(doran.display_stats())

doran.attack(zephyr, 0)
print(zephyr.display_stats())

print(f"Zephyr fainted: {zephyr.is_fainted()}")
print("-------------------------------------------------------------------------------------------")

        
    
