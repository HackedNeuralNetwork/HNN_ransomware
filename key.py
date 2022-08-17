#!/usr/bin/env python3

from Crypto.PublicKey import RSA
import binascii

keyPair = RSA.generate(3072)
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
with open('public.pem','wb') as f:
    f.write(pubKeyPEM)
privKeyPEM = keyPair.exportKey()
with open('private.pem','wb') as f:
        f.write(privKeyPEM)
