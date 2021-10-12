import time, os
from base64 import b64encode, b64decode
from aes import AESEncryption
from aes_manual import AES

def main():
    msg = input("Enter a message: ")

    start_encrypt_time = time.time()
    iv, ciphertext = AESEncryption.encrypt(msg)
    end_encrypt_time = time.time()
    encrypt_time = end_encrypt_time - start_encrypt_time

    start_decrypt_time = time.time()
    decrypted = AESEncryption.decrypt(iv, ciphertext)
    end_decrypt_time = time.time()
    decrypt_time = end_decrypt_time - start_decrypt_time

    print(f"Encrypted with library = {ciphertext}")
    print(f"Decrypted with library = {decrypted}")
    print(f"Encrypt time with library = {encrypt_time}")
    print(f"Decrypt time with library = {decrypt_time}")

    key = os.urandom(16)
    iv = os.urandom(16)

    start_encrypt_time = time.time()
    encrypted = AES(key).encrypt_cbc(msg.encode('utf-8'), iv)
    end_encrypt_time = time.time()
    encrypt_time = end_encrypt_time - start_encrypt_time

    start_decrypt_time = time.time()
    decrypted = AES(key).decrypt_cbc(encrypted, iv)
    end_decrypt_time = time.time()
    decrypt_time = end_decrypt_time - start_decrypt_time

    print(f"Encrypted without library = {b64encode(encrypted).decode('utf-8')}")
    print(f"Decrypted without library = {decrypted.decode('utf-8')}")
    print(f"Encrypt time without library = {encrypt_time}")
    print(f"Decrypt time without library = {decrypt_time}")
    

if __name__ == "__main__":
    main()