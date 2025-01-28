# Écrivez un programme qui demande à l'utilisateur
# un nombre et affiche sa table de multiplication
# jusqu'à 10.

nombre = int(input("Entrez un nombre: "))
for i in range(1, 11):
    print(f"{nombre} x {i} = {nombre * i}")
