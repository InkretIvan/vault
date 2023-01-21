from modules.database import *

def printHelp():
    print("-help")
    print("  shows this list")
    print("-exit")
    print("  terminates the program")

def main():
    print("\nType 'help' for available commands")
    while True:
        inp1=input()
        inp2=inp1.split()
        comm=inp2[0]
        match comm:
            case "help":
                printHelp()

            case "nodestatus":
                print("status")

            case "exit":
                break

            case _:
                print("I don't recognize this command, type 'help' for available commands")
        

        

main()