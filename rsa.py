from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP

class RSAEncryption:
    def generate_key(username):
        key = RSA.generate(2048)

        # Generate Private Key
        private_key = key.export_key()
        file_name = username.lower() + "-private.pem"
        file_out = open(file_name, "wb")
        file_out.write(private_key)
        file_out.close()

        # Generate Public Key
        public_key = key.publickey().export_key()
        file_name = username.lower() + "-public.pem"
        file_out = open(file_name, "wb")
        file_out.write(public_key)
        file_out.close()

    def get_session_key(username):
        file_name = username + "-public.pem"
        public_key = RSA.import_key(open(file_name).read())
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(public_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        return enc_session_key, session_key

    def decrypt_session_key(username, enc_session_key):
        file_name = username + "-private.pem"
        private_key = RSA.import_key(open(file_name).read())

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        return session_key