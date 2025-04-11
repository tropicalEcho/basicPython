import os, random, sys, time

helpText = """
COMMANDS:
    CLEAR | CLS - Cleans Everything...
    EXIT | QUIT - Kills rpsls.py!
    HELP        - Prints this.
    SHELDON     - Summons Sheldon Lee Cooper?!
    SCORE       - Displays the current scoreboard.
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

p1Score = 0
p2Score = 0

single = False

CHARACTERS = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]
COMMANDS = ["CLEAR", "CLS", "EXIT", "QUIT", "HELP", "MANUAL", "SHELDON", "GUIDE", "SCORE", "SCOREBOARD", "RANK", "TALLY", "COUNT"]

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
    global p1Score, p2Score, single
    if cmd in {"CLEAR", "CLS"}:
        clear()
    elif cmd in {"EXIT", "QUIT"}:
        sys.exit("GOODBYE!")
    elif cmd == "SHELDON":
        print(sheldonHelp)
    elif cmd == "HELP":
        print(helpText)
    elif cmd in {"SCORE", "SCOREBOARD", "RANK", "TALLY", "COUNT"}:
        if single:
            print(f"YOU: {p1Score}\nCOMPUTER: {p2Score}")
        else:
            print(f"PLAYER 1: {p1Score}\nPLAYER 2: {p2Score}")
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
    global p1Score, p2Score
    if single:
        time.sleep(random.uniform(0.6, 1.6))
        print(f"COMPUTER: {player2}")
    
    time.sleep(random.uniform(0.01, 0.4))
    
    if player1 == player2:
        print("TIE!\n")
    elif player2 in WINS[player1]:
        if single:
            print("YOU WON!\n")
        else:
            print("PLAYER 1 WON!\n")
        p1Score += 1
    else:
        if single:
            print("YOU LOST!\n")
        else:
            print("PLAYER 2 WON!\n")
        p2Score += 1

def main():
    global p1Score, p2Score, single
    clear()
    while True:
        p1Score = 0
        p2Score = 0
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
                playerChoice = getChoice("PLAYER: ")
                computerChoice = random.choice(CHARACTERS)
                playGame(playerChoice, computerChoice, True)
                print(f"You: {p1Score}; Computer: {p2Score}\n")
            else:
                player1Choice = getChoice("PLAYER 1: ")
                clear()
                player2Choice = getChoice("PLAYER 2: ")
                clear()
                playGame(player1Choice, player2Choice, False)
                print(f"Player 1: {p1Score}; Player 2: {p2Score}\n")

if __name__ == "__main__":
    main()