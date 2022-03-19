#iteration 4

#Importing Librarires

from ntpath import join
from typing import List
import translators as ts


# Variables
inputWords = open("testWords.txt", "r")##@@ change testwords.txt into input.txt when ready to test with your own input.
inputData = 0 #Reads from inputWords
inputList = 0 #Turns the words into readable 
transStore = open("translated.txt", "w") #Store the translated words in a txt file so you can access it when needed
transRead = open("translated.txt", "r") # open the translated texts # read the translated texts
transText = 0 # translated text
sepText = list() #seperates the texts
#Lists

#Read the text File
inputData = inputWords.read()
#Data STR --> LIST
inputList = inputData.split("\n")




#Translate the words in inputList
transText = ts.google(inputData) # default: from_language='auto', to_language='en'




#seperate the texts
transText = transText.split('\n')

#Remove white spaces
[i.strip() for i in transText]

sepText = transText




# List --> translated.txt
for word in transText:
    transStore.write(word + "\n")
    




#Print 
print(transText[1])

#Close files
inputWords.close
transStore.close

#Aadesh testing to see if you can see this

