# Demander à l'utilisateur d'entrer son âge et son genre
age = int(input("Veuillez entrer votre âge : "))
genre = input("Veuillez entrer votre genre (H/F) : ").upper()  # Convertir en majuscules pour éviter les erreurs

# Si c'est un homme de plus de 20 ans, il paye l'impôt
if genre == "H" and age > 20:
    print("Vous payez l'impôt.")

# Si c'est une femme entre 18 et 35 ans, elle paye l'impôt
elif genre == "F" and 18 <= age <= 35:
    print("Vous payez l'impôt.")

# Sinon, l'utilisateur ne paye pas l'impôt
else:
    print("Vous ne payez pas l'impôt.")
