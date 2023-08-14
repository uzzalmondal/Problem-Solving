#list is 1 of python data type.
#List is accesable, ordered, indexable 
#Index Start from 0 
#List item can add, remove, clear
#List item can be varient by item data type
#List item can be duplicate value

#list

listitem  = ['Ram', 'Uzzal', 'Gargi', 2023 ]
print(listitem)
print(listitem[0]) #Ram
print(listitem[-1]) #2023
print(listitem[-0]) #Ram

#Add Item (append method)
listitem.append('Sarmistha')
print(listitem)

#remove Item
listitem.remove('Ram')
print(listitem)

#len count
print(len(listitem))

for x in listitem:
   print(x)

for i in range(len(listitem)):
   print(listitem[i])

#short hand for loop to access list item
[print(x) for x in listitem]