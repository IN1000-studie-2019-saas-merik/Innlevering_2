#Oppgave 5
# Overordnet: Jeg og Håkon Moen Eriksen, syntes det var mer interessant dersom vi lagde oppgaveteksten til hverandre
# når vi nå uansett var på samme sted. jeg har derfor løst oppgaven som han lage i Oppgave 5: 1. og han har løst min.

#1. Oppgavetekst
# Lag et gjettespill der brukeren skal gjette et tall mellom 1 og 1000.
# Det hemmelige tallet er satt på forhånd.
# For hvert gjett får brukeren bekjed om det hemmelige tallet er høyere eller lavere.
# Når brukeren gjetter riktig får han/hun meldingen "Gratulerer, du gjtettet riktig på x forsøk",
# der x er antall gjett brukeren brukte.

import random # her importerer vi "random" modulen, slik at vi kan nytte oss av et "tilfeldig" for hver gjennomføring

# under definerer vi den ukjente variabelen (x i oppgaveteksten) som kjøreren av programmet skal komme fram til.
# vi benytter oss av modulen som vi akkurat importerte og velger at det "tilfeldige" tallet skal være mellom 1 og 1000.
svar = random.randint(1,1000)

# ettersom kjører av programmet skal få en tilbakemelding på hvor mange forsøk det tok å komme fram svaret, lager vi
# variabelen under og setter den til tallverdien 1, og lar den senere øke med 1 for hver gang kjøreren gjetter feil.
antall_gjett = 1

print("Hei du ambisiøse gjetter!") # her får bare kjøreren av programmet en velkomsthilsen
print("Her skal du gjette et tall mellom 1 og 1000.") # og en innføring i reglene for "spillet"
print("På hvor få forsøk kan DU finne svaret!?")

# under gir vi kjøreren av programmet muligheten til å gjøre sitt første gjett. tallet som da skrives inn lagres som
# en integer i variabelen "gjettet_tall".
gjettet_tall = int(input("Hvilket tall tror du så er svaret [1-1000]:"))

# deretter kjører vi en while-loop som først sjekker om tallet vi skrev inn i "gjettet_tall" over er likt tallet som er
# lagret i "svar"-variabelen. Dersom det er tilfellet går den forbi loopen og videre nedover i koden.
# dersom vi ikke gjetter det riktige tallet, vil while-loopen kjøre. og basert på tallet vi skrev inn sist
# vil den gi en tilbakemelding på om vi har gjettet for høyt eller lavt. dersom tallet vi gjettet er utenfor det lovlige
# området, 1-1000, i dette tilfellet, får vi tilbakemelding på at vi har brutt reglene og programmet avslutter.
while (gjettet_tall != svar):
    if (gjettet_tall < 1 or gjettet_tall > 1000):
        print("Dette er en ugyldig verdi, no more games for you!")
        exit()
    elif(gjettet_tall < svar):
        gjettet_tall = int(input("Tallet ditt er for lavt, gjett høyere"))
    elif (gjettet_tall > svar):
        gjettet_tall = int(input("Tallet ditt er for høyt, gjett lavere"))
         # her øker vi variabelen "antall_gjett" med 1 for hver gjennomføring av while-loopen, slik at vi senere kan gi
         # kjøreren av programmet tilbakemelding på hvor mange forsøk som ble brukt på å finne svaret.
    antall_gjett = antall_gjett + 1
# Når vi har kommet hit i koden er vi ferdige med å gjette, vi har funnet det riktige svaret og brutt ut av while-loopen
# det eneste som da gjenstår er å gi kjøreren en tilbakemelding på at svaret var riktig og hvor mange forsøk det tok
# å komme fram til det.
print(f"Riktig! svaret er {svar}!")

# det er nærmere 13% sannsynlighet for å gjette riktig på sitt 7 gjett. så klarer en det på 7 eller mindre er det
# veldig bra.
if (antall_gjett <= 7):
    print(f"Gratulerer, du gjettet riktig på {antall_gjett} forsøk, utmerket!")
# sannsynligheten for å gjette riktig stiger raskt dersom en fortsetter å halvere. og etter 10 gjett/halveringer finner
# man garantert det ukjente tallet.
elif(antall_gjett >= 8 and antall_gjett <= 10 ):
    print(f"Gratulerer, du gjettet riktig på {antall_gjett} forsøk, ikke dårlig!")
# med mindre man har ikke har klart å halvere riktig/ gjette på best måte. og får da tilbakemelding på at en kan
# finne en mer effektiv måte å komme fram til svaret på.
elif(antall_gjett > 10):
    print(f"Gratulerer, du gjettet riktig på {antall_gjett} forsøk, kommer du på en bedre måte å finne svaret på?")
    
# program ferdig.
