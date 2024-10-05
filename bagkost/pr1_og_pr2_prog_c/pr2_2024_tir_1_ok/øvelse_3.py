personer = {}

while True:
    navn = input("Indtast navn (eller 'stop' for at afslutte): ")
    if navn == "stop":
        #
    alder = input("Indtast alder: ")
    
    try:
        # Konverter alder til et heltal
        # Tilføj navn og alder til ordbogen (navn:alder)
    except ValueError:
        # print fejlbesked

# Udskriv listen over personer
for navn, alder in personer.items():
    print(navn, "er", alder, "år gammel")
