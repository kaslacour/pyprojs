

# open external text document
try:
    #"x": opret dokument
    file = open("textdoc.txt","x")
except:
    #"w": skriv til eksisterende dokument
    file = open("textdoc.txt","a")    
    

file.write("this is a new line in my document\n")

#for i in [0,1,2,3,4,5,6,7,8,9]:
#for i in range(10):
#    file.write(f"This is line {i}\n")

#save file
file.close()

