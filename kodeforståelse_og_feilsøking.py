#Oppgave 4

#1. Nei denne koden vil ikke uten videre fungere.
#grunnen til det er at vi i "print-setningen" prøver å skrive en "int" sammen med en streng.
#da prøver programmet å summere int(b) med strengen "Hei!", noe som ikke er mulig.

#problemet kan løses som under, ved å gjøre om heltallet "b" til en streng igjen, og behandle den der etter.
#da får vi en "vanlig" print-setning med bare strenger og resultatet blir en setning.
a = input("Tast inn et heltall!")
b = int(a)

if b < 10:
    print(str(b) + " Hei!")