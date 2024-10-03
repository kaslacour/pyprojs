# Opgave 17: Palindrom Tjekker
# Skriv et program, der afgør, om et indtastet ord eller en sætning er et palindrom.
# Ignorer mellemrum, tegnsætning og forskel på store og små bogstaver.

tekst = input("Indtast et ord eller en sætning: ")
# Fjern mellemrum og tegnsætning, og gør alt til små bogstaver
renset = ''.join(c for c in tekst if c.isalnum()).lower()
# Skriv din kode herunder: