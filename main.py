from aes import AESEncryption

def main():
    msg = input("Enter a message: ")
    iv, ciphertext = AESEncryption.encrypt(msg)
    decrypted = AESEncryption.decrypt(iv, ciphertext)

    print(f"Encrypted = {ciphertext}")
    print(f"Decrypted = {decrypted.decode('utf-8')}")
    

if __name__ == "__main__":
    main()