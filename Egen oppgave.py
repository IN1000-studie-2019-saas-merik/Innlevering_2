# Lag et gjettespill der brukeren skal gjette et tall mellom 1 og 1000.
# Det hemmelige tallet er satt på forhånd.
# For hvert gjett får brukeren bekjed om det hemmelige tallet er høyere eller lavere.
# Når brukeren gjetter riktig får han/hun meldingen "Gratulerer, du gjtettet riktig på x forsøk",
# der x er antall gjett brukeren brukte.

import random

svar = random.randint(1,1000)

print("Hei du ambisiøse gjetter!")
print("Her skal du gjette et tall mellom 1 og 1000.")
print("På hvor få forsøk kan DU finne svaret!?")
gjettet_tall = int(input("Hvilket tall tror du så er svaret [1-1000]:"))

if (gjettet_tall < 1 or gjettet_tall > 1000):
    print("Dette er en ugyldig verdi, no more games for you!")
    exit()
while (gjettet_tall != svar):
    if (gjettet_tall < svar):
        gjettet_tall = int(input("Tallet ditt er for lavt, gjett høyere"))
    elif (gjettet_tall > svar):
        gjettet_tall = int(input("Tallet ditt er for høyt, gjett lavere"))

print(f"Riktig! svaret er {svar}!")
