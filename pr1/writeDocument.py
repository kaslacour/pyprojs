

# open external text document
try:
    file = open("textdoc.txt","x")
except:
    file = open("textdoc.txt","w")    

#write to external file
for i in range(10):
    file.write(f"This is line {i}\n")

#save file
file.close()

