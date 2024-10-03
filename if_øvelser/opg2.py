# Opgave 2: Bestem aldersgruppe
# Skriv et program, der beder brugeren om at indtaste sin alder.
# Programmet skal bestemme, hvilken aldersgruppe brugeren tilhører:
# - Barn (0-12 år)
# - Teenager (13-19 år)
# - Voksen (20-64 år)
# - Senior (65+ år)

alder = int(input("Indtast din alder: "))
# Færdiggør koden nedenfor
if 0 <= alder <= 12:
    print("Du er et barn.")
elif 13 <= alder <= 19:
    print("Du er en teenager.")