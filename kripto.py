from ecdsa import SigningKey

sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
#print(signature.decode())
assert vk.verify(signature, b"message")


class Kripto:
    def __init__(self):
        self.sk = SigningKey.generate() # uses NIST192p
        self.vk = sk.verifying_key

    def sign(self,message):   #ocekujem string
        byteString = bytes(message, 'utf-8')
        signature = sk.sign(byteString)
        self.signature=signature
        return signature

    def verify(self, signature, message):
        byteString = bytes(message, 'utf-8')
        print(vk.verify(signature, byteString))

k1=Kripto()
sig=k1.sign("bok")
print(sig)
k1.verify(sig,"bok")




