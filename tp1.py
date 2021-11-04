
 #exercice 1:

def fact(x): 
  if x == 1:
    return 1 # 1!=1
  else:
    return x * fact(x-1) #la recursivite jusqu'a x=1
somme=0
n=5
for x in range (1,n+1,1):
  somme=somme+fact(x)/x
print(somme) #affichage du resultat


#exercice 2

num=10
def binaire(num): #declaration de la fonction
  f=1
  bin=0
  while(num>0) :
   
   r=num%2 #stoquer le reste de num//2
   bin=bin+r*f 
   f=f*10 # inverser lordre de l'affichage
   num=num//2 

  print (bin, end=" ")

binaire(10) # on apelle la fontion
 



#exercice 3: 
def somm(n): # on declare une fonction
  y=0
  while(n>0):  # la boucle while s'executre jusqu'a la condition d'arret
     y= y+ somm(n-1) 

  return y #on affiche la somme 




 
#exercice 4:

def fibonacci(n):
  if(n<=1): #fibonnacci de = 1 et fibonnacci de 0 =0
      return n 
  else:
      return(fibonacci(n-1)+fibonacci(n-2)) #la fonction affiche la somme de deux nombre precedents
n=int(input("enter a number n =" )) # lutilisateur choisit le nombred'arret
 
for i in range (n): #i s'incremente jusqu'a i=n-1
 print(fibonacci(i)) #on affihce notre liste 





#ecercice 5:

def chiffre(n):

  if n//10 ==0: #si n//10=0 alors le nombre contient un seul chiffre
    return 1
  else:
     return 1+ chiffre(n/10) #chaque fois que la recursivite ait lieu return s'incremente par 1


n=int(input("enter a number:"))
print(chiffre(n)) #on affiche le nombre des chiffre


#exercice 6:
def tri_bull(tabl):
  n=len(tabl)
  permut=True
  while permut==True: 
    permut=False #une fois dans la boucle while on initialise permut a false
    for i in range(0,n-1): # la boucle parcourit la liste tant que i<n-1
      if tabl[i]>tabl[i+1]: 
        tmp=tabl[i] # on echange les valeurs par une variable tmp dans laquel on stoque tab[i]
        tabl[i]=tabl[i+1] 
        tabl[i+1]=tmp
        permut = True #a la fin on redonne a permut true pourqu'elle puisse entrer dans la boucle while
    n=n-1
my_list=[1,4,3,3,4,5,5,6] # a titre d'exemple on donne cette liste


print("tableau non triee: /n",my_list) #on affiche le tableau avant tri
tri_bull(my_list)
print("le tableau trie a bull: /n",my_list) #on affiche le tableau apres tri 




# tri par selection

def tri_selection(tab):
   for i in range(len(tab)): #on parcours la liste 
    
       min = i
       for j in range(i+1, len(tab)): #on cherche le minimum
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp #on stoque le minimum dans la premiere case de la liste
   return tab
# Programme principale pour tester le code 
tab = [98, 63, 15, 76, 2, 74, 9, 0]
 
tri_selection(tab) #on appelle la fonction
 
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i]) #on affiche la fonction apres tri 
    
    

    #tri par insertion

def tri_insertion(tab): 
    # Parcour  la liste de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : #la boucle while  parcours la liste jusqu'a j=0
                tab[j + 1] = tab[j] 
                j -= 1 # on decremente la valeur de j 
        tab[j + 1] = k
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i])

#exercice 7:

ch=input("entrer un mot :") #l'utilisateur entre une chaine
def invers(ch): #appel de la fonction
  inv=""
  for x in ch : 
    inv = x + inv #on stoque les valeurs de la chaine dans inv et achaque fois le dernier element se pousse vers la vin de inv
  print(inv)
invers(ch) #on appelle la fonction

#exercice 8
ch=input("entrer un mot :")

def occurence(ch):
  i=0

  for x in ch:
    if ch[x] == ch[x+1]:
      i=i+1 #i s'increente chaque fois qu elle trouve l;element choisit se repete
    print(i) 
occurence(ch)
#exercice9

def matrice(x): 
    for i in x: #la boucle for parcours l liste principale x
      l=0
      for j in i: #la boucle parcours la liste secondaire i
        if j==k:
          print("i=",x.index(i),"j=",l)
        l=l+1
x=[[8,10,7],
      [4,7,5],
      [4,5,3]]
k=int(input("saisirla valeur recherchee"))
print(matrice(x)) #on affiche 
