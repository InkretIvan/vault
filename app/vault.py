from modules.database import *
from modules.kripto import *

database = db()       

def printHelp():
    print("-help")
    print("  shows this list")
    print("-exit")
    print("  terminates the program")

def main():
    print("Type 'help' for available commands")
    while True:
        inp1=input()
        inp2=inp1.split()
        comm=inp2[0]
        match comm:
            case "help":
                printHelp()

            case "nodestatus":
                print("status")

            case "generate":
                newKey = Key()
                randId=random.randint(100000,999999)
                ss = newKey.generateKey()

                check=database.saveFragments(randId,ss)
                Key.id=randId


                if check==0:
                    print("Key could not be generated")
                else:
                    print("New key with id ", randId," generated")

            case "exit":
                database.closeTheDB()
                break

            case _:
                print("I don't recognize this command, type 'help' for available commands")
        


main()