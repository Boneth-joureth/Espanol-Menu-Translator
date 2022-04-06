#Importing Librarires
from ntpath import join
from re import I
from typing import List
import translators as ts

#Open Necessary Files for Reading and Writing
inputFile = open("input.txt", "r")##@@ change testwords.txt into input.txt when ready to test with your own input.
outputFile = open("output.txt", "w+") #Store the translated words in a txt file so you can access it when needed

#Variable Definitions:
#These may be helpful if it is necessary to switch y between a vowel and a consonant, also just needed to 
#make things work correctly
vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

inputVals = []
outputVals = []

#Function Definitions:

#Handles vowel and consonant counting; I think it's efficient-ish.
def CountVal(word):
    val = 0
    for char in vowels:
        val += word.casefold().count(char)*2
    for char in consonants:
        val += word.casefold().count(char)
    return val

inputString = inputFile.read()
inputWords = inputString.split('\n')
outputWords = ts.google(inputString).split('\n')

for word in inputWords:
    inputVals.append(CountVal(word))

for word in outputWords:
    outputVals.append(CountVal(word))

#Writes all results to the output file in a neat format:
outputFile.write("Spanish: \n")
for i in range(len(inputWords)):
    print(inputWords[i] + " " + str(inputVals[i]))
    outputFile.write(inputWords[i] + " " + str(inputVals[i]) + '\n')
outputFile.write("English: \n")
for i in range(len(outputWords)):
    print(outputWords[i] + " " + str(outputVals[i]))
    outputFile.write(outputWords[i] + " " + str(outputVals[i]) + '\n')
    
#Closes files
inputFile.close
outputFile.close