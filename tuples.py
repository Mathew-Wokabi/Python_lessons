#tuples
fruits=("banana","mangoes","oranges")
print(fruits)
#if i want to modify tuple
#convert to list
#make your changes
#revert to tuple



#how to change from tuple to list
myfruitslist=list(fruits) #converting to list
print(myfruitslist)
myfruitslist[2]="pineapples" #modification
print(myfruitslist)
fruits=tuple(myfruitslist)  #converting back to tuple
print(fruits)





