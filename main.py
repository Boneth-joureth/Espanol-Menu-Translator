#Importing Librarires

from typing import List
import translators as ts


# Variables
inputWords = open("testWords.txt", "r")##@@ change testwords.txt into input.txt when ready to test with your own input.
inputData = 0 #Reads from inputWords
inputList = 0 #Turns the words into readable 
#Lists

#Read the text File
inputData = inputWords.read()

#Data STR --> LIST
inputList = inputData.split("\n")

#Translate the given words

final_text = ts.google(inputData) # default: from_language='auto', to_language='en'

#Print 
print(inputList)


#Close files
inputWords.close


#Aadesh testing to see if you can see this

