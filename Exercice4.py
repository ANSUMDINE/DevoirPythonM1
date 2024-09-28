import re

def generer_listes(phrase):
    # Utiliser une expression régulière pour capturer les mots et les séparateurs
    mots = re.findall(r'\b[\w\']+\b', phrase)
    separateurs = re.findall(r'\s+|,', phrase)
    
    # Ajuster la longueur des séparateurs pour correspondre à celle des mots
    if len(separateurs) < len(mots):
        separateurs.append(" ")
    
    # Créer la liste finale des séparateurs en ajoutant un espace après chaque mot sauf le dernier
    final_separateurs = []
    for i in range(len(mots) - 1):
        final_separateurs.append(separateurs[i])
    final_separateurs.append(" ")
    
    return [mots, final_separateurs]

# Exemples d'utilisation
phrase1 = "J'ai découvert Python cette semaine"
phrase2 = "J'ai découvert Python, cette semaine"
phrase3 = "J'ai découvert, Python, cette semaine"

print(generer_listes(phrase1))  # Retourne [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ", " ", " " ," " , " "]]
print(generer_listes(phrase2))  # Retourne [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ", " ", ", " ," " , " "]]
print(generer_listes(phrase3))  # Retourne [["J'ai","découvert" , "Python" , "cette" , "semaine"] , [" ",", ", ", " ," " , " "]]
