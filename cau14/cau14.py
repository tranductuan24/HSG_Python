fi = open("DAYTANG.INP")
fo = open("DAYTANG.OUT", "w")
n = int(fi.readline())
C = list(map(int, fi.readline().split()))

res = ""
temp = []
ma = -1
for i in range(len(C)-1):
    if C[i] < C[i+1]:
        temp.append(C[i])
    else:
        temp.append(C[i])
        if ma <= len(temp):
            ma = len(temp)
            res = " ".join(map(str, temp))
        temp = []
res = f"{ma}\n{res}"
fo.write(res)

fi.close()
fo.close()
