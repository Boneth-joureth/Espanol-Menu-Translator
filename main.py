#Importing Librarires
from ntpath import join
from re import I
from typing import List
import translators as ts
#Variable Definitions:
#These may be helpful if it is necessary to switch y between a vowel and a consonant, also just needed to 
#make things work correctly
vowels = ['a', 'e', 'i', 'o', 'u','í','ó','ú','é']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
htmlInput = open("htmlInput.txt", "w")
outputFile = open("output.txt", "w")

#Function Definitions:

#Handles vowel and consonant counting; I think it's efficient-ish.
def CountVal(word):
    val = 0
    for char in vowels:
        val += word.casefold().count(char)*2
    for char in consonants:
        val += word.casefold().count(char)
    return val

def Translate(inputString):

    inputWords = inputString.split('\n')
    outputWords = ts.google(inputString).split('\n')
    outputString = ""

    outputString += "Spanish: \n"
    for word in inputWords:
        outputString += word + " " + str(CountVal(word)) + '\n'

    outputString += "\n English: \n"
    for word in outputWords:
        outputString += word + " " + str(CountVal(word)) + '\n'

    return outputString
