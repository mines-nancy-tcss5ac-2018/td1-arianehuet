def solve(n):
    resultat=0
    nombre=str(2**n) #on transforme le nombre en chaine
    for i in nombre:
        resultat+=int(i) #on transforme les nombres en entiers pour pouvoir les ajouter
    return resultat

assert solve(15)==26
print(solve(1000))

