asignaturas = ["matematicas", "Física", "Química", "Historia", "Lengua"]
notak = []
for i in asignaturas:
    x = float(input(f"cual es tu nota en {i} "))
    notak.append(x)
for z in range(5):
    print(f"has sacado un {notak[z]} en {asignaturas[z]}")