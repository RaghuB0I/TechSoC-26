import random

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

class Duel:

    turn = 1
    element_relations = [("Water", "Fire"), ("Fire","Air"), ("Air","Earth"), ("Earth","Water")]

    def __init__(self, bender1, bender2):
        self.bender1 = bender1
        self.bender2 = bender2

    def start_duel(self):

        element_mult = 0
        crit_mult = 0
        c_count = 0
        s_count = 0

        print(f"{self.bender1.name} ({self.bender1.element}, {self.bender1.hp}/{self.bender1.hp_t}) vs {self.bender2.name} ({self.bender2.element}, {self.bender2.hp}/{self.bender2.hp_t})")


        while not(self.bender1.is_fainted() or self.bender2.is_fainted()):

            if self.bender1.speed > self.bender2.speed:
                first, second = self.bender1, self.bender2
            elif self.bender1.speed < self.bender2.speed:
                first, second = self.bender2, self.bender1
            else:
                first, second = random.choice([(self.bender1, self.bender2), (self.bender2, self.bender1)])

            print(f"Turn-{self.turn} {first.name} goes first!(Speed: {first.speed} vs {second.speed})")
            print(f"{first.name} uses {first.moves[r][0]}")

            r = random.randint(0,3)
            crit = random.randint(1,10)
            
            if (first.element, second.element) in self.element_relations:
                element_mult = 2
                print(f"Super Effective! ({first.element} is strong against {second.element})")
                s_count += 1
            elif (second.element, first.element) in self.element_relations:
                element_mult = 0.5
                print(f"Not Very Effective! ({first.element} is weak against {second.element})")
            else:
                element_mult = 1

            if crit == 10:
                crit_mult = 2
                c_count += 1
                print("Critical Hit!")
            else:
                crit_mult = 1

            b_damage = round((first.moves[r][1] * first.atk) / second.defense)
            t_damage = round(b_damage * element_mult * crit_mult)
            t_damage = max(t_damage, 1)
            second.hp -= t_damage

            print(f"{second.name} took {t_damage} damage! ")
            print(f"{second.name} HP: {max(0, second.hp)}/{second.hp_t}\n")



            self.turn += 1

        else:

            winner = ""

            if self.bender1.is_fainted():
                print(f"{self.bender1.name} has fainted!\n {self.bender2.name} wins the duel!\n")
                winner = self.bender2.name
            else:
                print(f"{self.bender2.name} has fainted!\n {self.bender1.name} wins the duel!\n")
                winner = self.bender1.name

            print("Duel Summary:")
            print(f" - Winner: {winner}")
            print(f" - Total Turns: {self.turn}")
            print(f" - Critical Hits: {c_count}")
            print(f" - Super Effective Hits: {s_count} \n")

##Example 1:

# Create Benders
kael = Bender("Kael", "Fire", 100, 58, 38, 88,
             [("Ember Slash", 40), ("Quick Jab", 30), ("Focus", 0), ("Flame Surge", 70)])

mira = Bender("Mira", "Water", 92, 50, 45, 60,
             [("Water Whip", 35), ("Tide Push", 25), ("Mist Veil", 0), ("Tidal Wave", 60)])

# Start duel
duel = Duel(kael, mira)
duel.start_duel()

# Turn 1: Kael uses Ember Slash (move 0)
# Turn 2: Mira uses Water Whip (move 0), Critical Hit

##Example 2:

# Create Benders with a neutral matchup (Water vs Air) and tied speed
nadia = Bender("Nadia", "Water", 85, 48, 60, 72,
              [("Wave Crash", 35), ("Splash Kick", 25), ("Guard", 0), ("Riptide", 50)])

talon = Bender("Talon", "Air", 90, 52, 55, 72,
              [("Gale Strike", 38), ("Wind Cutter", 28), ("Updraft", 0), ("Cyclone Blast", 48)])

duel = Duel(nadia, talon)
duel.start_duel()
