asignaturas = ["matematicas", "Física", "Química", "Historia", "Lengua"]
ezgaindituak = []
for i in asignaturas:
    x = float(input(f"cual es tu nota en {i} "))
    if x < 5:
        ezgaindituak.append(i)
print("estas son tus asignaturas pendientes ",ezgaindituak)