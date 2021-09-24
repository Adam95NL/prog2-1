print("""
<svg version="1.1"
    baseProfile="full"
    width="300" height="200"
    xmlns="http://www.w3.org/2000/svg">
    """)
for circle in range(0,10):
    print('    <circle cx="150" cy="100" r="80" fill="green" />')
    
print("</svg>")