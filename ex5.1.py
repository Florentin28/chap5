# Demander à l'utilisateur d'entrer l'heure et les minutes (on suppose que les entrées sont valides)
heure = int(input("Veuillez entrer l'heure : "))
minute = int(input("Veuillez entrer les minutes : "))

# Ajouter 1 aux minutes, gérer le dépassement de 59 minutes
minute += 1
if minute > 59:
    minute = 0
    heure += 1

# Si l'heure dépasse 23, la remettre à 0
if heure > 23:
    heure = 0

# Afficher le résultat
print(f"Dans 1 minute, il sera {heure} heure et {minute} minutes.")
