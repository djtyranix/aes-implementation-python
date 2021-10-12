import aes, os
key = os.urandom(16)
iv = os.urandom(16)
encrypted = aes.AES(key).encrypt_ctr(b'Attack at dawn', iv)
print(aes.AES(key).decrypt_ctr(encrypted, iv))
# b'Attack at dawn'
