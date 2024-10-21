fi = open("TACKE.INP")
fo = open("TACKE.OUT","w")
arr = []
x,y,z = map(int, fi.read().split())
#x,y,z = 6,2,2
if x > 0:
    if y == z:
        for i in range(y):
            y -= 1
            z-=1
            x+=2
            arr.append([x,y,z])
    else:
        while True:
            y -= 1
            z -= 1
            x += 2
            arr.append([x, y, z])
            if z == 0:
                if x > 0 and y > 0:
                    x -= 1
                    y -= 1
                    z += 2
                    arr.append([x, y, z])
                else:
                    break
            elif y == 0:
                if x > 0 and y > 0:
                    x -= 1
                    z -= 1
                    y += 2
                else:
                    break
            if x == y:
                z -= 1
                y -= 1
                x += 2
else:
    if y == z:
        for i in range(y):
            y -= 1
            z-=1
            x+=2
            arr.append([x,y,z])
    else:
        while True:
            if x > 0 and y > 0:
                x -= 1
                y -= 1
                z += 2
                arr.append([x, y, z])
            else:
                break
            if x > 0 and y > 0:
                x -= 1
                z -= 1
                y += 2
            else:
                break
            if x == y:
                z -= 1
                y -= 1
                x += 2
if arr == [] or arr[-1][1] != arr[-1][2]:
    fo.write("KHONG")
else:
    r = ""
    for i in arr:
        s = " ".join(map(str, i))
        r += s +"\n"
    r = r.strip("\n")
    fo.write(r)
fi.close()
fo.close()
