picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for image in picture:
    for pixel in image:
        if pixel==0:
            print(" ", end="")  #By default print() ends with "\n", and to override newline, "" is used
        else:
            print("*", end="")
    print("",end="\n")  #By default print function ends with print(end="\n") and to overcome this \n, we have to use "" to print in same line

