bestand = open("powerpoint.txt", "wt")
naam = input("naam?")
ww = input("wachtwoord?")
bestand.write(f"{naam}\n")
bestand.write(f"{ww}\n")
bestand.close()