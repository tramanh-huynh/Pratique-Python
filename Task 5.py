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