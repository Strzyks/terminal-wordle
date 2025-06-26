#Warning!! The game is in the Polish launge


#imports
import random
from collections import Counter

#lists
Word = [
    "aktor","banet","bufet","bilet","baton","brzeg","bufor","cegła","chleb","cukry",
    "dolar","droga","ducha","fotel","grupa","guzik","głowa","hotel","iskra",
    "kabel","klucz","kolej","koszt","kwiat","ludek","mleko","model","motyl",
    "mucha","muzyk","mysza","norka","obiad","okres","opcja","owocą","patyk","pazur",
    "piłka","pismo","płasz","pokój","porty","proza","puder","ratus",
    "rolka","rybak","rzeka","sklep","smoki","sport","szafa",
    "szlak","szopa","szron","szyba","taler","tempo","torba","tramp","treść","ulica",
    "upiór","uroda","wążyk","wazon","wirus","worek","wstęp","wtycz","wtyka","wzrok",
    "ząbek","zegar","zgoda","zwrot","żabka","żeton","żmija","żółta","życie",
    "dźwig","jodły","kryształ","łapka","łuków",
    "męska","ogród","pasja","rzeźb","upiór"
]
wrongwords = ["1","2","3","#","@","$","_","&","-","+","(",")","/","*","'",":",";","!","?"]

#virables
trueword = random.choice(Word)
emotes = ["🟩", "🟨", "⬛"]
tryies = 0
can_write_result = True

print("🟩-dobra litera w dobrym miejscu, ")
print("🟨-dobra litera w złym miejscu, ")
print("⬛-zła litera")

print("wpisz h dla pomocy")

print("")


#main loop
while True:
    def lose():
        print(f"przegrana, prawidłowe słowo: {trueword}")

    def win():
        print("Wygrałeś!!!")

    def white_flag():
        print(f"poddałeś się, prawidłowe słowo to: {trueword}")

    yourwrite = str(input("Napisz słowo: ")).lower()
    letter_counts = Counter(yourwrite)

    if yourwrite == "h":
        print("")
        print("w - poddaje się")
        print("q - wychodzi z gry")
        print("")

    if yourwrite == "w":
        continue

    if yourwrite == "q":
        print("wychodzę z gry....")
        break

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
        win()
        continue

    #lose
    if tryies == 5 and yourwrite != trueword:
        lose()
        continue

    #check if be more letters than 2
    if any(count >= 3 for count in letter_counts.values()):
        print("Przepraszamy, nie możesz używać tej samej litery 3 razy lub więcej.")
    else:
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
