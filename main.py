import os
import time
from src import encrypt as e
from src import decrypt as d

dirPath = b' Folder Path '

def getAllFiles(dirPath):
    files = [dirPath + "\\".encode("utf-8") + file for file in os.listdir(dirPath)]
    return files


def main():
    # if a user exist with some password
    if os.path.isfile('data.txt.enc'):
        password = input('Enter a password to login into file encryption system : ')
        d.decryptfile("data.txt.enc",password)
        with open('data.txt','rb') as fileObject:
            data = fileObject.read()
            userExist = False
            if data.decode("utf-8") == password:
                userExist = True
            else:
                print("Incorrect Password")
        
        if userExist:
            e.encryptfile("data.txt".encode("utf-8"),password)
            print("Enter 1 to encrypt")
            print("Enter 2 to decrypt")
            print("Enter 3 to encrypt all files")
            print("Enter 4 to decrypt all files")
            print("Enter 5 to exit")
            choice = int(input("Enter your choice : "))

            if choice == 1:
                file = input("Enter a file name : ")
                files = getAllFiles(dirPath)
                found = False
                #print(dirPath + "\\".encode("utf-8") + file.encode("utf-8"))
                for availableFiles in files:
                    if availableFiles == dirPath + "\\".encode("utf-8") + file.encode("utf-8"):
                        found = True
                        break
                if not found:
                    print("File not found")
                else:
                    e.encryptfile(dirPath + '\\'.encode("utf-8") + file.encode("utf-8"),password)

            elif choice == 2:
                file = input("Enter a file name : ")
                files = getAllFiles(dirPath)
                found = False
                for availableFiles in files:
                    if availableFiles == dirPath + "\\".encode("utf-8") + file.encode("utf-8"):
                        found = True
                        break
                if not found:
                    print("File not found")
                else:
                    d.decryptfile(dirPath + '\\'.encode("utf-8") + file.encode("utf-8"),password)
            elif choice == 3:
                files = getAllFiles(dirPath)
                e.encryptall(files,password)
            elif choice == 4:
                files = getAllFiles(dirPath)
                d.decryptall(files,password)
            elif choice == 5:
                exit()
            else:
                print("Wrong choice")

    # if the program is run for the first time then the password is created to protect the files
    else:
        password = ''
        while True:
            password = input('Enter a password to protect your files : ')
            repassword = input('Confirm your password : ')
            if password == repassword:
                break
            else:
                print("Password didn't match")
        

        with open("data.txt",'wb') as fileObject:
            fileObject.write(password.encode("utf-8"))
        
        e.encryptfile("data.txt".encode("utf-8"),password)
            #encryptfile("password.txt")
        # encrypt the password file

        print("Restart the program to start encrypting and decrypting")
        time.sleep(15)


if __name__ == '__main__':
    main()
