fi = open("DAYXN.INP")
fo = open("DAYXN.OUT", "w")

x, n = (int(i) for i in fi.read().split())

def congChuSo(n):
    sN = str(n)
    p = 0
    for i in sN:
        p += int(i)**2
    return p

arr = [x]
for i in range(n-1):
    temp = congChuSo(arr[-1])
    arr.append(temp)

res = " ".join(map(str, arr))
fo.write(res)
fi.close()
fo.close()
