from ecdsa import SigningKey, BadSignatureError
import shamirs
import random

class Key:
    def __init__(self):
        self.id=-1
        print("key instance made")

    def generateKey(self):
        sk = SigningKey.generate() # uses NIST192p
        vk = sk.verifying_key
        #with open("private.pem", "wb") as f:   # ako budem trebal spremiti na disk
        #    f.write(self.sk.to_pem())
        #with open("public.pem", "wb") as f:
        #    f.write(self.vk.to_pem())

        sk_int = int.from_bytes(sk.to_string(), byteorder='big')

        silly_big_prime= 5210644015679228794060694325390955853335898483908056458352183851018372555735221

        ss = shamirs.shares(sk_int, quantity=5, modulus=silly_big_prime, threshold=3)

        ss64=[]
        for s in ss:
            ss64.append(s.to_base64())
            #print(s.to_base64())

        del sk, sk_int, ss

        return ss64
        


        #with open("share1.txt", "w") as f:   # ako budem trebal spremiti na disk
        #   f.write(self.ss[0].to_base64())


        #ii1=self.ss[0].to_base64()
        #ii2=self.ss[1].to_base64()
        #ii3=self.ss[2].to_base64()
        #ii4=self.ss[3].to_base64()
        #ii5=self.ss[4].to_base64()

        #li1=shamirs.share.from_base64(ii1)
        #li2=shamirs.share.from_base64(ii2)
        #li3=shamirs.share.from_base64(ii3)
        #li4=shamirs.share.from_base64(ii4)
        #li5=shamirs.share.from_base64(ii5)
        

        #print(shamirs.interpolate(lll[0:4],threshold=3))

    def sign(self,message):   #ocekujem string
        byteString = message.encode()
        signature = self.sk.sign(byteString)
        self.signature=signature
        return signature

    def verify(self, signature, message):
        byteString = message.encode()
        try:
             self.vk.verify(signature, byteString)
             return True
        except BadSignatureError:
             return False




#k1=Key()
#keyId=k1.generateKey()
#sig=k1.sign("bok")

#print(k1.sk.to_string())
#temp=int.from_bytes(sk.to_string(), byteorder='big')
#print(temp)
#temp2=temp.to_bytes(24,'big')
#print(temp2)

#print(sig)
#print(k1.verify(sig,"bok"))




