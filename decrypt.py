from cryptography.fernet import Fernet


def decrypt():
    '''Function to decrypt the data inside the file'''

    with open(r'C:\Users\Utente\Desktop\Save password\key.key', 'rb') as filekey:
        key = filekey.read()
        filekey.close

        f = Fernet(key)

        with open(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv', 'rb') as enc_file:
            encrypted = enc_file.read()
            enc_file.close()

        decrypted = f.decrypt(encrypted) 

        with open(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv', 'wb') as dec_file:
            dec_file.write(decrypted)
            dec_file.close()
