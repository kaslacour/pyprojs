min_ordbog = {
    "program": "et program er (...)",
    "python": "et programmeringsprog",
    "streng": "en streng af bogstaver og tegn",
    "datatyper": "strenge (str), heltal (int)" +
        "kommatal (float), sandhedsværdier (bool)",
    "variabel": "noget data gemt under et navn",
    "numpy": "et bibliotek-modul med mange funktioner fra mat",
    "tkinter": "et bibliotek-modul med mulighed for at lave grafiske brugergrænseflader",
    "print(\"besked\")":"print besked ud i chatten ud i konsolen",
    "5 // 4" : "heltalsdivison",
    "\"abc\".upper()": "laver abc om til ABC",
}



while True:
    ord = input()
    if ord in min_ordbog:
        output = min_ordbog[ord]
        print(output)
    else:
        print("ord findes ikke (endnu) i min_ordbog")


