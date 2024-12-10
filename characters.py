from special_abilities import Bezerk, Bombard, StealthAttack, SuperHeal, QuickShot, Evade, HolyStrike, DivineShield
import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health 
        self.evade = False
        self.special_ability_1 = None
        self.special_ability_2 = None
        self.shield = 0


    def attack(self, opponent, damage):
        if opponent.evade:
            opponent.evade = False
            print(f"{self.name}'s attack is evaded by {opponent.name}!")
        else:
            rand_attack_power = random.randint(damage - (damage//2), damage + (damage//2))
            if opponent.shield:
                if opponent.shield > rand_attack_power:
                    opponent.shield -= rand_attack_power
                    rand_attack_power = 0
                    print(f"{opponent.name}'s shield absorbs entire attack")
                else:
                    rand_attack_power -= opponent.shield
                    print(f"{opponent.name}'s shield absorbs {opponent.shield} worth of damage")
                    opponent.shield = 0    
            opponent.health -= rand_attack_power
            print(f"{self.name} attacks {opponent.name} for {rand_attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def special_abilities(self, opponent):
        print("Choose which special ability to use: ")
        print(f"1. {self.special_ability_1.name}")
        print(f"2. {self.special_ability_2.name}")
        choice = input("Enter the number of your ability choice: ")
        if(choice == '1'):
            self.special_ability_1.use(self, opponent)
        elif(choice == '2'):
            self.special_ability_2.use(self, opponent)
        else:
            print(f"Invalid choice, defaulting to {self.special_ability_1.name}")
            self.special_ability_1.use(self, opponent)

    def heal(self, multiplier = 1):
        heal_amount = 25 * multiplier
        if(self.max_health > (self.health + heal_amount)):
            self.health += heal_amount
            print(f"{self.name} heals {self.name} by {heal_amount}!")
        else:
            self.health = self.max_health
            print(f"{self.name} heals {self.name} to max health!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability_1 = Bezerk()
        self.special_ability_2 = Bombard()  

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability_1 = StealthAttack()
        self.special_ability_2 = SuperHeal() 

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability_1 = QuickShot()
        self.special_ability_2 = Evade()

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability_1 = HolyStrike()
        self.special_ability_2 = DivineShield()    

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.minions = 0

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def generate_minions(self):
        successful_generation = random.randint(1,2)
        if successful_generation == 1:
            self.minions += 1
            print(f"{self.name} generates 1 new minion for a total of {self.minions}")

    def attack(self, opponent, power):
        super().attack(opponent, power)
        if self.minions > 0:
            print(f"{self.name} has {self.minions} minion(s) which deal 5 damage each")
            super().attack(opponent, 5*self.minions)
