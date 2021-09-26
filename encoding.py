from cryptography.fernet import Fernet

def get_key():
    def generate_new_key():
        key = Fernet.generate_key()
        f = open("key.key","wb")
        f.write(key)
        return key
    
    try:
        f = open("key.key","rb")
        key = f.read()
    except:
        key = generate_new_key()
    return key
        

def encrypt(text):
    key =get_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(text.encode())
    return encMessage


def decrypt(encMessage):
    key =get_key()
    fernet = Fernet(key)
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage
        