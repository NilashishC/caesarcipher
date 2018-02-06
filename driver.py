"""

A demo driver file for Caesar Cipher module

"""

import caesarcipher

caesarcipher.encrypt('<enter full path of plain text file>',
                     '<enter fullpath of encrypted file>',
                     key, deletefile=False[True]) # setting deletefile=True deletes the plain text file

caesarcipher.decrypt('<enter fullpath of encrypted file>',
                     '<enter fullpath of decrypted file>',
                     key, deletefile=False[True]) # setting deletefile=True deletes the encrypted text file

