from ecdsa import SigningKey, VerifyingKey, BadSignatureError
from modules.database import *
from modules.kripto import *

database = db()  

def printHelp():
    print("-help")
    print("  shows this list")
    print("-generate")
    print("  generates a new key and returns its id, generates a file of the public key")
    print("  please write down the id!")
    print("-sign [id] [message.txt]")
    print("  signs the message with the key [id] belongs to")
    print("  example: sign 123456 text.txt")
    print("-purge")
    print("  deletes all keys from the database")
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

            case "test": #just for testing purposes
                id=int(inp2[1])
                strs=database.retrieveKeyById(id)
                sms=[]
                for s in strs:
                    sms.append(shamirs.share.from_base64(s))
                sk_int=shamirs.interpolate(sms,threshold=3)
                sk_bytes=sk_int.to_bytes(24,'big')
                sktest=SigningKey.from_string(sk_bytes)
                vktest=sktest.verifying_key
                with open("test.pem", "wb") as f:
                        f.write(vktest.to_pem())
               

            case "purge":
                database.purgeDB()

            case "sign":
                id=int(inp2[1])

                messagepath=inp2[2]

                with open(messagepath, "r") as f:   
                    message=f.read()

                strs=database.retrieveKeyById(id)
                if strs==0:
                    print("Too many nodes are down, key can not be retreived")
                    continue
                sms=[]
                for s in strs:
                    sms.append(shamirs.share.from_base64(s))
                sk_int=shamirs.interpolate(sms,threshold=3)
                sk_bytes=sk_int.to_bytes(24,'big')
                sk_reconstructed=SigningKey.from_string(sk_bytes)

                #signature=recKey.sign(sk_reconstructed,message)
                signature=sk_reconstructed.sign(message.encode())
                
                with open("signed_"+messagepath, "a") as f:   
                    f.write(message)
                    f.write("\n")
                
                with open("signed_"+messagepath, "ab") as f:   
                    f.write(signature)




            case "generate":
                newKey = Key()
                randId=random.randint(100000,999999)
                ss = newKey.generateKey()

                check=database.saveFragments(randId,ss[1])
                vk=ss[0]
                Key.id=randId

                if check==0:
                    print("Key could not be generated")
                else:
                    publicFileName="public"+str(randId)+".pem"
                    with open(publicFileName, "wb") as f:
                        f.write(vk.to_pem())
                    print("New key with id ", randId," generated")

            case "exit":
                database.closeTheDB()
                break

            case _:
                print("I don't recognize this command, type 'help' for available commands")
        


main()