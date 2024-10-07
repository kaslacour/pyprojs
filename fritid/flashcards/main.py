import json
import os
import random 
from gtts import gTTS

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
        # creating audio file
        tts = gTTS(text = context, lang='fr')
        try:
            os.mkdir(os.path.join(dir,"audios"))
        except Exception:
            pass    
        audio_path = os.path.join(dir, "audios/%s.mp3" % "".join(word_phrase.split()))
        tts.save(audio_path)
        # making a new entry to the flashcards dictionary
        file_data = json.load(file)
        file_data["flashcards"][word_phrase] = {
            "context": context,
            "definition" : definition,
            "audio_path": audio_path
        }
        # replace the existing dictionary with the updated one
        # we need to specify which portion of the file we want to overwrite
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()
    pass

def main():
    while True:
        user_command = input("Press 'n' for new flashcard, \
                             't' for test of knowledge, \
                             'e' for editing an existing flashcard, \
                             'r' for removing an existing flashcard, \
                             or 'x' for exit.\n").strip().lower()
        match user_command:
            case 'n':
                # create new flashcard
                word_phrase = input("Enter word or phrase: ")
                definition = input("Enter definition: ")
                context = input("Enter a context: ")
                appendFlashcard(word_phrase, definition, context)
            case 'e':
                word_phrase = input("Which flashcard should be edited?")
                with open(nameOfJson, "r") as file:
                    file_data = json.load(file)
                    file.close()

                if word_phrase in file_data["flashcards"]:
                    user_command = input("Press 'd' for definition, 'wp' for word/phrase, or 'c' for context")
                    match user_command:
                        case 'd':
                            mode = "definition"
                            pass
                        case 'c':
                            mode = "context"
                            pass
                        case 'wp':
                            mode = "word_phrase"
                            pass
                        case _:
                            print("Invalid key.")
                            continue
                    if mode == "word_phrase":
                        print(file_data["flashcards"][word_phrase])
                        new_word_phrase = input("Enter new %s\n" % mode)
                        file_data["flashcards"][new_word_phrase] = file_data["flashcards"][word_phrase]
                        del file_data["flashcards"][word_phrase]
                    else:
                        print(file_data["flashcards"][word_phrase][mode])
                        file_data["flashcards"][word_phrase]["mode"] = input("Enter new %s\n" % mode)

                    with open(nameOfJson, "r+") as file:
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                        file.close()
                else:
                    print("Unable to find an entry with the key '%s'" % word_phrase)

                #list_of_entries = 
            case 't':
                # test knowledge
                # TODO
                with open(nameOfJson, "r") as file:
                    loaded_file = json.load(file)
                    dict_of_cards = loaded_file["flashcards"]
                    file.close()
                list_of_cards = list(dict_of_cards)
                random.shuffle(list_of_cards)

                while len(list_of_cards) > 0:
                    word_phrase = list_of_cards.pop()
                    card = dict_of_cards[word_phrase]
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





