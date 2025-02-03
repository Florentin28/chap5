# __author__ = Florentin

# demander à l'utilisateur d'entrer le jour, le mois et l'année
jour = int(input("Entrez le jour : "))
mois = int(input("Entrez le mois : "))
annee = int(input("Entrez l'année : "))


# Vérifier le nombre de jours dans un mois
if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
    jours_max = 31
elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
    jours_max = 30
elif mois == 2:
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        jours_max = 29  # bissextile
    else:
        jours_max = 28  # pas bissextile

#Vérifier si le jour est valide (min 1 et max le nombre de jours du mois)
if jour < 1 or jour > jours_max:
    print("Le jour n'est pas valide")
else:
    print("Le jour est valide")

    # Ajouter un jour
    jour += 1  
    # Vérifier si le jour dépasse le nombre de jours max du mois
    if jour > jours_max:
        jour = 1  
        mois += 1  

     # Vérifier si c'est le mois de décembre, et passer à janvier
    if mois > 12:
         mois = 1  
         annee += 1  

    # Afficher la date du lendemain
    print("Le lendemain est :",jour, "/",mois, "/",annee)