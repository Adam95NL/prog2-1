naam = input('persoons naam:')
tickets = int(input('Hoeveel tickets wil u kopen:'))
prijs_per_ticket = int(input('prijs per ticket?'))
print(f"""Beste {naam}
Bedankt voor uw bestelling van {tickets} tickets! De totale prijs bedraagt {prijs_per_ticket} euro.
De totale prijs is {tickets*prijs_per_ticket}""")

