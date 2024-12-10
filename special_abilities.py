import random

# Special Ability Base class
class SpecialAbility:
    def __init__(self, name):
        self.name = name

    def use(self, user, opponent):
        pass #abstract function for subclass to define

class QuickShot(SpecialAbility):
    def __init__(self):
        super().__init__("Quick Shot")

    def use(self, user, opponent):
        succeful_attack = random.randint(1,2)
        if succeful_attack == 1:
            print(f"{user.name} uses {self.name} to deal double damage")
            user.attack(opponent, user.attack_power*2)
        else:
            print(f"{user.name} uses {self.name} to deal double damage but misses")

class Evade(SpecialAbility):
    def __init__(self):
        super().__init__("Evade")

    def use(self, user, opponent):
        print(f"{user.name} uses {self.name} to protect against next attack")
        user.evade = True

class HolyStrike(SpecialAbility):
    def __init__(self):
        super().__init__("Holy Strike")

    def use(self, user, opponent):
        bonus_damage = random.randint(0, user.attack_power)
        print(f"{user.name} uses {self.name} to add {bonus_damage} worth of bonus damage to attack but with half the initial attack_power")
        user.attack(opponent, ((user.attack_power//2) + bonus_damage))

class DivineShield(SpecialAbility):
    def __init__(self):
        super().__init__("Divine Shield")

    def use(self, user, opponent):
        user.shield += user.attack_power
        print(f"{user.name} uses {self.name} to add {user.attack_power} worth of protection to their shield")

class Bezerk(SpecialAbility):
    def __init__(self):
        super().__init__("Bezerk")

    def use(self, user, opponent):
        user.attack(opponent, user.attack_power*3)
        user.health -= user.attack_power
        print(f"{user.name} uses {self.name} to triple attack strength but deals {user.attack_power} damage to themselves")

class Bombard(SpecialAbility):
    def __init__(self):
        super().__init__("Bombard")

    def use(self, user, opponent):
        multiplier = random.randint(1, 4)
        print(f"{user.name} uses {self.name} to attack {multiplier} times with half damage")
        for i in range(0, multiplier):
            user.attack(opponent, user.attack_power//2)

class StealthAttack(SpecialAbility):
    def __init__(self):
        super().__init__("Stealth Attack")
    
    def use(self, user, opponent):
        succeful_evade = random.randint(1,2)
        if succeful_evade == 1:
            print(f"{user.name} uses {self.name} to deal half the damage and evades next attack")
            user.evade = True
        else:
            print(f"{user.name} uses {self.name} to deal half the damage but fails to evade next attack")   
        user.attack(opponent, user.attack_power//2)

class SuperHeal(SpecialAbility):
    def __init__(self):
        super().__init__("Super Heal")

    def use(self, user, opponent):
        succeful_heal = random.randint(1,2)
        if succeful_heal == 1:
            print(f"{user.name} uses {self.name} to heal twice as much")
            user.heal(2)
        else:
            print(f"{user.name} uses {self.name} to heal twice as much but fails")