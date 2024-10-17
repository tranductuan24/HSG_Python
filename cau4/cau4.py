fi = open("KANGAROO.INP")
fo = open("KANGAROO.OUT", "w")

res = False
n, a, b = list(map(int, fi.read().split()))
for i in range(n+1):
    for j in range(n+1):
        if (a*i + b*j == n):
            fo.write(str(i+j))
            res = True
            break
    if res:
        break
fi.close()
fo.close()

