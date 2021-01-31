from cryptography.fernet import Fernet
import os
from . import generateKey 

# function to encrypt the files
def encryptfile(file,password):
    with open(file,'rb') as fileObject:
        data = fileObject.read()
    
    with open(file + ".enc".encode("utf-8"),'wb') as fileObject:
        key = generateKey.createKey(password)
        fernet = Fernet(key)
        encryptedData = fernet.encrypt(data)
        fileObject.write(encryptedData)
    
    os.remove(file)

def encryptall(files,password):
    for file in files:
        fileName = file.decode("utf-8")
        if fileName[len(fileName) - 4:len(fileName)] != ".enc":
            encryptfile(file,password)