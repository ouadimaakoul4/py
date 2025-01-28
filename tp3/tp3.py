# Écrivez un programme qui demande à l'utilisateur
# un nombre et affiche "Positif" si le nombre est supérieur à 0,
# "Négatif" s'il est inférieur à 0, et "Zéro" s'il est égal à 0.

nombre = float(input("Entrez un nombre: "))
if nombre > 0:
    print("Positif")
elif nombre < 0:
    print("Négatif")
else:
    print("Zéro")
