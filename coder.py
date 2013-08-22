'''
Created on 2013.06.21.

@author: Roberto
'''

import random
import sys

tool = list()
tool.append("a")
tool.append("b")
tool.append("c")
tool.append("d")
tool.append("e")
tool.append("f")
tool.append("g")
tool.append("h")
tool.append("i")
tool.append("j")
tool.append("k")
tool.append("l")
tool.append("m")
tool.append("n")
tool.append("o")
tool.append("p")
tool.append("q")
tool.append("r")
tool.append("s")
tool.append("t")
tool.append("u")
tool.append("v")
tool.append("w")
tool.append("x")
tool.append("y")
tool.append("z")
tool.append("A")
tool.append("B")
tool.append("C")
tool.append("D")
tool.append("E")
tool.append("F")
tool.append("G")
tool.append("H")
tool.append("I")
tool.append("J")
tool.append("K")
tool.append("L")
tool.append("M")
tool.append("N")
tool.append("O")
tool.append("P")
tool.append("Q")
tool.append("R")
tool.append("S")
tool.append("T")
tool.append("U")
tool.append("V")
tool.append("W")
tool.append("X")
tool.append("Y")
tool.append("Z")

alphabet = {}
alphabet.update({"a":"?"})
alphabet.update({"b":"?"})
alphabet.update({"c":"?"})
alphabet.update({"d":"?"})
alphabet.update({"e":"?"})
alphabet.update({"f":"?"})
alphabet.update({"g":"?"})
alphabet.update({"h":"?"})
alphabet.update({"i":"?"})
alphabet.update({"j":"?"})
alphabet.update({"k":"?"})
alphabet.update({"l":"?"})
alphabet.update({"m":"?"})
alphabet.update({"n":"?"})
alphabet.update({"o":"?"})
alphabet.update({"p":"?"})
alphabet.update({"q":"?"})
alphabet.update({"r":"?"})
alphabet.update({"s":"?"})
alphabet.update({"t":"?"})
alphabet.update({"u":"?"})
alphabet.update({"v":"?"})
alphabet.update({"w":"?"})
alphabet.update({"x":"?"})
alphabet.update({"y":"?"})
alphabet.update({"z":"?"})
alphabet.update({"A":"?"})
alphabet.update({"B":"?"})
alphabet.update({"C":"?"})
alphabet.update({"D":"?"})
alphabet.update({"E":"?"})
alphabet.update({"F":"?"})
alphabet.update({"G":"?"})
alphabet.update({"H":"?"})
alphabet.update({"I":"?"})
alphabet.update({"J":"?"})
alphabet.update({"K":"?"})
alphabet.update({"L":"?"})
alphabet.update({"M":"?"})
alphabet.update({"N":"?"})
alphabet.update({"O":"?"})
alphabet.update({"P":"?"})
alphabet.update({"Q":"?"})
alphabet.update({"R":"?"})
alphabet.update({"S":"?"})
alphabet.update({"T":"?"})
alphabet.update({"U":"?"})
alphabet.update({"V":"?"})
alphabet.update({"W":"?"})
alphabet.update({"X":"?"})
alphabet.update({"Y":"?"})
alphabet.update({"Z":"?"})

num = input()

for l in alphabet:
    i=random.randint(0, len(tool)-1)
    alphabet[l] = tool[i]
    tool.remove(tool[i])
    
for l in sorted(alphabet):
    print(l + ": " + alphabet[l])
    
inputfile = open("D:\\GitHub\\SZTAKI\\inputfile.txt",'r')
outputstr = ""
for line in inputfile:
    for l in line:
        if l in alphabet.values():
            for a in alphabet:
                if alphabet[a] == l:
                    outputstr = outputstr + a
        else:
            outputstr = outputstr + l 

outputfile = open("D:\\GitHub\\SZTAKI\\example" +num+".txt",'w')
outputfile.write(outputstr)

alp = open("D:\\GitHub\\SZTAKI\\example" +num+"abc.txt",'w')
for l in sorted(alphabet):
    alp.write(l + ": " + alphabet[l] + "\n")

alp.close()
outputfile.close()
inputfile.close()




