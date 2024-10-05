# Opgave 15: Sten-Saks-Papir
# Skriv et program, der lader brugeren spille sten-saks-papir mod computeren.
# Brugeren skal indtaste sit valg, og computeren skal vælge tilfældigt.
# Programmet skal bestemme vinderen baseret på følgende regler:
# - Sten slår saks
# - Saks slår papir
# - Papir slår sten
# Udskriv resultatet af spillet.

import random

valg = input("Vælg sten, saks eller papir: ").lower()
muligheder = ['sten', 'saks', 'papir']
computer_valg = random.choice(muligheder)

print("Computeren valgte:", computer_valg)

# Udfyld resten af koden herunder:
if valg == computer_valg:
    print("Uafgjort!")