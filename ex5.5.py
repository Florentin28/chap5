elec1 = int(input("Veuillez entrer le nombre de voix du premier candidat : "))
elec2 = int(input("Veuillez entrer le nombre de voix du deuxième candidat : "))
elec3 = int(input("Veuillez entrer le nombre de voix du troisième candidat : "))
elec4 = int(input("Veuillez entrer le nombre de voix du quatrième candidat : "))

totalelec = elec1 + elec2 + elec3 + elec4

# Vérification si le candidat 1 est élu dès le premier tour
if elec1 > (totalelec / 2):
    print("Le candidat 1 gagne au premier tour !")

# Vérification si le candidat 1 a perdu complètement (derrière tout le monde)
elif elec1 < max(elec2, elec3, elec4):
    print("Le candidat 1 a perdu")

# Vérification si le candidat 1 peut participer au second tour
elif elec1 >= (totalelec * 0.125):  # 12.5% des voix minimum
    if elec1 > max(elec2, elec3, elec4):
        print("Le candidat 1 est en ballotage favorable")
    else:
        print("Le candidat 1 est en ballotage défavorable")

# Si aucune des conditions ne s'applique, alors il est éliminé
else:
    print("Le candidat 1 est éliminé car il n'a pas atteint 12.5% des voix.")
