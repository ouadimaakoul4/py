# Écrivez un programme qui vérifie si une année est bissextile.

annee = int(input("Entrez une année: "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("Bissextile")
else:
    print("Non bissextile")
