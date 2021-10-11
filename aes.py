from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad

ezkey = b"e820nf0ndnk3idm2"

class AESEncryption:
    def encrypt(msg):
        cipher = AES.new(ezkey, AES.MODE_CBC)
        cipher_bytes = cipher.encrypt(pad(msg.encode('utf-8'), AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ciphertext = b64encode(cipher_bytes).decode('utf-8')
        return iv, ciphertext

    def decrypt(iv, ciphertext):
        cipher_bytes = b64decode(ciphertext)
        iv_decode = b64decode(iv)
        cipher = AES.new(ezkey, AES.MODE_CBC, iv_decode)
        plaintext = cipher.decrypt(cipher_bytes)
        return unpad(plaintext, AES.block_size)