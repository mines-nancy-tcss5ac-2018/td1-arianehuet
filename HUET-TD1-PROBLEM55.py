def EstUnPalindrome(nombre): #nous indique si un nombre est un palindrome ou non
     i=0
     nombrebis=str(nombre)
     longueur=len(nombrebis)
     while i<longueur:
          if nombrebis[i]!=nombrebis[-i-1]: #on regarde si les lettres de part et d'autre 
                                            #du mot sont egales puis on refait de même en se 
                                            #rapprochant du centre a chaque fois
               return False
          i+=1
     return True

def Somme(n): #renvoie la somme d'un nombre et de son 'inverse' 
              #ie Somme(47) renvoie la valeur de 47+74
     n1=str(n)
     n2=list(n1)
     n3=''
     for k in range(len(n2)-1,-1,-1):
          n3+=n2[k]          
     return int(n3)+n

def EstDeLychrel(n): #nous indique si un nombre est de Lychrel
     i=0
     s=Somme(n)
     while i<=50: 
          if EstUnPalindrome(s):
               return False #si on obtient un palindrome nous n'avons pas un nombre de Lychrel
          else:
               s=Somme(s) #sinon on réitère les opérations sur la somme obtenue précédemment
               i+=1
     return True #on sait que tout nombre en dessous de 10000 
                  #devient un palindrome en moins de 50 itérations 
                  #donc si l'on sort de la boucle while c'est qu'au bout
                  #de 50 itérations nous n'avons pas obtenu de palindrome
                  #et donc nous avons bien affaire à a un nombre de Lychrel

def solve(n): #compte le nombre de nombres de Lychrel entre 0 et n
     res=0
     for i in range(n+1):
          if EstDeLychrel(i):
               res+=1
     return res

print(solve(10000))

      

        