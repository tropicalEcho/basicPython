import os, sys

helpText = """
COMMANDS:
    HELP        - Prints this.
    CLEAR | CLS - Cleans Everything...
    EXIT | QUIT - Kills morseTranslator.py!
MORSE:
    <TEXT>  - Translates to Morse code.
    <MORSE> - Translates to Regular English Text.
"""

morseDict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
    '/': '-..-.', '-': '-....-', '"': '.-..-.', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '_': '..--.-', '@': '.--.-.'
}

morseDictRev = {v: k for k, v in morseDict.items()}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def translate(userInput):
    words = userInput.split(" / ")
    isMorse = True
    for word in words:
        codes = word.split()
        if not all(code in morseDictRev for code in codes):
            isMorse = False
            break
    if isMorse:
        translatedWords = [''.join(morseDictRev[code] for code in word.split()) for word in words]
        print(f"TEXT: {' '.join(translatedWords)}")
    else:
        translatedWords = [' '.join(morseDict.get(char.upper(), '') for char in word) for word in userInput.split()]
        print(f"MORSE: {' / '.join(translatedWords)}")

def main():
    clear()
    while True:
        userInput = input("~/morseTranslator$ ").strip()
        cmd = userInput.split()[0].upper()
        if cmd in {"CLS", "CLEAR"}:
            clear()
        elif cmd in {"EXIT", "QUIT"}:
            sys.exit("GOODBYE!")
        elif cmd in {"HELP"}:
            print(helpText)
        else:
            translate(userInput)
                
if __name__ == "__main__":
    main()