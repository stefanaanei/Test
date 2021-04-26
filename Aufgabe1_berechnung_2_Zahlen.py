# Aufgabe 1:
# Schreibe ein Python-Programm, das
# 1) Den Nutzer grüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahl berechnet und ausgibt (kleinere Zahl von großen abziehen)
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotienten kleinerer Zahl durch größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)


Name = input("Bitte geben Sie Ihren Namen ein:")
print("Hallo", Name)

Zahl1_String = input("Bitte geben Sie Ihre erste Zahl ein:")
Zahl1 = int(Zahl1_String) # int erlaubt nur ganze Zahlen

Zahl2 = float(input("Bitte geben Sie Ihre zweite Zahl ein:")) # float erlaubt auch Kommazahlen

#Summe berechnen
Summe = Zahl1 + Zahl2
print("Die Summe Ihrer Zahlen ergibt:",Summe )

#Differenz berechnen
if Zahl2 < Zahl1: #wenn Zahl2 kleiner als Zahl1, wird Zahl1 minus Zahl2 gerechnet
    Differenz = Zahl1 - Zahl2
    print("Die Differenz Ihrer Zahlen ergibt:", Differenz ) #Diese Zeile muss nicht nicht in jeder Funktion da stehen, kann nur einmal am Ende stehen
    
elif Zahl1 < Zahl2: #wenn Zahl1 kleiner als Zahl2, wird Zahl2 minus Zahl1 gerechnet
    Differenz = Zahl2 - Zahl1
    print("Die Differenz Ihrer Zahlen ergibt:", Differenz )

elif Zahl1 == Zahl2: #wenn Zahl1 gleich Zahl2, wird Zahl1 minus Zahl2 gerechnet
    Differenz = Zahl1 - Zahl2
    print("Die Differenz Ihrer Zahlen ergibt:", Differenz )
    
#Produkt berechnen
Produkt = Zahl1 * Zahl2
print("Das Produkt Ihrer Zahlen ergibt:", Produkt )

#Quottient berechnen
if Zahl2 < Zahl1: #wenn Zahl2 kleiner als Zahl1, wird Zahl2 durch Zahl1 gerechnet
    Quottient = Zahl2 / Zahl1
    
elif Zahl1 < Zahl2: #wenn Zahl1 kleiner als Zahl2, wird Zahl1 durch Zahl2 gerechnet
    Quottient = Zahl1 / Zahl2
    
else: #wenn Zahl1 und Zahl2 gleich groß sind, wird Zahl1 durch Zahl2 gerechnet
    Quottient = Zahl1 / Zahl2
    
print("Der Quottient Ihrer Zahlen ergibt:", Quottient )

