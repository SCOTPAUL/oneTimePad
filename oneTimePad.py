#!/usr/bin/python

from functions import *
from string import lower

def menu():
    alpha = enumeratePad()
    message = ""

    choice = raw_input("Type 1 to set a pad, 2 to randomly create one or 3 to import one: ")
    if choice == "1":
        pad = setPad()
        print "Your pad is\n", pad
    elif choice == "2":
        pad = randomPad()
        print "Your pad is\n", pad
    elif choice == "3":
        padFile = raw_input("Enter the file name: ")

        try:
            pad = readInPad(padFile)
            print "Your pad is\n", pad
        except IndexError:
            print "Error: File is empty\n"
            menu()
        except IOError:
            print "Error: No  such file exists in current directory\n"
            menu()
    else:
        print "Error: selection was not 1 or 2\n\n"
        menu()


    print "---------------------------\n"
    choice = (raw_input("Enter 1 to encrypt or 2 to decrypt: "))
    while choice != "q":
        makeChoice(choice, pad, alpha)
        choice = (raw_input("Enter 1 to encrypt or 2 to decrypt: "))


def makeChoice(choice, pad, alpha):
    if choice == "1":
        message = lower(raw_input("Enter a message you wish to encrypt, with no spaces\n"))
        try:
            encryptedMessage = convertMessage(message, pad, alpha)
            print "Encrypted message is as follows\n", encryptedMessage
        except IndexError:
            print "Error: Pad is smaller than message"

    elif choice == "2":
        message = lower(raw_input("Enter a message you wish to decrypt, with no spaces\n"))
        try:
            decryptedMessage = deconvertMessage(message, pad, alpha)
            print "Decrypted message is as follows\n", decryptedMessage
        except IndexError:
            print "Error: Pad is smaller than message"

    else:
        print "Error: selection was not 1 or 2\n\n"

    return choice


def setPad():
    return lower(raw_input("Enter the pad with no spaces\n\n"))


def randomPad():
    length = int(raw_input("Enter the length of the pad you require: "))

    return createPad(length)


#######
menu()
