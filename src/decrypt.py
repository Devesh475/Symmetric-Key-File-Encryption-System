from cryptography.fernet import Fernet
from . import generateKey
import os

# function to decrypt the files
def decryptfile(file,password):
    fileName = ""
    data = ""
    with open(file,'rb') as fileObject:
        data = fileObject.read()
        if(type(file) == bytes):
            newFile = file.decode("utf-8")
            indexOfDot = 0
            for i in range(0,len(newFile)):
                if newFile[i] == '.':
                    indexOfDot = i
            fileName = newFile[:indexOfDot]
        else:
            for i in range(0,len(file)):
                if file[i] == '.':
                    indexOfDot = i
            fileName = file[:indexOfDot]
    os.remove(file)
    with open(fileName,'wb') as fileObject:
        key = generateKey.createKey(password)            
        fernet = Fernet(key)
        decryptedData = fernet.decrypt(data)
        fileObject.write(decryptedData)

def decryptall(files,password):
    for file in files:
        fileName = file.decode("utf-8")
        if fileName[len(fileName) - 4:len(fileName)] == ".enc":
            decryptfile(file,password)