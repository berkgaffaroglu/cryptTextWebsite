from cryptography.fernet import Fernet
def keyReturner(key):
    print(key.decode())
def encryptMessage(givenMessage):
    key = Fernet.generate_key() # generating random key
    encryptedMessage = Fernet(key).encrypt(givenMessage.encode()) # encrypting the message
    keyReturner(key)
    return encryptedMessage.decode()



