from characters import Warrior, Mage, Archer, Paladin

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

def battle(players, wizard):
    total_player_count = len(players)
    turn = 1
    while wizard.health > 0 and total_player_count > 0:
        if turn > total_player_count:
            turn = 1
        player = players[turn-1]
        print(f"\n --- {player.name}'s turn ---")
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
            wizard.generate_minions()

        if player.health <= 0:
            del players[turn-1]
            total_player_count = len(players)
        turn += 1

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated with {player.name} landing the final blow!")
    else:
        print(f"The wizard {wizard.name} has defeated all players!")