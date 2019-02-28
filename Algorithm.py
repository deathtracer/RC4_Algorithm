#!/usr/bin/Python3
#
# Author : Shivam Goel  ; Date : March 1, 2019
#
# Description : RC4 implementation in Python
# Reference : Cryptography and Network Security by William Stallings
#
# IDE : Pycharm
#============================================================================

# Global variables
s = [None] * 256
p = q = None

def setKey(key):
    ##RC4 Key Scheduling Algorithm
    global p, q, s
    s = [n for n in range(256)]
    p = q = j = 0
    for i in range(256):
        if len(key) > 0:
            j = (j + s[i] + key[i % len(key)]) % 256
        else:
            j = (j + s[i]) % 256
    s[i], s[j] = s[j], s[i]

def byteGenerator():
    ##RC4 Pseudo-Random Generation Algorithm
    global p, q, s
    p = (p + 1) % 256
    q = (q + s[p]) % 256
    s[p], s[q] = s[q], s[p]
    return s[(s[p] + s[q]) % 256]

def encrypt(key,inputString):
    ##Encrypt input string returning a byte list
    setKey(string_to_list(key))
    return [ord(p) ^ byteGenerator() for p in inputString]

def decrypt(inputByteList):
    ##Decrypt input byte list returning a string
    return "".join([chr(c ^ byteGenerator()) for c in inputByteList])



def intToList(inputNumber):
    ##Convert a number into a byte list
    inputString = "{:02x}".format(inputNumber)
    return [int(inputString[i:i + 2], 16) for i in range(0, len(inputString), 2)]

def string_to_list(inputString):
    ##Convert a string into a byte list
    return [ord(c) for c in inputString]




loop = 1
while loop == 1: #simple loop to always bring the user back to the menu

    print("RC4 Encryptor/Decryptor")
    print
    print("Please choose an option from the below menu")
    print
    print("1) Encrypt")
    print("2) Decrypt")
    print

    choice = input("Choose your option: ")
    choice = int(choice)

    if choice == 1:
        key = input("Enter Key: ")
        inputstring = input("enter plaintext: ")
        encrypt(key, inputstring)


    elif choice == 2:
        key = input("Enter Key: ")
        ciphertext = input("enter Ciphertext: ")
        print (decrypt(intToList(ciphertext))

    #elif choice == 3:
    #returns the user to the previous menu by ending the loop and clearing the screen.
     #   loop = 0

    #else :
      #  print ("please enter a valid option") #if any NUMBER other than 1, 2 or 3 is entered.