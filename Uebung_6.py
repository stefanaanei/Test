# 1) Funktion zur Eingabe des Befehls 
# 2) Funktion zur Eingabe des Suchbegriffs
# 3) Funktion zur Suche
# 4) Funktion der Ausgabe

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]


def Wortsuche(wordInput):                #Funktion für das Suchen eines Wortes ob es nicht schon im Wörterbuch vorhanden ist.
    Index = 0
    for wort in woerterbuch_deutsch:               #Wenn Wort in Woerterbuch_deutsch = wordinput, dann brich ab und gib den Index aus.
        if wordInput.lower() == wort.lower():  
            break
        Index +=1   
    
    if Index == len(woerterbuch_deutsch):
        Index=0
        for wort in woerterbuch_english:          #Wenn Wort in Woerterbuch_english = wordinput, dann brich ab und gib den Index aus.
            if wordInput.lower() == wort.lower():
                break
            Index +=1    
        
        if index == len(woerterbuch_english):
            raise Exception("Das Wort steht nicht im Wörterbuch")   #Ansonsten gib "Das Wort steht nicht im Wörterbuch" aus. 
    return (woerterbuch_deutsch[Index], woerterbuch_english[Index], Index)
    

def Wort_hinzufügen(Wort_d, Word_e):                                #Funktion für das einfügen eines Wortes an letzter Stelle.
    try:
        Wortsuche(Wort_d)                                           #Überprüfung ob Wort im Wörterbuch nicht schon vorhanden ist.
        print("Wort bereits im Wörterbuch vorhanden")
        
    except:
       woerterbuch_deutsch.append(Wort_d)
       woerterbuch_english.append(Word_e)

def Wort_loeschen():
    try:
        output = Wortsuche(input("Welches Wort möchten sie löschen? "))   #Funktion für das Suchen eines Wortes ob es nicht schon im Wörterbuch vorhanden ist und zur eingabe des zu löschenden Wortes
        woerterbuch_deutsch.remove(output[0])
        woerterbuch_english.remove(output[1])
    except Exception as e:                                          #Wenn try nicht funktioniert, akzeptiere die Fehlermeldung und gib sie aus.
        print(e)
        

def Wort_uebersetzen():
    try:
        output = Wortsuche(input("Welches Wort möchten sie übersetzen? "))   #Funktion für das Suchen eines Wortes ob es nicht schon im Wörterbuch vorhanden ist.
        print(output[0] + "[DE]")
        print(output[1] + "[EN]")
    except Exception as e:                                            #Wenn try nicht funktioniert, akzeptiere die Fehlermeldung und gib sie aus.
        print(e)  

def eingabe_befehl():                                                 #Funktion zur Eingabe des zu anwendeteden Befehls.
    while True:
        Auswahl = input("Was möchten Sie tun? \n Einfügen [E] \n Löschen [L] \n Abfragen [A] \n Abbrechen [Q]:" )
        
        if Auswahl.lower() == "e" or Auswahl.lower() == "l" or Auswahl.lower() == "a" or Auswahl.lower() == "q":     #wenn die Eingabe des Buchstaben mit einem angegebenen Buchstaben übereinstimmt,
            return Auswahl.lower()                                                                                   #gib diesen Buchstaben weiter
        
        else:
            print("Eingabe nicht korrekt. Versuchen Sie es erneut!")
            
            
while True:
    Auswahl = eingabe_befehl()
    if Auswahl == "e":
         Wort_hinzufügen(input("Deutsches Wort eingeben: "), input("Englisches Wort eingeben: "))
    
    elif Auswahl == "l":
        Wort_loeschen()
    
    elif Auswahl == "q":
        break
    
    else:
        Wort_uebersetzen() 
        
    print(woerterbuch_deutsch)
    print(woerterbuch_english)    