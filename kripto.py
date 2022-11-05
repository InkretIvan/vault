from ecdsa import SigningKey

sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
assert vk.verify(signature, b"message")

print("hello")