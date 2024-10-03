import time

list_of_things = [2, -4, "'Hello, world!'", "'42.0'", 42.0, -19.0, [1,2,3]]


#primære datatyper: heltal (int), kommatal (float), sanhedsværdi (boolean), strenge (str)

#sammensatte datatyper: lister (list), arrays, ordbøger (dict), strenge (str)

for thing in list_of_things:
    print("What data type is", thing,"?")
    input()
    print(thing,"is of type", type(thing),"\n")
    input()

