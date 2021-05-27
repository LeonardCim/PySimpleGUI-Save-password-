from cryptography.fernet import Fernet


def crypt(cssv_filename):
    '''Function to encrypt the data inside the file'''
    
    with open(r'C:\Users\Utente\Desktop\Save password\key.key', 'rb') as filekey:
        key = filekey.read()
    
    f = Fernet(key)

    with open(cssv_filename, 'rb') as dec_file:
        original = dec_file.read()
        dec_file.close()
    
    encrypted_data = f.encrypt(original)

    with open(cssv_filename, 'wb') as enc_file:
        enc_file.write(encrypted_data)
        enc_file.close()