mk = [x for x in input().split(",")]

az = [chr(x) for x in range(ord("a"), ord("z") + 1)]
AZ = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
O9 = [chr(x) for x in range(ord("0"), ord("9") + 1)]
sym = ['$','#','@']
for i in mk:
    isaz = False
    isAZ = False
    isO9 = False
    isSym = False
    if 6<= len(i) <= 12:
        for j in i:
            if j in az:
                isaz = True
            elif j in AZ:
                isAZ = True
            elif j in O9:
                isO9 = True
            elif j in sym:
                isSym = True
    if isaz and isAZ and isO9 and isSym:
        print(i)
