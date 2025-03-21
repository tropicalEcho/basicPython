import os, sys, string, random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

helpText = """
COMMANDS:
  HELP            - Prints this.
  CLEAR | CLS     - Cleans everything...
  EXIT | QUIT     - Kills passManager.py!

PASSWORD:
  PASS | NEW      - Generate a random password.
    -S <STRENGTH> - Strength: STRONG | MEDIUM | WEAK.
    -L <LENGTH>   - Length: 4-25.
    -R            - Presence = Repetition, and vise-versa.

  RP <PASSWORD>   - Rate given password strength!
"""

def parseArg(uiParts):
    strength = "STRONG"
    length = 12 
    rep = False

    for i in range(len(uiParts)):
        if uiParts[i].upper() == "-S" and i + 1 < len(uiParts):
            strength = uiParts[i + 1].upper()
        elif uiParts[i].upper() == "-L" and i + 1 < len(uiParts):
            if uiParts[i + 1].isdigit():
                length = int(uiParts[i + 1])
                if length < 4:
                    length = 4
                elif length > 25:
                    length = 25
            else:
                print("INVALID LENGTH! SETTING TO 12.")
        elif uiParts[i].upper() == "-R":
            rep = True

    return strength, length, rep

def generate(strength, count, rep):
    upperL = list(string.ascii_uppercase)
    lowerL = list(string.ascii_lowercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    allChars = upperL + lowerL + digits + symbols

    if strength in {"STRONG", "S", "STR", "EVERYTHING", "ET"}:
        pool = allChars
    elif strength in {"MID", "MED", "MOD", "MODERATE", "MEDIUM", "MIDDLE", "OKAY"}:
        pool = upperL + lowerL + digits
    elif strength == "WEAK":
        pool = upperL + lowerL
    else:
        print("ERROR! INVALID STRENGTH.")
        return None
    
    if count > len(pool) and not rep:
        print("ERROR! CANNOT GENERATE NON-REPEATING PASSWORD OF THIS LENGTH.")
        return None

    password = "".join(random.choices(pool, k=count)) if rep else "".join(random.sample(pool, count))
    return password

def ratePass(password):
    length = len(password)
    hasUpper = any(c.isupper() for c in password)
    hasLower = any(c.islower() for c in password)
    hasDigit = any(c.isdigit() for c in password)
    hasSymbol = any(c in string.punctuation for c in password)

    score = sum([hasUpper, hasLower, hasDigit, hasSymbol])

    return "STRONG" if length >= 12 and score == 4 else "MEDIUM" if length >= 8 and score >= 3 else "WEAK"

def main():
    clear()
    while True:
        userInput = input("~\\passManager$ ").strip()
        if not userInput:
            continue

        uiParts = userInput.split()
        cmd = uiParts[0].upper()

        if cmd in {"CLS", "CLEAR"}:
            clear()
        elif cmd in {"EXIT", "QUIT"}:
            sys.exit("GOODBYE!")
        elif cmd in {"HELP"}:
            print(helpText)
        elif cmd in {"NEW", "PASS", "GENERATE", "GEN"}:
            strength, length, rep = parseArg(uiParts)
            password = generate(strength, length, rep)
            if password:
                print(f"PASSWORD: {password}")
        elif cmd in {"RP", "RATE"}:
            if len(uiParts) < 2:
                print("ERROR! PLEASE PROVIDE A PASSWORD TO RATE.")
            else:
                rating = ratePass(" ".join(uiParts[1:]))
                print(f"PASSWORD STRENGTH: {rating}")
        else:
            print(f"INVALID COMMAND '{cmd}'")
            continue
if __name__ == "__main__":
    main()
