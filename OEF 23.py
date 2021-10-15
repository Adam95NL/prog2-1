import random

bestand = open("opgave23.svg", "wt")
bestand.write(f"""
<svg version="1.1"
    baseProfile="full"
    width="1920" height="1080"
    xmlns="http://www.w3.org/2000/svg">\n
""")
for x in range(0,100):
    for y in range(0,100):
        bestand.write(f'    <circle cx="{x}" cy="{y}" r="{random.randint(50,200)}" fill="green" />\n')

bestand.write("</svg>")
bestand.close()