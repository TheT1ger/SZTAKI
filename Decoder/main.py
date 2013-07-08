#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 2013.06.28.

'''


# Entry class: a dekódolandó szöveg egy szavát ábrázolja
# coded: A kódszó
# pattern: A kódszóhoz tartozó minta
# length: A szó hossza
# options: A szótárból a kódszóhoz rendelt szavak, mint lehetséges feloldásuk
# frequency: Szógyakoriság
class Entry:
    coded = str("")
    pattern = list("")
    length = 0
    options = list()
    frequency = 1

    # Constructor: Paraméterként kapott kódszóhoz elkészíti az osztályt    
    def __init__(self,word):
        self.coded = word
        self.pattern = list(getPattern(word)) # Lista, nem string
        self.length = len(word)
        self.options = get("".join(self.pattern)) # A get paraméterében a lista string-é konvertálása
        
    # Kiírja a fontosabb tulajdonságait az osztálynak
    def p(self):
        print(self.coded)
        print("".join(self.pattern))
        print(self.length)
        print(self.options)
        if self.options is not None:
            print(len(self.options))
        else:
            print(0)
        print(self.frequency)
        print()
    
    # Paraméterként kapott szóról eldönti az osztály tulajdonságai alapján, hogy jelölheti-e azt a kódszó    
    def match(self,word):
        # Hossz nem egyezik
        if len(word) != self.length:
            return False
        # Elkészíti a paraméter szó mintáját
        ip = list(getPattern(word))
        for i in range(0,self.length):
            # Ha a kódszóban kérdőjel van (adott betű egyszer szerepel és még nem ismert) akkor az input mintájában is kérdőjel kell legyen
            if self.pattern[i] == '?':
                if ip[i]!='?':
                    return False
                # Ha az input adott poizicioju betüje már ismert, akkor a kódszó mintájában bent kell legyen, nem kérdőjel
                if word[i] in alphabet.values():
                    return False
            # Ha a kódszó mintájában szám van
            elif self.pattern[i].isdigit():
                # Az input mintájában is adott számnak kell lennie
                if self.pattern[i] != ip[i]:
                    return False
                # Ha az input adott poizicioju betüje már ismert, akkor a kódszó mintájában bent kell legyen, nem kérdőjel
                if word[i] in alphabet.values():
                    return False
            # Ha a kódszóban már beírt betű van
            else:
                # Ha az adott betű nem egyezik az input adott betűjével
                if self.pattern[i] != word[i]:
                    return False
                if ip[i]=='?':
                    # Ha az input mintájában kérdőjel van (adott betű egyszer szerepel), de a kódszó mintájában többször
                    for j in range(0,self.length):
                        if j!=i and self.pattern[j] == self.pattern[i]:
                            return False
                else:
                    # Ha a kódszó két betűje egyezik, de az input mintájának két betűje nem, vagy fordítva
                    for j in range(0,self.length):
                        if (self.pattern[j] == self.pattern[i] and ip[j] != ip[i]) or (self.pattern[j]!=self.pattern[i] and ip[j]==ip[i]):
                            return False
                        
        return True
       
    # Az entitáson belül a lehetséges szavak listáján végig megy, és kitörli azt, ami nem match-el
    def constraint(self):
        if self.options is not None:
            i=len(self.options)-1
            while i>=0:
                word = self.options[i]
                if not self.match(word):
                    self.options.remove(word)
                i=i-1
                
# Class vége ##################################################


# Előállítja az input szó mintáját
def getPattern(_input):
    tempPattern = list("")
    word = str(_input)
    sign = 1
    used = 0
    # Előállít egy ugyanolyan hosszú listát, csupa kérdőjellel
    for i in range(0,len(word)):
        tempPattern.append('?')
        
    # Ha az input adott karaktere megismétlődik, akkor számmal jelzi minden előfordulásnál
    for i in range(0,len(word)):
        if tempPattern[i] == '?':
            for j in range(i+1,len(word)):
                if word[i] == word[j]:
                    if used==0:
                        # String indexelés
                        tempPattern[i]=str(sign).__getitem__(0)
                    used=1
                    tempPattern[j]=str(sign).__getitem__(0)
            if used == 1:
                if sign<9:
                    sign = sign + 1
                used=0
    # Listából string
    return "".join(tempPattern)

# Az input db hashmap-hez, a pattern kulccsal jelölt listához hozzáadja a word-öt
def add(db,pattern,word):
    if pattern in db:
        if word not in db[pattern]:
            db[pattern].append(word)
    # Ha még nincs ilyen kulcsú elem
    else:
        db.update({pattern:list()})
        db[pattern].append(word)
    
# Adott db hashmap-be, adott file-fájlból felépíti a szótár-t. Először szóhosszal indexeli a map-et
def build(db,file):
    for line in file:
        words = line.split(',')
        if len(words[0]) in db:
            # Ha már van
            add(db[len(words[0])],words[1].strip('\n'),words[0])
            # Ha még nincs ilyen kulcsú elem
        else:
            db.update({len(words[0]):{}})
            add(db[len(words[0])],words[1].strip('\n'),words[0])
    
# Lekéri az adott mintára illeszkedő szavak számát a szótárból
def get(pattern):
    if len(pattern) in db:
        if pattern in db[len(pattern)]:
            return db[len(pattern)][pattern].copy()
        else:
            return None
    else:
        return None
 
# Feltölt egy hashmap-et a szótárnak (itt helyettesítődik be a megfejtett karakter)       
def fill_alphabet():
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


abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Feltölt egy hashmap-et a szótárnak (betű gyakorisággal, és lehetséges betűkkel)
def fill_alphabetic_info():
    a_info.update({"a":{"frequency":0,"options":abc.copy()}})
    a_info.update({"b":{"frequency":0,"options":abc.copy()}})
    a_info.update({"c":{"frequency":0,"options":abc.copy()}})
    a_info.update({"d":{"frequency":0,"options":abc.copy()}})
    a_info.update({"e":{"frequency":0,"options":abc.copy()}})
    a_info.update({"f":{"frequency":0,"options":abc.copy()}})
    a_info.update({"g":{"frequency":0,"options":abc.copy()}})
    a_info.update({"h":{"frequency":0,"options":abc.copy()}})
    a_info.update({"i":{"frequency":0,"options":abc.copy()}})
    a_info.update({"j":{"frequency":0,"options":abc.copy()}})
    a_info.update({"k":{"frequency":0,"options":abc.copy()}})
    a_info.update({"l":{"frequency":0,"options":abc.copy()}})
    a_info.update({"m":{"frequency":0,"options":abc.copy()}})
    a_info.update({"n":{"frequency":0,"options":abc.copy()}})
    a_info.update({"o":{"frequency":0,"options":abc.copy()}})
    a_info.update({"p":{"frequency":0,"options":abc.copy()}})
    a_info.update({"q":{"frequency":0,"options":abc.copy()}})
    a_info.update({"r":{"frequency":0,"options":abc.copy()}})
    a_info.update({"s":{"frequency":0,"options":abc.copy()}})
    a_info.update({"t":{"frequency":0,"options":abc.copy()}})
    a_info.update({"u":{"frequency":0,"options":abc.copy()}})
    a_info.update({"v":{"frequency":0,"options":abc.copy()}})
    a_info.update({"w":{"frequency":0,"options":abc.copy()}})
    a_info.update({"x":{"frequency":0,"options":abc.copy()}})
    a_info.update({"y":{"frequency":0,"options":abc.copy()}})
    a_info.update({"z":{"frequency":0,"options":abc.copy()}})
    
# Kiírja az ABC-t, és hogy melyik betű mit kódol (KÓDOLT: JELÖLT)
def print_alphabetic():
    for letter in sorted(alphabet):
        print(letter + ": " + alphabet[letter])
# Előfordulási sorrendben kiírja az ABC-t (KÖZBEN TÖRLI AZ ELEMEIT, kiüriti a map-et!!!)
def print_frequency():
    while len(a_info)>0:
        key = list(a_info.keys())[0]
        max = a_info[key]["frequency"]
        for l in a_info:
            if a_info[l]["frequency"] > max:
                max = a_info[l]["frequency"]
                key = l 
        print(key + ": " + str(max))
        a_info.pop(key)

# Kiírja a kód ABC-t, és hogy milyen betűk lehetségesek hozzá
def print_options():
    for letter in sorted(a_info):
        print(letter + ": ")
        print(a_info[letter]["options"])

# A beolvasott szöveg minden szavánál frissíti a lehetséges szavak listáját (szűkíti)
def change():
    for e in text:
        e.constraint()

# Egy input szólistára(a listán bellül azonos hosszú szavak állnak) megnézi, hogy az egybetűs szavak betűje, 
# ha szerepel benne, akkor törli azokat az entitás options listájából, amiben nem szerepel 'i', 'a'
# ha nem szerepel benne, akkor törli azokat az entitás options listájából, amiben szerepel 'i','a'        
def one_letter_filter(source):
    if len(oneletter) == 1:
        for e in source:
            for ind in range(0,len(source[0].coded)):
                if e.coded[ind] == oneletter[0]:
                    i = len(e.options)-1
                    while i>=0:
                        if e.options[i][ind] != 'i' and e.options[i][ind] != 'a':
                            e.options.remove(e.options[i]) 
                        i = i-1
    elif len(oneletter) == 2:
        for e in source:
            for ind in range(0,len(source[0].coded)):
                if e.coded[ind] == oneletter[0] or e.coded[ind] == oneletter[1]:
                    i = len(e.options)-1
                    while i>=0:
                        if e.options[i][ind] != 'i' and e.options[i][ind] != 'a':
                            e.options.remove(e.options[i]) 
                        i = i-1
                else: 
                    i = len(e.options)-1
                    while i>=0:
                        if e.options[i][ind] == 'i' or e.options[i][ind] == 'a':
                            e.options.remove(e.options[i]) 
                        i = i-1
    else:
        raise Exception("WARNING: Több egy betűs szó")

# Egy listába teszi a három leggyakoribb betűt    
def getFrequentLetters():
    temp = list()
    nums = list()
    for key,value in a_info.items():
        nums.append(value["frequency"])
    while len(temp) < 3:
        maxm = nums[0]
        for n in nums:
            if n > maxm:
                maxm = n 
        temp.append(maxm)
        nums.remove(maxm)
    for key,value in a_info.items():
        if value["frequency"] in temp and key not in most_frequent_letters:
            most_frequent_letters.append(key)

# Az ABC frissítése, coded betű jelöli a real-t
# Az összes beolvasott szó mintájában behelyettesít
# Kiszedi az adott betűt az ABC maradék betűjének options listájából
# Ha egy betű options listája 1 hosszú lett, akkor azt beírja az ABC-be (rekurzió!)
# Szűkíti a szavak options listáját            
def updateAlphabet(coded,real):
    alphabet[coded]=real
    for e in text:
        for i in range(0,len(e.coded)):
            if e.coded[i] == coded:
                e.pattern[i] = real
    a_info[real]["options"].clear()
    a_info[real]["options"].append(real)    
    for letter in a_info:
        if letter != real:
            if real in a_info[letter]["options"]:
                a_info[letter]["options"].remove(real)
                if len(a_info[letter]["options"]) == 1:
                    updateAlphabet(letter, a_info[letter]["options"][0])
    change()
            
# Szótár 
dbfile = open('..\\..\\dic.txt','r')
# Dekódolandó szöveg
inputfile = open('..\\..\\example.txt','r')

# Szótár 
db = {}
# ABC
alphabet = {}
# ABC infói
a_info = {}
# Szótár(fa) felépitése
build(db,dbfile)
# ABC feltöltése
fill_alphabet()
fill_alphabetic_info()

# Beolvasott szöveg
text = list()
# egy hosszú szavak listája(entity/osztály!)
one = list()
# egy hosszú szavak betűinek listája(betű!)
oneletter = list()
# Három leggyakoribb betű(döntetlen helyezett esetén lehet több is)
most_frequent_letters = list()
# kettő hosszú szavak listája(entity/osztály!)
two = list()
# három hosszú szavak listája(entity/osztály!)
three = list()

# Szöveg beolvasása, speciális karakterek törlése
for line in inputfile:
    line = line.lower()
    words = line.split(" ")
    for word in words:
        word = word.strip('"!?-[]{}();:\'.\n0123456789')
        if len(word) > 0:
            find = False
            # Végig nézi az eddig beolvasott szavakat
            for e in text:
                # Ha egyszer már szerepelt ez a szó, akkor az adott entitás gyakoriságát növeli
                if e.coded == word:
                    e.frequency = e.frequency + 1
                    temp = e
                    find=True
            # Ha nem szerepelt még, akkor létrehoz egy entitást
            if not find:
                temp = Entry(word)
                text.append(temp)
            # one,two,three listákhoz értelemszerűen hozzáadja
            if len(word) == 1:
                if temp not in one:
                    one.append(temp)
                if word not in oneletter:
                    oneletter.append(word)
            elif len(word) == 2:
                if temp not in two:
                    two.append(temp)
            elif len(word) ==3:
                if temp not in three:
                    three.append(temp)
            # Betűgyakoriság 
            for l in word:
                if l.isalpha():
                    a_info[l]["frequency"] = a_info[l]["frequency"] +1

getFrequentLetters()  

print(most_frequent_letters)   
# Kettő és három hosszú szavakra leellenőrzi hogy 'i', 'a' szerepel-e benne     
one_letter_filter(two)          
one_letter_filter(three)

# Megkeresi, hogy melyik kódolt betű szerepel a leggyakrabban, az lesz az 'e'
key = list(a_info.keys())[0]
maxm = a_info[key]["frequency"]
for l in a_info:
    if a_info[l]["frequency"] > maxm:
        maxm = a_info[l]["frequency"]
        key = l 
 
updateAlphabet(key, 'e')
      
# Az egy betűs szavaknál, amelyik egy betűs szó betűje benne van a leggyakoribb betűk listájába, az lesz az 'a'    
if len(oneletter) == 0:
    raise Exception("WARNING: Nincs egy betűs szó")
elif len(oneletter) == 1:
    updateAlphabet(oneletter[0], 'a')
elif len(oneletter) == 2:
    if oneletter[0] in most_frequent_letters and oneletter[1] not in most_frequent_letters:
        updateAlphabet(oneletter[0], 'a')
        
    elif oneletter[1] in most_frequent_letters and oneletter[0] not in most_frequent_letters:
        updateAlphabet(oneletter[0], 'a')
    else:
        raise Exception("WARNING: Mindkét betű gyakorisága Top3, vagy egyiké sem")
    
elif len(oneletter) > 2:
    raise Exception("WARNING: Több egy betűs szó van")


# print print print, ne sípoljál, printelj
# http://www.youtube.com/watch?v=nmyHJrBNATw

for l in one:
    l.p()
for l in two:
    l.p()
for l in three:
    l.p()

print_options()
print() 
print_frequency()
print()
print_alphabetic()
print()

while len(text) > 0:
    temp = text[0]
    max = text[0].frequency
    for e in text:
        if e.frequency > max:
            temp = e
            max = e.frequency
    print(temp.coded + " , " + "".join(temp.pattern) + ": " + str(max))
    text.remove(temp)


dbfile.close()
inputfile.close()
print('ok')