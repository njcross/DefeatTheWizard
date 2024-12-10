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

    def heal(self):
        heal_amount = 25
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

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

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

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

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
        print(f"{user.name} uses {self.name} to deal double damage")
        user.attack(opponent, user.attack_power*2)

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
        bonus_damage = random.randint(0, user.attack_power*2)
        print(f"{user.name} uses {self.name} to add {bonus_damage} worth of bonus damage to attack")
        user.attack(opponent, (user.attack_power + bonus_damage))

class DivineShield(SpecialAbility):
    def __init__(self):
        super().__init__("Divine Shield")

    def use(self, user, opponent):
        user.shield += user.attack_power
        print(f"{user.name} uses {self.name} to add {user.attack_power} worth of protection to their shield")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)

    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard, player.attack_power)
        elif choice == '2':
            player.special_abilities(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player, wizard.attack_power)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()