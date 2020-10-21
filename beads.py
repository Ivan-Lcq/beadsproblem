
f = open('beads.in', 'r')
g = open('beads.out', 'w')
from collections import deque
readfile = f.readlines()
numofbeads = int(readfile[0])
beads = readfile[1]
beadsarr = []
beadsarrn = []
finaltotalnumber = 0
totalnumber = 2
num = 1
numx = 1
isnotwhite = True
allequal = True

for x in range (0, numofbeads):
    beadsarr.append(beads[x])
firstitem = beadsarr[0]
for item in beadsarr:
    if firstitem != item:
        allequal = False
        break;


if allequal:
    if firstitem == 'w':
        isnotwhite = False
beadsarrn = beadsarr 
if isnotwhite == True:
    for x in range (0, numofbeads):
        beadsarrn = list(beadsarr)
     
        totalnumber  = 2
        for z in range(0, numofbeads):
            if beadsarr[z] == "r" or beadsarr[z] == "b":
                rightcolorx = beadsarr[z]
                break
        for z in range(0, numofbeads):
            if beadsarr[-z-1] == "r" or beadsarr[-z-1] == "b":
                rightcolory = beadsarr[-z-1]
                break
      
        for y in range (1, numofbeads):
            
            if beadsarr[y-1] == beadsarr[y] or beadsarr[y-1] == "w" or beadsarr[y] == "w":
                if beadsarr[y-1] == rightcolorx or beadsarr[y] == rightcolorx:
                    totalnumber = totalnumber + 1
                    beadsarrn.remove(beadsarr[y-1])
                 
                elif beadsarr[y] == "w" and beadsarr[y-1] == "w":
                    totalnumber = totalnumber + 1 
                    beadsarrn.remove(beadsarr[y-1])
                   
                else:
                    break
            else:
                break
        del beadsarrn[0]
        for y in range (1, len(beadsarrn)):
            if beadsarrn[0 - y] == beadsarrn[-1 - y] or beadsarrn[0-y] == "w" or beadsarrn[-1-y] == "w":
                if beadsarrn[0-y] == rightcolory or beadsarrn[-1-y] == rightcolory:
                    totalnumber = totalnumber + 1                
                elif beadsarrn[0-y] == "w" and beadsarrn[-1-y] == "w":
                    totalnumber = totalnumber + 1
                    
                else:
                    break
            else:
                break
      
        if totalnumber > finaltotalnumber:
            finaltotalnumber = totalnumber
        beadsarr = [beadsarr[-1]] + beadsarr[:-1]

for item in beadsarr:
    if firstitem != item:
        allequal = False
        break;
if allequal == True:
    finaltotalnumber = numofbeads
g.write(str(finaltotalnumber))
g.write("\n")
f.close()
g.close()
