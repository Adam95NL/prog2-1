import getpass

print('Nieuw account :')

naam = input('Naam: ')
wachtwoord = getpass.getpass(prompt='Wachtwoord: ', stream=None)

bestand = open("./database.txt", "wt")
bestand.write(f"{naam}\n{wachtwoord}\n")
bestand.close()

print('Gebruiker opgeslagen.')