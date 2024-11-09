user = {
    "Name":["Naresh", "Uma"],
    "Age":[29,28]
}
for i in user:
    print(i)    #This gives keys only
#If we want to iterate over values:
for j in user.values():
    print(j)

#OR items() can be used but it gives dictionary values in tuples form
for k in user.items():
    print(k)

#Iterating over keys:
for l in user.keys():
    print(l)