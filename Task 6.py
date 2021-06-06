#Task 6: Les cinq polyèdres réguliers de Platon sont représentés ci-dessous, avec la formule de leur volume.

#Source des images de polyèdres : Vikidia, l’encyclopédie pour les jeunes, qui explique aux enfants et à ceux qui veulent une présentation simple d'un sujet (https://fr.vikidia.org/wiki/Polyèdre).
#Écrire un programme qui lit :

#la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),

#la longueur de l’arête du polyèdre,

#et qui imprime le volume du polyèdre correspondant.

#Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".

a = input("")
b = float(input())
if a == "C":
    res = b**3
    print(res)
elif a == "T":
    res = ((2**(1/2))/12)*(b**3)
    print(res)
elif a == "O":
    res = ((2**(1/2))/3)*(b**3)
    print(res)
elif a == "D":
    res =((15 + 7*(5**(1/2)))/4)*(b**3)
    print(res)
elif a == "I":
    res = ((5*(3+5**(1/2)))/12)*(b**3)
    print(res)
else:
    print("Polyèdre non connu")