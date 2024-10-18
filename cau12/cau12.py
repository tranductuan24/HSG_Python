fi = open("bai3.inp")
fo = open("bai3.out", "w")

n = int(fi.readline())
a = list(map(int,fi.readline().split()))
reA = []
msumA = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in range(1,len(a)):
    if abs(sum(a[i:]) - sum(a[:i])) < msumA:
        reA = []
        msumA = abs(sum(a[i:]) - sum(a[:i]))
    if abs(sum(a[i:]) - sum(a[:i])) == msumA:
        reA.append([a[:i], a[i:]])
sRes = ""
for i in reA:
    for j in i:
        x = " ".join(map(str, j))
        sRes += (f"{x}\n")
sRes = sRes.strip("\n")
fo.write(sRes)
fi.close()
fo.close()
