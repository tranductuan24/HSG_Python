fi = open("XAU.INP")
fo = open("XAU.OUT","w")
n = int(fi.readline())
k = int(fi.readline())
sN = str(n)
sN = list(map(int,sN))
le = len(sN)-k
miN =  sN.index(min(sN[:k+1]))
sN = sN[miN:]
while len(sN) != le:
    iMax = sN.index(max(sN))
    sN.pop(iMax)
res = "".join(map(str, sN))
fo.write(res)
fi.close()
fo.close()
