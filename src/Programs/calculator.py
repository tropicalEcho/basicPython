import math, os, sys

helpText = """
COMMANDS:
    HELP        - Prints this.
    CLEAR | CLS - Cleans Everything...
    EXIT | QUIT - Kills calculator.py!
CALCULATOR:
    <EXPRESSION> - Compute the given expression.
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    while True:
        userInput = input("~/calculator$ ").strip()
        cmd = userInput.split()[0].upper()
        if cmd in {"CLS", "CLEAR"}:
            clear()
        elif cmd in {"EXIT", "QUIT"}:
            sys.exit("GOODBYE!")
        elif cmd in {"HELP"}:
            print(helpText)
        else:
            try:
                print(eval(userInput))
            except SyntaxError:
                print("AN ERROR OCCURRED! NAMELY? SYNTACTICAL ERROR.")
            except NameError:
                print("AN ERROR OCCURRED! NAMELY? NAME ERROR.")
            except IndexError:
                print("AN ERROR OCCURRED! NAMELY? INDEX ERROR.")
            except:
                print("AN UNKNOWN ERROR OCCURRED!")

if __name__ == "__main__":
    main()