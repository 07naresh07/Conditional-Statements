myList = ['a','b','c','b','d','m','n','n']
duplicate = []
for i, item in enumerate(myList):
    if item in myList[i+1:]:    #This will check if first taken item i.e. 'a' is in myList[i+1:] i.e. from ['b'..'n']
        duplicate.append(item)
print(duplicate)