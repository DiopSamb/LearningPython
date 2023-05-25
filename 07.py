# Function

# Fonction sans arguments
def hello():
    print('Howdy!')
    print('Howdy!!:')
    print('Hello there')

# Fonction avec argumments
def helloArg(name):
    print('Hello '+name)

# Appel de fonction sans arguments 
hello()

# Appel de fonction avec arguments
helloArg('Samba')
helloArg(str(1))


import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)
print(r)
fortune = getAnswer(r)
print(fortune)

# la valeur None
# En python c'est une valeur appelé None, lequel représente l'absence de valeur
# None est une valeur unique du type de donné NoneType(Les autres languages de programmation
# devait l'appelé la valeur null, nil ou undefined). Juste comme les valeurs Booléen True et False
# None doit être tapé avec un N 

# Exemples dans un shell interactive
# >>> spam = print('Hello!')
# Hello!
# >>> None == spam
# True 

############################## Dés paramétres dans les fonctions appelés #######################
# Toutefois, les mots clés d'arguments sont identifié par des mots clés mis avant 
# eux dans la fonction print(). Les mots clés d'arguments sont souvent utilisé pour 
# des paramétres optionnels. Par exemple, la fonction print() a des paramétres optionnels 
# end et sep pour spécifier que pourra être imprimé à la fin de l'arguments et entre leurs arguments(leur sépare) respectivement

print('Pour les paramétres optionels')
print('Hello', end='')
print('World')
# Séparation sep dans print() en tant que paramétres optionnel
print('cats', 'dogs', 'mice', sep=',')

############
# Si tu as besoin de modifier pour un variavle global dans un fonction,
# utilise l'état global. Si tu as une line de code tels que global eggs en haut 
# d'une fonction, il dit à python, "Dans cette fonction, eggs refére à un variabke global
# ainsi ne crée pas de variable local avec ce nom"
print("Tranformer varible local en global")
def spam():
 global eggs
 eggs = 'spam'
eggs = 'global'

spam()
print(eggs)

########################Manipulation d'exception########################
# Les erreurs peuvent être manipulé avec les états try et except.
# Le code qui pourra potentiellement avoir une erreur est mis dans une clause try.
# Ce programme d'exécution se déplace au debut du clause suivant except si une erreur se produit

print('La manipulation d\'exception commence ici')
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

##########
#Exercice######################################
##########
# C'est un jeu de devinette de numéro
# On demande au joueur de deviner le numéro
# qu'on pense
import random

NombreSecret = random.randint(1, 20)
print('Bienvenue au jeux deviner de mon numéro\n')
print('Donnez votre nom complet ou pseudo')
NomPlayers=input()
print('Bonne chance '+NomPlayers)
print('S\'il plait donner votre numéro : ')
NombreDevine = int(input())

if NombreDevine > NombreSecret:
    print('Votre nombre est plus grand. Désolé '+NomPlayers+ ' :)')
elif NombreDevine <NombreSecret:
    print('Votre nmbre est plus petit. Désolé '+NomPlayers+ ' :)')

if NombreDevine == NombreSecret:
    print('Good job '+NomPlayers)
else:
    print('Désolé, je ne pensais pas à ce numéro '+NomPlayers)

print('Voici mon numéro '+str(NombreSecret) )

