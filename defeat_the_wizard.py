from helper import create_character, battle
from characters import EvilWizard

def main():
    total_players = input("Choose how many players: ")
    players = []
    for n in range(int(total_players)):
        player = create_character()
        players.append(player)
    wizard = EvilWizard("The Dark Wizard")
    battle(players, wizard)

if __name__ == "__main__":
    main()