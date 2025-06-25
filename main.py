#Warning!! The game is in the Polish launge


#imports
import random

#lists
Word = [
    "aktor", "banan", "brzeg", "cegła", "cukier", "dolar", "droga", "ducha", "farba", "fotel",
    "głowa", "guzik", "hotel", "iskra", "jazda", "kabel", "karta", "klucz", "kolej", "komik",
    "koszt", "kreda", "lampa", "ludek", "łódka", "mapka", "masło", "miara", "miska", "model",
    "motyl", "mucha", "mysza", "nocny", "norka", "obiad", "okres", "opcja", "owoc",  "panda",
    "patyk", "piłka", "pismo", "plama", "pokój", "porty", "proza", "prąd",  "robot", "rolka",
    "rondo", "rybak", "rzeka", "sarna", "serce", "sklep", "słowo", "smoki", "sojusz", "sport",
    "start", "stres", "szafa", "szlak", "szopa", "szyba", "tempo", "torba", "trawa", "treść",
    "ulica", "upiór", "uroda", "wałek", "wazon", "wirus", "worek", "wstęp", "wtyka", "wzrok",
    "ząbek", "zegar", "zgoda", "ziarna", "złota", "znicz", "zwrot", "żabka", "żarów", "żmija",
    "życie", "żwire", "żyzna", "żółta", "żeton", "bufet", "klasa", "grupa", "tempo", "druk", 
    "mleko", "kwiat", "bilet", "piase", "płasz", "linie", "pliki", "korek", "czapa", "kreda",
    "kotek", "pasja", "torus", "luzak", "taler", "flaga", "kamera", "kubek", "puder", "notka",
    "sanki", "blok",  "kocyk", "winda", "plaza", "piana", "tramp", "szron", "kącik", "torba",
    "zapas", "notat", "żarno", "muzyk", "kurcz", "baton", "zwóz",  "luzik", "grill", "pupil"
]
wrongwords = ["1","2","3","#","@","$","_","&","-","+","(",")","/","*","'",":",";","!","?"]

#virables
trueword = random.choice(Word)
emotes = ["🟩", "🟨", "⬛"]
tryies = 0
can_write_result = True

#main loop
while True:
    yourwrite = str(input("Napisz słowo: "))

    #check the wrong letters in the text
    for znak in wrongwords:
        if znak in yourwrite:
            print("ZŁA LITERA, HAHAHA")
            continue
    
    #how much the text have letters
    if len(yourwrite) >5:
        print("Za dużo liter")
        continue
    if len(yourwrite) <5:
        print("za mało liter")
        continue
    
    #win
    if yourwrite == trueword:
        print("Wygrałeś!!!")
        break
    #lose
    if tryies == 5 and yourwrite != trueword:
        print(f"przegrana, prawidłowe słowo: {trueword}")
        break
    
    #emotes system
    result = []
    for i in range(5):
        if yourwrite[i] == trueword[i]:
            result.append(emotes[0])
        elif yourwrite[i] in trueword:
            result.append(emotes[1])
        else:
            result.append(emotes[2])

    #write in the screen results
    print("".join(result))

    #tries
    tryies+=1

#I dont speak english very well :)
