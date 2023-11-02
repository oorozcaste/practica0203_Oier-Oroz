palabra = list(input("dime una palabra: "))
alderantziz=list(palabra)
alderantziz.reverse()
if palabra == alderantziz:
    print("la palabra es un palindromo")
else:
    print("no lo es")