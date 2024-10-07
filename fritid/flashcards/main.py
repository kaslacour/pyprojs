import json
import os
import random 


from gtts import gTTS
"""
text = "Bonjour ! Voici un petit texte de lire à voix haute."
tts = gTTS(text = text, lang='fr')
tts.save("output.mp3")
os.system("afplay output.mp3")
"""

dir = os.path.dirname(__file__)
nameOfJson = os.path.join(dir,"flashcards.json")

def appendFlashcard(word_phrase, definition, context):
    # create .json file if it doesn't already exist
    try:
        with open(nameOfJson, "x") as file:
            json.dump({"flashcards": []},file)
            file.close()
    except Exception:
        pass

    # add entry to the .json file
    with open(nameOfJson, "r+") as file:
        file_data = json.load(file)
        data_entry = {"context": context, "word_phrase": word_phrase, "definition" : definition}
        tts = gTTS(text = context, lang='fr')
        try:
            os.mkdir(os.path.join(dir,"audios"))
        except Exception:
            pass    
        data_entry["audio_path"] = os.path.join(dir, "audios/%s.mp3" % "".join(word_phrase.split()))
        tts.save(data_entry["audio_path"])
        file_data["flashcards"].append(data_entry)

        # we need to specify which portion of the file we want to overwrite
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()
    pass

def main():
    while True:
        user_command = input("Press 'n' for new flashcard, 't' for test of knowledge, or 'x' for exit.\n").strip().lower()
        match user_command:
            case 'n':
                # create new flashcard
                word_phrase = input("Enter word or phrase: ")
                definition = input("Enter definition: ")
                context = input("Enter a context: ")
                appendFlashcard(word_phrase, definition, context)
            case 't':
                # test knowledge
                # TODO
                with open(nameOfJson, "r") as file:
                    loaded_file = json.load(file)
                    list_of_cards = loaded_file["flashcards"]
                    file.close()
                random.shuffle(list_of_cards)

                while len(list_of_cards) > 0:
                    card = list_of_cards.pop()
                    word_phrase = card["word_phrase"]
                    #mode = random.choice(["context", "definition"])
                    prompt = card["context"].replace(word_phrase, "_" * len(word_phrase))
                    guess = input(prompt+"\n")
                    if guess.strip() == word_phrase.strip():
                        print("Correct!")
                    else:
                        guess = input("hint: %s \n" % card["definition"])
                        if guess.strip() == word_phrase.strip():
                            print("Correct!")
                    print(card["context"])
                    os.system("afplay %s" % card["audio_path"])
                pass
            case 'x':
                break
            case _:
                print("Invalid key.")
    pass

if __name__ == "__main__":
    main()





