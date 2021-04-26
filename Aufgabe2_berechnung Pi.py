#Aufgabe2
#Erstellen Sie ein Python-Programm, das unter Verwendung der Leibniz-Reihe den Wert der Zahl Pi näherungsweise berechnet.
#Dabei soll es für den/die BenutzerIn möglich sein, die Anzahl der Iterationen bei Programmbeginn einzugeben.
#Am Ende des Programmlaufs soll der Näherungswert für Pi ausgegeben werden, optional können auch die Zwischenwerte und Iterationsstufen zur Ausgabe gelangen.

piviertel = 0
k = 0
Iterationen = int(input("Bitte geben Sie die gewünschte Anzahl an Iterationen ein:"))

while k < Iterationen:
    
    
    print("k=" , k )
    piviertel =  piviertel + (  ( -1 ) ** k )  / ( 2*k + 1 )
    k = k + 1
    print("pi viertel =" , piviertel )
    
pi = piviertel * 4
print("pi=" , pi )
    
    
    
    
