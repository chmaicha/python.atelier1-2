
#exercice 1:

li=[]
my_list1=[1,2,3,56,24,5]
my_list2=[9,12,34,5,0,5]

count = 0
for i in my_list1:
    if count%2 == 1: #si le reste =1 alors count est impaire
        li.append(i)#on stoquela valeur associe a l'index impaire  de la premiere listedans li
    count += 1
for i in my_list2: #la boucle parcours la deuxieme liste
    if count%2 == 0: #si le reste =0 alors count est paire
        li.append(i)#on stoquela valeur associe a l'index paire de la duxoeme liste dans li
    count += 1
print(li)

#exercice 2:
mylist=[1,2,34,5,5,6,4,3,3]
def invers(myliste):
    x=len(myliste)//3 
    y=x*2
    l1=myliste[:x] #on stoque dans cette liste le premier tiert de la liste entiere
    l2=myliste[x:y] #on stoque dans cette liste le dexieme tiert de la liste entie
    l3=myliste[y:] #on stoque dans cette liste le 3eme tiere de la liste entie
    print(l1[::-1],l2[::-1],l3[::-1]) #on affiche les 3 liste inversement
invers(mylist)
# exrcice 3
list=[23,12,3,4,5,4,32,54,3]
d={}
for i in list:
    if list.count(i)>1 :#condition pour savoir les elements qui se repete plus qu'une fois
       d.update({i:list.count(i)})
       del(i)
    else:
        d.update({i:list.count(i)})
print(d,end= "    ")

#exercice 4:
list1={23,43,5,6,43,23,56,23,69}
list2={34,56,345,23,34,64,64,31}
t=list1.intersection(list2) #on utilise la fonction intersection pour faire l intersection entre les 2 listes
list3=(list1-1) 
print("intersection du deux listes est  ",t)
print("la nouvelle liste est ",list3)
