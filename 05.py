# Boucle for
# Tu peux utiliser les états continue et break dans la boucle for
# En gros, tu peux utiliser les états continue et break en entré de boucles while et for.
# Si tu l'utilises autre part que ces états python te donnera une erreur
print('My name is')
for x in range(5):
    print('Jimmy five times('+str(x)+')')

# Affiche Jimmy five times((0)) car il y a le break
print('My name is')
for i in range(5):
    print('Jimmy five times('+str(i)+')')
    break

# Il fait l'addition  de 0 à 100 et nous donne la valeur final
total = 0
for num in range(101):
    total = total + num
print(total)

# Tu peux fixer le debut et la fin dans le range()
for i in range(12,16):
    print(i)


# range peut aussi être appeler avec 3 arguments
# Les deux premiers indiquent le debut et la fin 
# Et la troisiéme inquique le pas ou bien le saut
print('Debut range avec 3 arguments')
for i in range(0, 10, 2):
    print(i)

# Peux être utiliser pour des nbres négatives
print('range avec des valeurs négatives')
for i in range(5, -1, -1):
    print(i)
