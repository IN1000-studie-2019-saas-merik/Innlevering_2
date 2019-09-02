#Oppgave 2: Konvertering

# nå skal vi definere en variabel som blir gitt ved brukerinput
# her bruker vi float slik at vi ikke er bundet til heltall

temp_f = float(input("Skriv inn en temperatur i fahrenheit: "))
print(f"du skrev inn: {temp_f} Fahrenheit") # verifiserer for brukeren av programmet verdien som ble skrevet inn

# vi skal så bruke formelen for omregning av fahrenheit til celsius og bruker round-metoden og tilater kun 2 desimaler
temp_c = round((temp_f - 32) * 5/9, 2)

# vi må også ta en sjekk med en "if-setning" for å sjekke at inputen er gyldig
# siden -459.67 Fahrenheit = -273.15 Celsius (0 Kelvin, absolutt nullpunkt) så kan ikke temperaturen være lavere,
# dermed har vi vår bunnverdi. vi kunne like godt sjekket temp_c >= -273.15 her.
# er verdien under 0 Kelvin så har noe ugyldig blitt skrevet inn og programmet avslutter.
if (temp_f >= -459.67):
    print(f"Dette blir {temp_c} i Celsius")
else:
    print("Dette er en ugyldig verdi!")
    exit()
