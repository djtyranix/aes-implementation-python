from Crypto.PublicKey import RSA

class RSAEncryption:
    def generate_key(username):
        key = RSA.generate(2048)

        # Generate Private Key
        private_key = key.export_key()
        file_name = username + "-private.pem"
        file_out = open(file_name, "wb")
        file_out.write(private_key)
        file_out.close()

        # Generate Public Key
        public_key = key.publickey().export_key()
        file_name = username + "-public.pem"
        file_out = open(file_name, "wb")
        file_out.write(public_key)
        file_out.close()
