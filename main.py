from googletrans import Translator

translator = Translator()

print(translator.translate('perro', dest='en').text)
