#Task 1: Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, imprime cette valeur (le programme n’imprime rien dans le cas contraire).

a = int(input())
b = int(input())
c = int(input())
if a == b or a == c:
    res = a
    print(res)
elif b == c:
    res = b
    print(res)

#Task 2: Écrire un programme qui, si temperature (entier lu sur input correspondant à la température maximale prévue pour aujourd’hui) est strictement supérieur à 0, teste si temperature est inférieur ou égal à 10, auquel cas il imprime le texte :

#Il va faire frais.

#et qui, si temperature n’est pas supérieur à 0, imprime le texte :

#Il va faire froid.

#Dans les autres cas, le programme n’imprime rien.

temperature = int(input())
if temperature > 0:
    if temperature <= 10:
        print("Il va faire frais.")
else:
    print("Il va faire froid.")

#Task 3: Écrire un programme qui lit trois entiers a, b et c en input. Ensuite :

#si l’entier c est égal à 1, alors le programme affiche la valeur de a + b ;

#si c vaut 2, alors le programme affiche la valeur de a - b ;

#si c est égal à 3, alors l’output sera la valeur de a.b (produit de a par b) ;

#enfin, si la valeur 4 est assignée à la variable c, alors le programme affiche la valeur de a^2 + a.b ;

#et si c contient une autre valeur, le programme affiche le message Erreur.

a = int(input())
b = int(input())
c = int(input())
if c == 1:
    res = a + b
    print(res)
elif c == 2:
    res = a - b
    print(res)
elif c == 3:
    res = a*b
    print(res)
elif c == 4:
    res = (a**2) + (a*b)
    print(res)
else:
    print("Erreur")

#Task 4: Écrire un programme qui teste la parité d’un nombre entier lu sur input et imprime True si le nombre est pair, False dans le cas contraire.

number = int(input())
if number % 2 == 0:
    print("True")
else:
    print("False")

#Task 5: Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.

#Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.

a = int(input())
b = int(input())
if a > b and a%b == 0:
    print("False")
elif b > a and b%a == 0:
    print("False")
elif a == b and a%b == 0:
    print("False")
else:
    print("True")

#Task 6: Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} (la racine carrée du produit de a par b) de deux nombres positifs a et b de type float lus en entrée.

#Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur ».

a = float(input())
b = float(input())
if a >= 0 and b >= 0:
    res = (a*b)**(1/2)
    print(res)
else:
    print("Erreur")

#Task 7: Les cinq polyèdres réguliers de Platon sont représentés ci-dessous, avec la formule de leur volume.

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
    