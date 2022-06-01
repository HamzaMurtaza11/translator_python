from pydoc import text
from typing import Text
from translate import Translator
translator= Translator(to_lang="ur")

try:
    with open("./translate_file.txt",mode="r") as myfile:
       
        text = myfile.read()
        translation = translator.translate(text)

       
        print(translation)

        
        
        
except FileNotFoundError:
    print("file not found")

