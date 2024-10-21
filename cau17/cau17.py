fi = open("BDS.INP")
fo = open("BDS.OUT", "w")
n = int(fi.read())
reA = []
while n > 0:
    re = int(n**0.5)
    reA.append(re)
    n -= re ** 2
reA = " ".join(map(str, reA))
fo.write(reA)
fi.close()
fo.close()
