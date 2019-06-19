import sys

fic = sys.argv[1]
fic_temps = open(fic).read()
fic_temps = fic_temps.split("\n")
with open ("k.txt", "w", encoding="utf-8") as kaka:
    for x in fic_temps:
        x = x.split("\t")
    
        kaka.write("%.2f"% float(x[4])+"\n")