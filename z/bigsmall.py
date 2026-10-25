big = 0
small = 0

for i in range(5):
    x = (input("Chose Big or Small BY B/S:  "))
    if(x == 'B'):
        big += 1
    elif(x == 'S'):
        small += 1
    else:
        print("invalid")

if(small < big):
    print("small wins")
else:
    print("big wins")
    #