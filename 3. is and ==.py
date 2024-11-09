#== checks value at each position
print(True==1)
print(''==1)    #Empty string represents False
print('1'==1)   #String is not equal to integer
print([]==1)    #Empty list or array is not equal to 1
print([]==[])

# is checks the location in memory
print(True is 1)    #True is not 1 so it gives False
print(True is True) #True is True, so it gives True
print('1' is 1) # '1' is not integer 1, so False
print(1 is 1)   #Data type is integer for both so 1 is 1 and gives True
print([] is []) #Gives False because every time a new list is created, it goes in new location on memory
print([1,2] is [1,2])   #False
