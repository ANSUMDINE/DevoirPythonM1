
def deviner_nombre(t, g, d, coups, historique):
    '''
    La récursive de la recherche dichotomique
    '''
    if g == d :
        print(f"Script propose {t[g]}... +, - ou G ?")
        reponse = input().strip()
        if reponse == "G":
            print(f"Script a trouvé {t[g]} en {coups} coups !!!")
        else:
            print(f"Tricheur !!! A la réponse {coups} il avait été proposé {t[g]} et tu as donnée une autre directive !!!")
            print(f"J'ai gagné par forfait en {coups} coups !!!")
    else:
        coups +=1
        m = (g+d)//2
        if t[m] in historique:
            print(f"Tricheur !!! A la réponse {coups} il avait été proposé {t[m]} et tu as donnée une autre directive !!!")
            print(f"J'ai gagné par forfait en {coups} coups !!!")
        else:
            historique.append(t[m])
            print(f"Script propose {t[m]}... +, - ou G ?")
            reponse = input().strip()
            if reponse == "+":
                return deviner_nombre(t, m+1, d, coups, historique)
            elif reponse == "-":
                return deviner_nombre(t, g, m, coups, historique)
            elif reponse == "G":
                print(f"Script a trouvé {t[m]} en {coups} coups !!!")


def commencer():
    tableau = [i for i in range(1, 101)]
    print("Mémorisez un nombre entier entre 1 et 100, le script va essayer de le retrouver, ne trichez pas !")
    # Utilisons la récursive de la recherche dichotomique
    historique = []
    coups = 0
    deviner_nombre(tableau, 0, 99, coups, historique)

commencer()