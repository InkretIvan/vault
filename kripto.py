from ecdsa import SigningKey, BadSignatureError

class Kripto:
    def __init__(self):
        self.sk = SigningKey.generate() # uses NIST192p
        self.vk = self.sk.verifying_key
       # with open("private.pem", "wb") as f:
       #     f.write(sk.to_pem())
       # with open("public.pem", "wb") as f:
       #     f.write(vk.to_pem())

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

k1=Kripto()
sig=k1.sign("bok")
print(int.from_bytes(k1.sk.to_string(), byteorder='big'))
print(int.from_bytes(k1.vk.to_string(), byteorder='big'))
print(sig)
print(k1.verify(sig,"bok"))




