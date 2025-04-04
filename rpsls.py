import os, random, sys, time

helpText = """
COMMANDS:
    CLEAR | CLS - Cleans Everything...
    EXIT | QUIT - Kills rpsls.py!
    HELP        - Prints this.
    SHELDON     - Summons Sheldon Lee Cooper?!
GAME MODES:
    MONO - Play against randomness.
    DUO  - Play against another player.
"""
sheldonHelp = """
SCISSORS cuts PAPER
PAPER covers ROCK
ROCK crushes LIZARD
LIZARD poisons SPOCK
SPOCK smashes SCISSORS
SCISSORS decapitates LIZARD
LIZARD eats PAPER
PAPER disproves SPOCK
SPOCK vaporizes ROCK
and as it always has
ROCK crushes SCISSORS
"""

CHARACTERS = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]
COMMANDS = ["CLEAR", "CLS", "EXIT", "QUIT", "HELP", "MANUAL", "SHELDON", "GUIDE"]

WINS = {
    "ROCK": ["SCISSORS", "LIZARD"],
    "PAPER": ["ROCK", "SPOCK"],
    "SCISSORS": ["PAPER", "LIZARD"],
    "LIZARD": ["PAPER", "SPOCK"],
    "SPOCK": ["SCISSORS", "ROCK"]
}

def clear(): 
    os.system("cls" if os.name == "nt" else "clear")

def handleCommands(cmd):
    if cmd in {"CLEAR", "CLS"}:
        clear()
    elif cmd in {"EXIT", "QUIT"}:
        sys.exit("GOODBYE!")
    elif cmd == "SHELDON":
        print(sheldonHelp)
    elif cmd == "HELP":
        print(helpText)
    else:
        return False
    return True

def getChoice(prompt):
    while True:
        choice = input(prompt).strip().upper()
        if handleCommands(choice):
            continue
        if choice in CHARACTERS:
            return choice
        print("ERROR: INVALID CHOICE!")

def playGame(player1, player2, single):
    if single:
        time.sleep(random.uniform(0.6, 1.6))
        print(f"COMPUTER: {player2}")
    
    time.sleep(random.uniform(0.01, 0.4))
    
    if player1 == player2:
        result = "TIE!"
    elif player2 in WINS[player1]:
        result = "YOU WON!" if single else "PLAYER 1 WON!"
    else:
        result = "YOU LOST!" if single else "PLAYER 2 WON!"
    
    print(f"{result}\n")

def main():
    clear()
    while True:
        mode = input("SINGLE | MULTI: ").strip().upper()
        if handleCommands(mode):
            continue
            
        single = mode in ["SINGLE", "1", "ONE", "MONO"]
        multi  = mode in ["MULTI", "2", "TWO", "BI", "DUO"]
        
        if not (single or multi):
            print("ERROR: INVALID CHOICE!")
            continue

        while True:
            if single:
                player1 = getChoice("PLAYER: ")
                computer = random.choice(CHARACTERS)
                playGame(player1, computer, True)
            else:
                player1 = getChoice("PLAYER 1: ")
                clear()
                player2 = getChoice("PLAYER 2: ")
                clear()
                playGame(player1, player2, False)

if __name__ == "__main__":
    main()