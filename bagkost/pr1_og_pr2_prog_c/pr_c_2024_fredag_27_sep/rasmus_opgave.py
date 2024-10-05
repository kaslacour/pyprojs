'''
En klasse er i gang med at sælge skrabekalendere ved juletid og vil gerne kunne holde styr på deres fortjeneste efter hver gang en elev har været ud at sælge kalendere. De vil også gerne holde styr på deres egen fortjeneste undervejs.
Lav et program, som kan holde styr på hver af de individuelle elevers score og den samlede score af klassen.
Du får først størrelsen af klassen, n, og derefter m efterspørgsler.
Hver efterspørgsel vil være følgende:
"sum" - print det samlede beløb
"fortjeneste 'elev'" - print fortjenesten for en elev, som er nummer 'elev' i klassen (Den først elev har indekset '1')
"tjent 'elev' 'beløb'" - Tilføj mængden 'beløb' til fortjenesten tilhørende elev nummer 'elev'

0 < n,m < 10^6 
'''
#import time
import random as rand
import matplotlib.pyplot as plt
import numpy as np
#import sys

# define globals
n = rand.randint(1,10**6)
m = rand.randint(1,10**6)
moneys = [0] * n
total = 0

def run_request(request: str, print = True):
    global commands
    global moneys
    global total

    print_text = ""
    print_text += "running request >> "
    if request == commands[0]:
        print_text += "summen er " + str(total)
    else:
        parms = request.split()
        try:
            elev_idx = int(parms[1][1:-1])
        except Exception:
            pass
        if parms[0] == "fortjeneste":
            print_text += "fortjenesten af elev " + str(elev_idx)+ " : " + str(moneys[elev_idx])
        elif parms[0] == "tjent":
            try:
                amount = float(parms[2][1:-1])
                moneys[elev_idx] += amount
                total += amount
                print_text += "et beløb på "+ str(amount) + " tjent af elev " + str(elev_idx)
            except Exception:
                pass
    if print:
        print(print_text)
    pass

# generate m 'randomly selected' requests
print("Generating requests")
commands = ["sum", "fortjeneste 'elev'", "tjent 'elev' 'beløb'"]
requests = []
for i in range(m):
    command_idx = rand.randint(0,len(commands)-1)
    if command_idx == 1:
        elev_idx = rand.randint(0,n-1)
        string_command = commands[command_idx].replace("'elev'","\'"+str(elev_idx)+"\'")
    elif command_idx == 2:
        elev_idx = rand.randint(0,n-1)
        amount = int(rand.gammavariate(200,0.5))
        string_command = commands[command_idx].replace("'elev'","\'"+str(elev_idx)+"\'")
        string_command = string_command.replace("'beløb'","\'"+str(amount)+"\'")
    else:
        string_command = commands[command_idx]
    requests.append(string_command)
    print(f"{i} out of {m} requests generated")
print(f"{m} requests generated")

# run the requests
print("...running the requests...")
for i,request in enumerate(requests):
    run_request(request,False)
print("...finished running the requests...")

# plot results (optional)
x = [i for i in range(n)]
plt.xlabel(r'elev', fontsize = 14)
plt.ylabel(r'fortjeneste', fontsize = 14)
plt.title(f'#elever = {n}, #forespørgsler = {m}')
plt.scatter(x,moneys,s=1)
plt.show()