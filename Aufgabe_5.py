# Erstellen eines Wörterbuches mittels dictionaries

woerterbuch_deutsch = {"Apfel" : "apple",
                       "Birne" : "pear",
                       "Kirsche" : "cherry",
                       "Melone" : "melon",
                       "Marille" : "apricot",
                       "Pfirsich" : "peach",
                       }

woerterbuch_englisch = { "apple" : "Apfel",
                         "pear" : "Birne",
                         "cherry" : "Kirsche",
                         "melon" : "Melone",
                         "apricot" : "Marille",
                         "peach" : "Pfirsich",
                         }

def eingabe_befehl():
    Bedingung = False
    while Bedingung == False:
        Auswahl = input("Was möchten Sie tun? \n Von Englisch auf Deutsch übersetzen [E] \n Von Deutsch auf Englisch übersetzen [D]:" )
        Auswahl = Auswahl.upper()
        
        if Auswahl == "E":
            Bedingung = True
            return Auswahl
        
        elif Auswahl == "D":
            Bedingung = True
            return Auswahl
        
        else:
            print("Eingabe nicht korrekt. Versuchen Sie es erneut!")
            
            
Auswahl = eingabe_befehl()


if Auswahl == "E":
    eingabe = input("Please type your word you would like to translate ")
    
    try:
        print(woerterbuch_englisch[eingabe])
    except KeyError:
        print("Your word is not in the dictionary")
        
elif Auswahl == "D":

    eingabe = input("Bitte geben Sie Ihr Wort ein das Sie übersetzen wollen: ")

    try:
        print(woerterbuch_deutsch[eingabe])
    except KeyError:
        print("Ihr Wort wurde nicht gefunden")
