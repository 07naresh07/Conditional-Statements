myList = ['a','b','c','b','d','m','n','n']
duplicate = []
for item in myList:
    if myList.count(item)>1 and item not in duplicate:
            duplicate.append(item)
print(duplicate)