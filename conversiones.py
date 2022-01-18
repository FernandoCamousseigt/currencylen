import sys

tasa_sol = float(sys.argv[1]) 
tasa_ars = float(sys.argv[2])
tasa_usd = float(sys.argv[3])
clp = float(sys.argv[4])

conv_clp_sol = clp * tasa_sol
conv_clp_ars = clp * tasa_ars
conv_clp_usd = clp * tasa_usd

print("Los {} pesos equivalen a:".format(clp))
print(f"{conv_clp_sol:.1f} Soles")
print(f"{conv_clp_ars:.1f} Pesos Argentinos")
print(f"{conv_clp_usd:.1f} Dólares")

print("___________________")
print("option2 using round:")
print(round(conv_clp_usd,1)," Dólares")


