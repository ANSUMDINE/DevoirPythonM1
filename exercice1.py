def eviter_doublons(liste, index):
    return index > 0 and liste[index] == liste[index - 1]

def trouver_groupes(liste, i, gauche, droite):
    resultats = []
    while gauche < droite:
        somme = liste[i] + liste[gauche] + liste[droite]
        if somme == 0:
            resultats.append([liste[i], liste[gauche], liste[droite]])
            gauche, droite = avancer_indices(liste, gauche, droite)
        elif somme < 0:
            gauche += 1
        else:
            droite -= 1
    return resultats

def avancer_indices(liste, gauche, droite):
    while gauche < droite and liste[gauche] == liste[gauche + 1]:
        gauche += 1
    while gauche < droite and liste[droite] == liste[droite - 1]:
        droite -= 1
    return gauche + 1, droite - 1

def trouver_groupes_somme_zero(liste):
    resultats = []
    liste = sorted(liste)
    n = len(liste)
    
    for i in range(n - 2):
        if eviter_doublons(liste, i):
            continue
        resultats.extend(trouver_groupes(liste, i, i + 1, n - 1))
    
    return resultats

# Exemple d'utilisation
liste1 = [2, 7, 9, -9]
liste2 = [-33, -10, -8, -2, 1, 4, 9, 10]
liste3 = [5, 12, -7, 3, 9, -2, 8, 15, -10, 4, 6, -1, 11, -5, 7, 2, -3, 14, -4, -6]

print(trouver_groupes_somme_zero(liste1))  # [[2, 7, -9]]
print(trouver_groupes_somme_zero(liste2))  # [[-10, 1, 9], [-8, -2, 10]]
print(trouver_groupes_somme_zero(liste3))