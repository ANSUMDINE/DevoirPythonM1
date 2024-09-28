def convertir_nombres(liste):
    nombre = 0
    for i,j in enumerate(reversed(liste)):
        nombre += j * (10 ** i)
    return nombre

def total(n1, n2):
    # Convertir les listes en nombres entiers
    num1 = convertir_nombres(n1)
    num2 = convertir_nombres(n2)
    
    # Faire l'addition
    total = num1 + num2
    
    # Convertir le total en liste
    resultat = []
    while total > 0:
        resultat.append(total % 10)
        total //= 10
    
    # Reverser la liste pour obtenir le bon ordre
    return resultat[::-1]

# Exemple d'utilisation
n1 = [1, 2, 3]
#n1 = [10, 2, 7]
n2 = [7]
print(total(n1, n2))  # Output: [1, 3, 0]
