# Demander à l'utilisateur le nombre de photocopies
nphoto = int(input("Veuillez entrer le nombre de photocopies désiré : "))

# Calcul du prix en fonction du nombre de photocopies
if 0 < nphoto < 11:
    prix = nphoto * 0.05
    print(f"Votre facture s'élève à {prix:.2f} euros.")

elif 10 < nphoto < 21:
    prix = nphoto * 0.04
    print(f"Votre facture s'élève à {prix:.2f} euros.")

elif nphoto > 20:
    prix = nphoto * 0.03
    print(f"Votre facture s'élève à {prix:.2f} euros.")

# Si le nombre est invalide
else:
    print("Veuillez entrer un nombre valide.")
