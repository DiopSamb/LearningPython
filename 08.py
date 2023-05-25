# Exercice: The Collatz Sequence
# Ce programme demande à l'utilisateur un nombre entier
# ensuite, il appelle la fonction collatz qui regarde si 
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3*number + 1
        print(number)
    return number
            
print('Donnez un nombre entier svp :\n')
# Ceci est une exception
# les caractéres non entier 
# ne sont pas pris en compte ici
# Donc, on ecrit une exception pour lui dire 
# Que si on a l'erreur ValueError
# De faire le except
try:
    nombre = int(input())
    collatz(nombre)
except ValueError:
    print('Erreur: Ceci n\'est pas un nombre entier ')
#collatz(nombre)

