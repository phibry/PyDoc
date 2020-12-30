# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:03:39 2018

@author: phili
"""

#testlist = ["Eins", "Zwei", "Drei", "Vier"]
#number = 0
#
#for number in range(4):
#    numberlist = []
#    numberlist.append(number)
##    for testlist in range(4):
#    
#    print(str(numberlist) #+ ": " + str(testlist))
#    

listone = ["Eins", "Zwei", "Drei"]
listtwo = []
newlist = []
for j in range(len(listone)):
    listtwo.append(str(j+1))

for i in range(len(listone)):
    newlist.append(listtwo[i] + ": " + listone[i])
       
newlist = ["Liste"] + newlist   
print(newlist) 
print(*newlist, sep = "\n")