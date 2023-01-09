from ecdsa import SigningKey, BadSignatureError
import shamirs

class Korisnik:
    def __init__(self):
        self.sk = SigningKey.generate() # uses NIST192p
        self.vk = self.sk.verifying_key
       # with open("private.pem", "wb") as f:   ako budem trebal spremiti na disk
       #     f.write(sk.to_pem())
       # with open("public.pem", "wb") as f:
       #     f.write(vk.to_pem())

        sk_int = int.from_bytes(self.sk.to_string(), byteorder='big')

        silly_big_prime= 5210644015679228794060694325390955853335898483908056458352183851018372555735221

        self.ss = shamirs.shares(sk_int, quantity=5, modulus=silly_big_prime, threshold=3)

        for i in self.ss:
            print(i)

        print(shamirs.interpolate(self.ss[0:3],threshold=3))



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




k1=Korisnik()
sig=k1.sign("bok")

#print(k1.sk.to_string())
temp=int.from_bytes(k1.sk.to_string(), byteorder='big')
print(temp)
#temp2=temp.to_bytes(24,'big')
#print(temp2)

#print(sig)
#print(k1.verify(sig,"bok"))




