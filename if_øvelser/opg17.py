# Opgave 17: Palindrom Tjekker
# Skriv et program, der afgør, om et indtastet ord eller en sætning er et palindrom.
# Ignorer mellemrum, tegnsætning og forskel på store og små bogstaver.

# Skriv din kode herunder:
tekst = input("Indtast et ord eller en sætning: ")
renset = ''.join(c for c in tekst if c.isalnum()).lower() 
