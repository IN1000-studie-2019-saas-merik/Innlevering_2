#Oppgave 2: Konvertering

# nå skal vi definere en variabel som blir gitt ved brukerinput
# her bruker vi float slik at vi ikke er bundet til heltall

temp_f = float(input("Skriv inn en temperatur i fahrenheit: "))
print(f"du skrev inn: {temp_f} Fahrenheit")

temp_c = round((temp_f - 32) * 5/9, 2)

# vi må også ta en sjekk med en "if-setning" for å sjekke at inputen er gyldig
# siden -459.67 = -273.15 Celsius så kan ikke temperaturen være lavere, dermed har vi vår bunnverdi
if (temp_f >= -459.67):
    print(f"Dette blir {temp_c} i Celsius")
else:
    print("Dette er en ugyldig verdi!")
    exit()