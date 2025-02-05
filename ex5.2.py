# Demander à l'utilisateur d'entrer l'heure, les minutes et les secondes (on suppose que les entrées sont valides)
heure = int(input("Veuillez entrer l'heure : "))
minute = int(input("Veuillez entrer les minutes : "))
seconde = int(input("Veuillez entrer les secondes : "))

# Ajouter 1 aux secondes, gérer le dépassement de 59 secondes
seconde += 1
if seconde > 59:
    seconde = 0
    minute += 1

# Ajouter 1 aux minutes si elles dépassent 59
if minute > 59:
    minute = 0
    heure += 1

# Si l'heure dépasse 23, la remettre à 0
if heure > 23:
    heure = 0

# Afficher le résultat
print(f"Dans 1 seconde, il sera {heure} heure(s), {minute} minute(s) et {seconde} seconde(s).")
