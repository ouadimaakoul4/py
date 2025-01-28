# Écrivez un programme qui demande une note (entre 0 et 20) et affiche "Valide"
# si la note est entre 0 et 20, sinon "Invalide".

note = float(input("Entrez une note: "))
if 0 <= note <= 20:
    print("Valide")
else:
    print("Invalide")
