f=open('p022_names.txt','r')
txt = f.read()
 
txtList = txt.split(',')
triTxt = sorted(txtList) #liste des prenoms triés

def valeur_lettre(lettre): #donne la valeur d'une lettre ie on obtient 7 pour G
    valeur=0 #indique le rang d'une lettre dans l'alphabet
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for e in alphabet:
        if e!=lettre: #tant que la lettre n'a pas été rencontré on continue 
                      #à la chercher dans l'alphabet et on incrémente 'valeur' 
            valeur+=1
        if e==lettre: 
            return valeur+1 #dès que l'on rencontre la lettre dans la liste 
                            #c'est que 'valeur' vaut la place de la lettre dans l'alphabet

def namescore(prenom): #donne la somme des valeurs des lettres dans un prénom
    score=0
    for caractere in prenom:
        if caractere=='"':
            score+=0
        else:
            score+=valeur_lettre(caractere)
    return score

assert namescore('COLIN')==53


def solve(liste): #donne le total demandé
    total=0
    for i in range(len(liste)):
        total=total+namescore(liste[i])*(i+1)
    return total

print(solve(triTxt))

