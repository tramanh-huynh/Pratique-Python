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