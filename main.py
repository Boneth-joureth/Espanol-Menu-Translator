#Importing Librarires
from googletrans import Translator
translator = Translator()

# Variables
inputWords = open("testWords.txt", "r")

print(translator.translate('perro', dest='en').text)


#Close files
inputWords.close
