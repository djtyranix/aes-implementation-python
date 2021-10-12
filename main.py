import time
from aes import AESEncryption

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

    print(f"Encrypted = {ciphertext}")
    print(f"Decrypted = {decrypted}")
    print(f"Encrypt time = {encrypt_time}")
    print(f"Decrypt time = {decrypt_time}")
    

if __name__ == "__main__":
    main()