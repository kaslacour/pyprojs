
import random as rand


personal_dict = {}


personal_dict[("string", "streng")] = "kombination af tegn og bogstaver anført i citationstegn"
personal_dict[("int","integer","heltal")] = "tal som 1, 2 og 3"
personal_dict[("float","floating point number","kommatal")] = "tal som 0.5, 4.2, -7.1"
personal_dict["program"] = "serie af instrukser, som kan foretages af en computer - også kaldet en opskrift"


while True:
    ord_flash, definition_flash = rand.choice(list(personal_dict.items()))
    ord_gæt = input(definition_flash + "?")

    if ord_gæt == "x":
        break

    if type(ord_flash) is not tuple:
        ord_flash = tuple([ord_flash])


    svar_accepteret = False
    for ord in ord_flash:
        if ord in ord_gæt:
            svar_accepteret = True
    
    if svar_accepteret:
        print("Korrekt")
    else:
        print("Forkert")

