# Symmetric-Key-File-Encryption-System
This is a python script to encrypt files using cryptography fernet which guarantees that a message encrypted using it cannot be manipulated or read without the key.

## How is the encryption process going on : 
* We are creating a key using the Fernet and saving it for the future use
* Next time we run the script we check the password is matched to the created password before 
* If the password is matched we list the menu else we say wrong password
* The encryption and decryption can be performed later 

## Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the cryptography package
```bash
pip install cryptography
```

## How to use
* Put all files in a same folder
* Place your important files in the EncryptedFiles folder
* Copy path of the EncryptedFiles and paste it in the dirPath ('Folder Path')
* Run main.py and encrypt and decrypt using the menu driven process


