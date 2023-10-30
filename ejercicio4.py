ganadores = []
primitiva = ["primer","segundo","tercero","cuarto"]
for i in range(4):
    x = int(input(f"{primitiva[i]} numero ganador de la primitiva (6 numeros): "))
    ganadores.append(x)
ganadores.sort()
ganadores.reverse()
print(f"los gandores son {ganadores} ")