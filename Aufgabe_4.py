# 1) Eingabe Suchbeggriff (deutsch)
# 2) Bestimmung der gesamtanzahl der Elemente ( = maximaler Index )
# 3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 4) Wenn Element gefunden -> Index speichern
# 5) Zugriff auf Listenelement[Index] in Liste (englisches Wörterbuch)

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

def eingabe_befehl():
    Bedingung = False
    while Bedingung == False:
        Auswahl = input("Was möchten Sie tun? \n Einfügen [E] \n Löschen [L] \n Abfragen [A]:" )
        Auswahl = Auswahl.upper()
        
        if Auswahl == "E":
            Bedingung = True
            return Auswahl
        
        elif Auswahl == "L":
            Bedingung = True
            return Auswahl
        
        elif Auswahl == "A":
            Bedingung = True
            return Auswahl
        
        else:
            print("Eingabe nicht korrekt. Versuchen Sie es erneut!")
            
Auswahl = eingabe_befehl()


if Auswahl == "E":
    Wort = input("Bitte geben Sie ihr deutsches Wort ein: ")
    woerterbuch_deutsch.append(Wort) #Wort in Liste hinzufügen
    Word = input("Bitte geben Sie ihr englisches Wort ein: ")
    woerterbuch_english.append(Word)
    
    print(woerterbuch_deutsch)
    print(woerterbuch_english)
    
elif Auswahl == "L" or Auswahl == "l":
    Wort = input("Welches Wort Möchten sie löschen? ")
    
    Index_Wort = 0
    k = 0
    Iterationen = len(woerterbuch_deutsch)
    
    while k < Iterationen:
    
        if woerterbuch_deutsch[k].lower() == Wort.lower():
            Index_Wort = k
            woerterbuch_deutsch.remove(woerterbuch_deutsch[Index_Wort])
            woerterbuch_english.remove(woerterbuch_english[Index_Wort])
            break
    
        elif woerterbuch_english[k].lower() == Wort.lower():
            Index_Wort = k
            woerterbuch_english.remove(woerterbuch_english[Index_Wort])
            woerterbuch_deutsch.remove(woerterbuch_deutsch[Index_Wort])
            break
        k += 1
        
    print(woerterbuch_deutsch)
    print(woerterbuch_english)
        
else: 

    Wort = input("Bitte geben Sie Ihr Wort ein das Sie übersetzen wollen:")

    Index_Wort = 0
    k = 0
    Iterationen = len(woerterbuch_deutsch)

    while k < Iterationen:
    
        if woerterbuch_deutsch[k].lower() == Wort.lower():
            Index_Wort = k
            print("Ihr Wort" , Wort , "lautet ins Englische übersetzt" ,  woerterbuch_english[Index_Wort] )
            break
        
        elif woerterbuch_english[k].upper() == Wort.upper():
            Index_Wort = k
            print("Your word" , Wort , "is translated to german" ,  woerterbuch_deutsch[Index_Wort] )
            break
    
        k += 1
    if k == max:
        print("Ihr Wort wurde nicht gefunden")
        
    
        