fi = open("bai1.inp")
fo = open("bai1.out", "w")

k = int(fi.read())

s = 0
for i in range(1,k//2):
    s += i
    if s == k:
        fo.write(f"{i}\n{k}")
        break

fi.close()
fo.close()
