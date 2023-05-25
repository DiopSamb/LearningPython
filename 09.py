###########################______Les_Lists______##############################
# Les Lists sont un type de données
# Une lists est une valeur qui contient plusieurs valeurs dans une séquence ordonnée
# Exemple de list: ['cat', 'bat', 'rat', 'elephant'] 


liste =  [1, 2, 3]
print(liste)

Animaux_domestiques = ['ouloudou','mballou','réwadou','mbéwa','naggé']
print(Animaux_domestiques)

# Mélange de chaine de caratéres, de réel, 
Melang_liste = ['hello', 3.1415, True, None, 42]


spam = ['cat', 'bat', 'rat', 'elephant']
#     ___î     __î   ___î     __î
#    /        /     /        /
#spam[0]  Spam[1] spam[2] spam[3]
#
#Exemple:
print('Ici on va afficher les valeurs de la liste spam') 
for n in range(4):    
    print(spam[n])
# On peut aussi faire ces manipulation
    print('Hello '+ spam[n])


# Maintenant qu'on la manipulation d'exception 
# On peut faire cette manipulation
# print('Exemple avec try et excepr')
# try:
#     print(spam[100])
# except IndexError:
#     print('Tu as dépassé l\'index de notre liste')

# Python te donnera une message d'erreur IndexError si tu 
# utilise un index qui dépasse le nombre de valeur dans ta valeur liste
# Exemple
# print(spam[100])

###########################################################################
## Note:  Les endexes peut uniquement être des valeurs entier et not réels#
###########################################################################


# Les listes peuvent contenir d'autres listes.
# Les listes de ce listes peuvent être accédé
# en utilisant plusieurs indexes. 
listes_dans_liste =  [['cat', 'bat'], [10,      20,    30,     40,       50]]
#                      [0][0]  [0][1]  [1][0]  [1][1]  [1][2]  [1][3]    [1][4]
#                    <--------------->   <----------------------------------------> 
#                        indexe [0]                      indexe[1]
# Affiche la premiére valeur de la listes_dans_liste qui est ['cat', 'bat']
print(listes_dans_liste)
print(listes_dans_liste[0])
# On peut aller plus loin, on peut manipuler les valeurs de la premiére
# liste de notre grande list listes_dans_liste
print(listes_dans_liste[0][1])
#     __________________î  î____________      
#    /                                  | 
#['cat','bat']                          bat

# Indexes négatives
#Il affiche la derniére liste de listes_dans_liste
print(listes_dans_liste[-1])

# On va affiché le 10 de notre derniére liste de la liste liste_dans_liste
print('On va affiché le 10 de notre derniére liste de la liste liste_dans_liste')
print(listes_dans_liste[-1][0])

# Tout comme un index peut obtenir une seule valeur d'une liste, une tranche peut obtenir plusieurs valeurs
# à partir d'une liste, sous la forme d'une nouvelle liste. Une tranche est tapée entre crochets,
# comme un index, mais il a deux entiers séparés par deux-points. Remarquez la différence
# entre les index et les tranches.
# Exemples: Afficher une tranche de spam = ['cat', 'bat', 'rat', 'elephant']
# Là on va afficher 3 éléments de spam
for n in range(4):
    for i in range(4):
        print('Là on va afficher '+str(n)+' éléments de spam')
        print(spam[0:n])

# On a aussi d'autre manipulation
#  affiche ['cat', 'bat']
print(spam[ : 2])
#       ___î
#       ||  
#       0

#
# Affiche de 1 jusqu'à la fin
#            __i_____________i
#            |
print(spam[1:])

#
#
# Là évidemment de 0 jusqu'à la fin
print(spam[ : ])
#          | | 
#         /   \
#        ||   ||
#        0    jusqu'à la fin

# On a la fonction len() pour obtenir le nombre d'éléments de la liste
print('Le nombre d\'éléments de la liste '+str(len(spam)))

######################################
#                                    #
# Changement de valeur dans un liste #
######################################

spam[2] = spam[1]
print(spam[2])
spam[-1] = 12345
print(spam[-1])

#################
#               #
# L'opérateur + #
#               #
#################
# L'opérateur + peut combiner deux listes pour créer une nouvelle liste
# de la même façon il combines deux caractéres pour former un nouveau caratére.
liste_1 = ['A','B','C']
print('liste_1 ='+str(liste_1))
liste_2 = ['1','2','3']
print('liste_2 ='+str(liste_2))
liste_combiner = liste_1 + liste_2
print('liste_combiner ='+str(liste_combiner))
#################
#               #
# L'opérateur * #
#               #
#################
#L'opérateur * peut aussi être utiliser avec une liste
# et une valeur entier pour répliquer la liste
#
liste_repliquer = liste_combiner * 3
print('liste_repliquer ='+str(liste_repliquer))

#######################################################
#                                                     #
# Suppression de valeurs dans un liste avec l'état del#                       
#                                                     #
#######################################################

liste_initial = [0,1,2,3,4,5,6,7,8,9]
print('liste initial= '+str(liste_initial))
del liste_initial[0]
print('liste avec un élément supprimé ='+str(liste_initial))
#
# 
print('Faisons une petite manipulation.\nOn va faire un liste pair et une liste impaire\nde la liste initiale')
liste_Initial = [0,1,2,3,4,5,6,7,8,9]
paire = []
impaire = []
for i in liste_Initial:
    if i % 2 == 0:
# append permet d'ajouter un éléments à la fin de la liste
        paire.append(i)
    else:
        impaire.append(i)
print('Liste paire ='+str(paire))
print('Liste impaire ='+str(impaire))

###############################################
#                                             #
#           Boucle dans une liste             #
###############################################
for i in [0, 1, 2, 3]:
    print(i)
# Un autre exemple
Utilisation_liste_dans_boucle = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
liste_de_0_à_10 = []
liste_de_11_à_20 = []
for i in Utilisation_liste_dans_boucle:
    if i < 11:
        liste_de_0_à_10.append(i)
    else:
        liste_de_11_à_20.append(i)
print('Liste de 0 à 10 =' +str(liste_de_0_à_10))
print('Liste de 11 à 20 =' +str(liste_de_11_à_20))

#################################################################
# Les opérateurs in et not pour des manipulations dans une liste#
# ############################################################### 
#
salutation = ['salut','hello','mbadda','nakamou']

# Créer des fonctions pour l'addition, la soustraction, la multiplication et la division

