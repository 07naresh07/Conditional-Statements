isFriend = True
isUser = True
print(isFriend and isUser)
print(isFriend or isUser)
if isFriend or isUser:  #OR short circuit: OR statement do not check after OR if first condition turns TRUE
    print("Friends forever")

isGame = False
isMovie = True
if isGame and isMovie:  #AND short circuit: AND statement do not check after AND if first statemtnt turns FALSE, it will terminate and returns FALSE
    print("Lets have fun")