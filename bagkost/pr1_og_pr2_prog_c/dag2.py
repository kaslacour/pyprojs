from test import variabel

print(variabel)

min_ordbog = {
    "program": "serie af instrukser, som kan foretages af en computer - også kaldet en opskrift",
    "python": "et programmeringsprog",
    "print()": "udskriver en besked i terminalen",
    "string": "en kombination af tegn og bogstaver i citationstegn"
}


while True:
    ord = input()
    if ord in min_ordbog:
        output = min_ordbog[ord]
        print(output)
    else:
        print("ord findes ikke (endnu) i min_ordbog")


