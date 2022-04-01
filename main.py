#iteration 8

#Importing Librarires

from ntpath import join
from re import I
from typing import List
import translators as ts
#from tkinter import *
#import tkinter as tk

# Variables
inputWords = open("testWords.txt", "r")##@@ change testwords.txt into input.txt when ready to test with your own input.
inputData = 0 #Reads from inputWords
inputList = 0 #Turns the words into readable 
transStore = open("translated.txt", "w") #Store the translated words in a txt file so you can access it when needed
transRead = open("translated.txt", "r") # open the translated texts # read the translated texts
transText = 0 # translated text
preVal = list() #value of words before translated as a list
preLet = list() #letter thing
val_calc = 0 #value of idk

preVal2 = list() #value of words after translated as a list
preLet2 = list() #letter thing 2
val_calc2 = 0 #value of idk 2
#counters
c1 = 0
c2 = 0
#Lists
list_int = list() # pre val summed up
final_val = list() #pre traslated total val each word into own list

list_int2 = list() # post val summed up
final_val2 = list() #post traslated total val each word into own list

#################################################### translates the words and puts them into another file neatly ####################################################


#Read the text File
inputData = inputWords.read()
#Data STR --> LIST
inputList = inputData.split("\n")




#Translate the words in inputList
transText = ts.google(inputData) # default: from_language='auto', to_language='en'


#length of text
lenText = len(transText)

#seperate the texts
transText = transText.split('\n')

#Remove white spaces
transText = [i.strip(' ') for i in transText]

    
sepText = transText




# List --> translated.txt
for word in transText:
    transStore.write(word + "\n")
    




#Print 


#Close files
inputWords.close
transStore.close
transRead.close
#Aadesh testing to see if you can see this

#inputList is the one with the pre translated words in a list


#################################################### calculates the value of the pre translated words ####################################################

while len(inputList) != val_calc:
    for x in inputList[0 + val_calc]:
        preLet.append(ord(x) - 96)
    
    while len(preLet) != c1:
        
        if preLet[c1] == 1:
            preVal.insert(c1, "2")
        elif preLet[c1] == 5:
            preVal.insert(c1, "2")
        elif preLet[c1] == 9:
            preVal.insert(c1, "2")
        elif preLet[c1] == 15:
            preVal.insert(c1, "2")
        elif preLet[c1] == 21:
            preVal.insert(c1, "2")
        elif preLet[c1] == -52:
            preVal.insert(c1, "0") #for commas
        elif preLet[c1] == -64:
            preVal.insert(c1, "0") #for spaces
        elif preLet[c1] == 137:
            preVal.insert(c1, "2") # é
        elif preLet[c1] == 129:
            preVal.insert(c1, "2") # á
        elif preLet[c1] == 141:
            preVal.insert(c1, "2") # í
        elif preLet[c1] == 147:
            preVal.insert(c1, "2") # ó
        elif preLet[c1] == 154:
            preVal.insert(c1, "2") # ú
        else:
            preVal.insert(c1, "1")
        c1 = c1 + 1
    
    #turn val into int
    list_int = [int(i) for i in preVal]
    list_int = (sum(list_int))

    # added value for 1 word
    final_val.append(list_int)
    
    val_calc = val_calc + 1
    preVal.clear()
#final_val has the list of values for pre translated words
    
#################################################### calculates the value of the post translated words ####################################################

while len(transText) != val_calc2:
    for x in transText[0 + val_calc2]:
        preLet2.append(ord(x) - 96)
    
    while len(preLet2) != c2:
        
        if preLet2[c2] == 1:
            preVal2.insert(c2, "2")
        elif preLet2[c2] == 5:
            preVal2.insert(c2, "2")
        elif preLet2[c2] == 9:
            preVal2.insert(c2, "2")
        elif preLet2[c2] == 15:
            preVal2.insert(c2, "2")
        elif preLet2[c2] == 21:
            preVal2.insert(c2, "2")
        elif preLet2[c2] == -52:
            preVal2.insert(c2, "0") #for commas
        elif preLet2[c2] == -64:
            preVal2.insert(c2, "0") #for spaces
        elif preLet2[c2] == 137:
            preVal2.insert(c2, "2") # é
        elif preLet2[c2] == 129:
            preVal2.insert(c2, "2") # á
        elif preLet2[c2] == 141:
            preVal2.insert(c2, "2") # í
        elif preLet2[c2] == 147:
            preVal2.insert(c2, "2") # ó
        elif preLet2[c2] == 154:
            preVal2.insert(c2, "2") # ú
        else:
            preVal2.insert(c2, "1")
        c2 = c2 + 1
    
    #turn val into int
    list_int2 = [int(i) for i in preVal2]
    list_int2 = (sum(list_int2)) - list_int2[0]

    # added value for 1 word
    final_val2.append(list_int2)
    
    val_calc2 = val_calc2 + 1
    preVal2.clear()
    
print(inputList) #pre translated list
print(transText) #post translated list
print(final_val) #FINAL VAL = PRE VAL
print(final_val2) #FINAL VAL2 = POST VAL


#################################################### calculates the value of the post translated words ####################################################


#close Files
inputWords.close


