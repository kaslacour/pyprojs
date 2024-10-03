import json
import os

from gtts import gTTS

text = "Bonjour ! Voici un petit texte de lire à voix haute."
tts = gTTS(text = text, lang='fr')
tts.save("output.mp3")
os.system("afplay output.mp3")



path = os.path.dirname(__file__)
nameOfJson = os.path.join(path,"flashcards.json")

def appendFlashcard(expression, definition, context):
    try:
        with open(nameOfJson, "x") as file:
            json.dump({"flashcards": []},file)
            file.close()
    except Exception:
        pass

    with open(nameOfJson, "r+") as file:
        file_data = json.load(file)
        data_entry = {"context": context, expression : definition}
        file_data["flashcards"].append(data_entry)

        # we need to specify which portion of the file we want to overwrite
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()
    pass
    pass

def main():
    pass

if __name__ == "__main__":
    main()





