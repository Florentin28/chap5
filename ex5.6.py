# Demander à l'utilisateur de rentrer ses informations
age = int(input("Veuillez entrer votre âge : "))  
anciennete_permis = int(input("Depuis quand avez-vous votre permis de conduire ? (en années) : "))  
accident = int(input("Combien d'accidents avez-vous provoqué ? (0 si aucun) : "))  
fidelite = int(input("Depuis quand êtes-vous client chez nous ? (en années) : "))  

couleur = None  

# Condition pour le tarif "ROUGE"
if age < 25 and anciennete_permis < 2 and accident == 0:  # Si le conducteur est jeune (<25) et avec moins de 2 ans de permis sans accident
    couleur = "ROUGE"  
elif age < 25 and anciennete_permis < 2 and accident != 0:  # Si le conducteur est jeune et avec moins de 2 ans de permis et a eu un ou plusieurs accidents
    couleur = "Refusé"  

# Condition pour le tarif "ORANGE" Si l'âge et l'ancienneté du permis correspondent aux critères
elif ((age < 25 and anciennete_permis >= 2) or (age >= 25 and anciennete_permis < 2)):  
    if accident == 0:  # Si le conducteur n'a pas eu d'accident
        couleur = "ORANGE"  
    elif accident != 0:  # Si le conducteur a eu un ou plusieurs accidents
        couleur = "ROUGE"  

# Condition pour le tarif "VERT" Si le conducteur a plus de 25 ans et a plus de 2 ans de permis
elif age > 25 and anciennete_permis >= 2:  
    couleur = "VERT"  # Attribuer le tarif VERT

else:
    couleur = "Refusé"  # Si aucune des conditions n'est remplie, on le refuse

# Vérification de la fidélité pour appliquer une promotion si le client est fidèle depuis plus de 5 ans et n'est pas refusé
if fidelite > 5 and couleur != "Refusé":  
    if couleur == "VERT":  
        couleur = "BLEU"  
    elif couleur == "ORANGE":  
        couleur = "VERT"  
    elif couleur == "ROUGE": 
        couleur = "ORANGE" 

# Affichage du résultat final
if couleur == "Refusé":  
    print("Nous ne pouvons pas vous assurer.")  
else:
    print(f"Vous êtes {couleur}.")  
