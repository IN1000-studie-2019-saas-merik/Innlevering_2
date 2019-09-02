#Oppgave 1: Utskriftsprosedyre

# Her lager vi en funksjon, som gjør at vi kan definere en mindre kode som vi
# senere kan kalle og benytte ved å bare kalle funksjonsnavnet.
def utskriftsprosedyre():
    navn = input("Skriv inn navn: ")            #definerer navn "stringen"
    origin = input("Hvor kommer du fra? ")      #definerer opphavssteds "stringen"
    print(f"Hei, {navn}! Du er fra {origin}.")  #skriver ut en setning med input-en vi akkurat skrev inn

#skriver nå ut tre ganger den funksjonen vi akkurat definerte
utskriftsprosedyre()
utskriftsprosedyre()
utskriftsprosedyre()


