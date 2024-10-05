# Bed brugeren om at indtaste tre tal
tal1 = input("Indtast det første tal: ")
tal2 = input("Indtast det andet tal: ")
tal3 = input("Indtast det tredje tal: ")

# Konverter input til tal
tal1 = float(tal1)
tal2 = float(tal2)
tal3 = float(tal3)

# Beregn summen af de tre tal
sum = tal1+tal2+tal3

# Beregn gennemsnittet af de tre tal
gennemsnit = sum/3

# Beregn produktet af de tre tal
produkt = tal1*tal2*tal3

# Vis resultaterne
print("Summen af de tre tal er:", sum)
print("Gennemsnittet af de tre tal er:", gennemsnit)
print("Produktet af de tre tal er:", produkt)
