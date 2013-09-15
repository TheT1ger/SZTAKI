#!/usr/local/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2013.06.21.

@author: Roberto
'''


import random
import sys
import codecs

tool = list()
tool.append("a")
tool.append("á")
tool.append("b")
tool.append("c")
tool.append("d")
tool.append("e")
tool.append("é")
tool.append("f")
tool.append("g")
tool.append("h")
tool.append("i")
tool.append("í")
tool.append("j")
tool.append("k")
tool.append("l")
tool.append("m")
tool.append("n")
tool.append("o")
tool.append("ó")
tool.append("ö")
tool.append("ő")
tool.append("p")
tool.append("q")
tool.append("r")
tool.append("s")
tool.append("t")
tool.append("u")
tool.append("ú")
tool.append("ü")
tool.append("ű")
tool.append("v")
tool.append("w")
tool.append("x")
tool.append("y")
tool.append("z")
tool.append("A")
tool.append("Á")
tool.append("B")
tool.append("C")
tool.append("D")
tool.append("E")
tool.append("É")
tool.append("F")
tool.append("G")
tool.append("H")
tool.append("I")
tool.append("Í")
tool.append("J")
tool.append("K")
tool.append("L")
tool.append("M")
tool.append("N")
tool.append("O")
tool.append("Ó")
tool.append("Ö")
tool.append("Ő")
tool.append("P")
tool.append("Q")
tool.append("R")
tool.append("S")
tool.append("T")
tool.append("U")
tool.append("Ú")
tool.append("Ü")
tool.append("Ű")
tool.append("V")
tool.append("W")
tool.append("X")
tool.append("Y")
tool.append("Z")

alphabet = {}
alphabet.update({"a":"?"})
alphabet.update({"a":"?"})
alphabet.update({"á":"?"})
alphabet.update({"b":"?"})
alphabet.update({"c":"?"})
alphabet.update({"d":"?"})
alphabet.update({"e":"?"})
alphabet.update({"é":"?"})
alphabet.update({"f":"?"})
alphabet.update({"g":"?"})
alphabet.update({"h":"?"})
alphabet.update({"i":"?"})
alphabet.update({"í":"?"})
alphabet.update({"j":"?"})
alphabet.update({"k":"?"})
alphabet.update({"l":"?"})
alphabet.update({"m":"?"})
alphabet.update({"n":"?"})
alphabet.update({"o":"?"})
alphabet.update({"ó":"?"})
alphabet.update({"ö":"?"})
alphabet.update({"ő":"?"})
alphabet.update({"p":"?"})
alphabet.update({"q":"?"})
alphabet.update({"r":"?"})
alphabet.update({"s":"?"})
alphabet.update({"t":"?"})
alphabet.update({"u":"?"})
alphabet.update({"ú":"?"})
alphabet.update({"ü":"?"})
alphabet.update({"ű":"?"})
alphabet.update({"v":"?"})
alphabet.update({"w":"?"})
alphabet.update({"x":"?"})
alphabet.update({"y":"?"})
alphabet.update({"z":"?"})
alphabet.update({"A":"?"})
alphabet.update({"Á":"?"})
alphabet.update({"B":"?"})
alphabet.update({"C":"?"})
alphabet.update({"D":"?"})
alphabet.update({"E":"?"})
alphabet.update({"É":"?"})
alphabet.update({"F":"?"})
alphabet.update({"G":"?"})
alphabet.update({"H":"?"})
alphabet.update({"I":"?"})
alphabet.update({"Í":"?"})
alphabet.update({"J":"?"})
alphabet.update({"K":"?"})
alphabet.update({"L":"?"})
alphabet.update({"M":"?"})
alphabet.update({"N":"?"})
alphabet.update({"O":"?"})
alphabet.update({"Ó":"?"})
alphabet.update({"Ö":"?"})
alphabet.update({"Ő":"?"})
alphabet.update({"P":"?"})
alphabet.update({"Q":"?"})
alphabet.update({"R":"?"})
alphabet.update({"S":"?"})
alphabet.update({"T":"?"})
alphabet.update({"U":"?"})
alphabet.update({"Ú":"?"})
alphabet.update({"Ü":"?"})
alphabet.update({"Ű":"?"})
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
    
inputfile = codecs.open("D:\\GitHub\\SZTAKI\\inputfile.txt",'r',"UTF-8")
outputstr = ""
for line in inputfile:
    for l in line:
        if l in alphabet.values():
            for a in alphabet:
                if alphabet[a] == l:
                    outputstr = outputstr + a
        else:
            outputstr = outputstr + l 

outputfile = codecs.open("D:\\GitHub\\SZTAKI\\example" +num+".txt",'w',"UTF-8")
outputfile.write(outputstr)

alp = codecs.open("D:\\GitHub\\SZTAKI\\example" +num+"abc.txt",'w',"UTF-8")
for l in sorted(alphabet):
    alp.write(l + ": " + alphabet[l])
    alp.write("\r\n")

alp.close()
outputfile.close()
inputfile.close()




