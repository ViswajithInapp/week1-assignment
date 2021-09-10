import random
c1=""
c2=""
c3=""
list1 = [1, 2, 3]
playerr = {}     #for storing round:user choice
computerr = {}   #for storing round:computer choice
roundd = {}      #for storing round:win/lost
print("ENTER THE CHOICE OF USER (ROCK :1,PAPER :2,SCISSORS :3")
for i in range(10):#gets values on all 3 dictionaries
    s = input("ENTER THE CHOICE IN ROUND {} :".format(i+1))
    playerr[i]=s
    computerr[i]=random.choice(list1)
    if playerr[i]==computerr[i]:
        roundd[i]="DRAW"
#    else :
#        if (playerr[i]==1 and computerr[i]==3):
#            roundd[i] = "WON"
#        elif (playerr[i]==2 and computer[i]==1):
#            roundd[i] = "WON"
#        elif (playerr[i]==3 and computerr[i]==2):
#            roundd[i] = "WON"
#        else:
#            roundd[i] = "LOST"
    else :
        if (playerr[i]==1):#when player chooses rock
            if (computerr[i]==3):
                roundd[i] = "WON"
            elif(computerr[i]==2):
                roundd[i]="LOST"
        elif (playerr[i]==2):#when player chooses paper
            if(computerr[i]==1):
                roundd[i] = "WON"
            elif (computerr[i]==3):
                roundd[i]="LOST"
        elif (playerr[i]==3):#when player chooses scissors
            if(computer[i]==1):
                roundd[i] = "LOST"
            elif (computerr[i]==2):
                roundd[i]="WON"
m=input("ENTER THE ROUND YOU NEED INFORMATION :")
m=int(m)
m=m-1
print (m)
#print(playerr[m])
#print(computerr[m])
#print(roundd[m])

if playerr[m]==1:
    c1="ROCK"
    if roundd[m]=="LOST":
        c2="PAPER"
        c3="LOST"
    elif roundd[m]=="WON":
        c2="SCISSORS"
        c3="WON"
    else:
        c2=c1
        c3="WON"
elif playerr[m]==2:
    c1="PAPER"
    if roundd[m]=="LOST":
        c2="SCISSORS"
        c3="LOST"
    elif roundd[m]=="WON":
        c2="ROCK"
        c3="WON"
    else:
        c2=c1
        c3="WON"
elif playerr[m]==3:
    c1="SCISSORS"
    if roundd[m]=="LOST":
        c2="ROCK"
        c3="LOST"
    elif roundd[m]=="WON":
        c2="PAPER"
        c3="WON"
    else:
        c2=c1
        c3="WON"
print("PLAYER CHOICE ="+ c1)   #c1 has value of player choice in mth round
print("COMPUTER CHOICE ="+ c2) #c2 has value of computer choice in mth round
print("ROUND "+ c3)            #c3 has value of player choice in mth round