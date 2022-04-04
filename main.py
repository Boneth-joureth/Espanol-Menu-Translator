#!/usr/bin/python
#iteration 8
#Importing Librarires

from ntpath import join
from re import I
from typing import List
from googletrans import Translator

#Open Necessary Files for Reading and Writing
inputWords = open("testWords.txt", "r")##@@ change testwords.txt into input.txt when ready to test with your own input.
outputWords = open("translated.txt", "w") #Store the translated words in a txt file so you can access it when needed
outputWordsRead = open("translated.txt", "r")

#init
translator = Translator()

#################################################### translates the words and puts them into another file neatly ####################################################

wordList = inputWords.read().split("\n")

#Translates the words in wordList (Still doesn't work, IDK why?)
for word in wordList:
    word = translator.translate(text=word, src='es', dest='en').text
    print(word)
    outputWords.write(word + "\n")
    print('Writing to file...')

#Closes files
inputWords.close
outputWords.close
