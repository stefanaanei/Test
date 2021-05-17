# Eingabe eines Wortes
# automaschies erkennen ob deutsch oder engllisch
# Wort wird übersetzt
# zusatzinfo auf sprache des übersetzten Wortes

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

Wort = input("Bitte geben Sie Ihr Wort ein das Sie übersetzen wollen:")

Index_Wort = 0
k = 0
Iterationen = len(woerterbuch_deutsch)

while k < Iterationen:
    
    if woerterbuch_deutsch[k].upper() == Wort.upper():
        Index_Wort = k
        print("Ihr Wort" , Wort , "lautet ins Englische übersetzt" ,  woerterbuch_english[Index_Wort] )
        break
        
    elif woerterbuch_english[k].upper() == Wort.upper():
        Index_Wort = k
        print("Your word" , Wort , "is translated to german" ,  woerterbuch_deutsch[Index_Wort] )
        break
    
    else:
        print("Ihr Wort konnte nicht gefunden werden")
        break
    
    k += 1