fi = open("THANTHIEN.INP")
fo = open("THANTHIEN.OUT", "w")
a = int(fi.read())
def isSNT(n):
    res = True
    if n <= 1:
        res = False
    else:
        for i in range(2, round(n**0.5)+1):
            if n % i == 0:
                res = False
                break
    return res

def uln(n):
    arr = []
    for i in range(1, (n//2)+1):
        if n % i == 0 and isSNT(i):
            arr.append(i)
    if isSNT(n):
        arr.append(n)
    return max(arr)
i = 2
count = 0
s = ""
while True:
    if uln(a) == uln(i):
        s += str(i) + " "
        count += 1
    if count == 5:
        s = s.strip(" ")
        fo.write(s)
        break
    i +=1
fi.close()
fo.close()
