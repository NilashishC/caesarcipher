#!/usr/bin/python3


"""
------------------------------------------------------------
A simple implementation of Caesar Cipher in Python.
Version : 1.0.0
Written By :  Nilashish C (nilashishchakraborty8@gmail.com)
------------------------------------------------------------

"""

from os import remove
from time import gmtime, strftime


def encrypt(file_name, encrypted_file_name, key, deletesource=False):
    try:
        with open(file_name, 'r') as input_file:
            text = input_file.read()
    except IOError as e:
        print (e)
        print ("\n--------ENCRYPTION FAILED--------\n")

    else:
        try:
            with open(encrypted_file_name, 'w') as output_file:
                result = list()

                print ('[{}]-------ENCRYPTING FILE-------\n'.format(gettime()))

                for i in range(0, len(text)):
                    ch = text[i]

                    if (str.isupper(ch)):
                        e_ch = (ord(ch) + key - 65) % 26 + 65
                        result.append(chr(e_ch))

                    elif (str.islower(ch)):
                        e_ch = (ord(ch) + key - 97) % 26 + 97
                        result.append(chr(e_ch))

                    # For any character in the text
                    else:
                        result.append(ch)

                encrypted_text = "".join(result)
                print (encrypted_text)
                output_file.write(encrypted_text)

                if (deletesource):
                    remove(file_name)

        except IOError as e:
            print (e)
    finally:
        print ('[{}]-----PROGRAM RUN COMPLETE-----'.format(gettime()))


def decrypt(encrypted_file, decrpted_file, key, deletesource=False):
    try:
        with open(encrypted_file, 'r') as input_file:
            text = input_file.read()
    except IOError as e:
        print (e)
        print ("\n--------DECRYPTION FAILED--------\n")

    else:
        try:
            with open(encrypted_file, 'w') as output_file:
                result = list()

                print ('[{}]-------DECRYPTING FILE-------\n'.format(gettime()))

                for i in range(0, len(text)):
                    ch = text[i]

                    if (str.isupper(ch)):
                        dec_ch = (ord(ch) - key - 65) % 26 + 65
                        result.append(chr(dec_ch))

                    elif (str.islower(ch)):
                        dec_ch = (ord(ch) - key - 97) % 26 + 97
                        result.append(chr(dec_ch))
                    else:
                        result.append(ch)

                encrypted_text = "".join(result)
                print (encrypted_text)
                output_file.write(encrypted_text)

                if (deletesource):
                    remove(encrypted_file)

        except IOError as e:
            print (e)
    finally:
        print ('[{}]-----PROGRAM RUN COMPLETE-----'.format(gettime()))


def gettime():
    return(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
