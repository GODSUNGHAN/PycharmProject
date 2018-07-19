player_health = 100
player_strength= 500
monster_health = 20000
monster_strength = 10


class player:

    def __init__(self, strength, health):
        self.strength = strength
        self.health = health

    def attack_palyer(self):
        print ("attack?")
        answer = input()

        if answer == "attack":
            self.health = monster_health - (random.randint(1,10))


