fi = open("XEPHANG.INP")
fo = open("XEPHANG.OUT", "w")

n = int(fi.readline())
a = list(map(int, fi.readline().split()))
subA = list(set(a))

arrMa = []
ma = 0
for i in subA:
    if ma < a.count(i):
        ma = a.count(i)
        arrMa = [a.count(i), i]
fo.write(" ".join(map(str, arrMa)))
fi.close()
fo.close()
