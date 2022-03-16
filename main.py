#Importing Librarires
from googletrans import Translator
translator = Translator()

# Variables
inputWords = open("testWords.txt", "r")


print(translator.translate('perro', dest='en').text)


#Close files
inputWords.close


#Aadesh testing to see if you can see this

# I do not have time rn to test it but if you get an error "ATRIBUTE ERROR : NoneType object has no attribute 'group'" then check out this https://pytutorial.com/python-solve-err-googletrans