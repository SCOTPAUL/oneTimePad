#!/usr/bin/python

from random import randint

def enumeratePad():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alphaDict = {}
    n = 0

    for char in alpha:
        alphaDict[char] = n
        n += 1

    return alphaDict


def finalNumber(textNum, keyNum):
    return (textNum + keyNum)%26


def reversedNumber(textNum, keyNum):
    return (textNum - keyNum)%26


def createPad(length):
    n = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pad = ""

    while n < length:
        pad += alpha[randint(0, 25)]
        n += 1

    return pad


def convertMessage(message, pad, enumerated):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    n = 0
    encrypted = ""
    while n < len(message):
        if message[n] in alpha:
            messageNum = enumerated[message[n]]
            padNum = enumerated[pad[n]]
            encryptedNum = finalNumber(messageNum, padNum)
            encryptedChar = alpha[encryptedNum]
            encrypted += encryptedChar
        else:
            encrypted += message[n]
        n += 1

    return encrypted


def deconvertMessage(converted, pad, enumerated):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    n = 0
    decrypted = ""

    while n < len(converted):
        if converted[n] in alpha:
            messageNum = enumerated[converted[n]]
            padNum = enumerated[pad[n]]
            encryptedNum = reversedNumber(messageNum, padNum)
            encryptedChar = alpha[encryptedNum]
            decrypted += encryptedChar
        else:
            decrypted += converted[n]
        n += 1

    return decrypted


