import random
letters = "abcdefghijklmnopqrstuvwxyz"
bestandsnaam = input("Hoe wilt u het bestand noemen?: ")
letter1 = random.choice(letters)
letter2 = random.choice(letters)
letter3 = random.choice(letters)
letter4 = random.choice(letters)
letter5 = random.choice(letters)
letter6 = random.choice(letters)
letter7 = random.choice(letters)
letter8 = random.choice(letters)
wachtwoord = f"{letter1}{letter2}{letter3}{letter4}{letter5}{letter6}{letter7}{letter8}"
bestand = open(f"{bestandsnaam}.txt", "wt")
bestand.write(f"key = {wachtwoord}")
bestand.close()