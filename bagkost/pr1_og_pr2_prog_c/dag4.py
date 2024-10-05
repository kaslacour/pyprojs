def capital_indexes(s):
    l = []
    for i in range(len(s)):
        if s[i].isupper():
            l.append(i)
    return l

print(capital_indexes("HelLo"))

def mid(s):
    if len(s) % 2 == 1:
        return s[int((len(s)+1)/2-1)]
    else:
        pass

print(mid("abc"))

input("Indtast et tal:")