fi = open("bai4.inp")
fo = open("bai4.out", "w")

def isSNT(n):
    res = True
    if n <= 1:
        res = False
    else:
        for i in range(2,round(n**0.5)+1):
            if n%i ==0:
                res = False
                break
    return res
m,n = map(int, fi.readline().split())
arr = fi.readlines()
maxI = 0
reA = []
for i in range(len(arr)):
    count = 0
    arr[i] = list(map(int,arr[i].strip("\n").split()))
    for j in arr[i]:
        if isSNT(j):
            count += 1
    if maxI < count:
        maxI = count
        reA = []
    if maxI == count:
        reA.append(i+1)
sRes = ''
if count != 0:
    sRes = "\n".join(map(str,reA))
else:
    sRes = "khong"
fo.write(sRes)
fi.close()
fo.close()






