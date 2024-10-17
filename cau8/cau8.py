fi = open("KHEPKIN.INP")
fo = open("KHEPKIN.OUT", "w")

N = fi.read()

KK0 = ["1","2","3","5","7"]
KK1 = ["0","4","6","9"]
KK2 = ["8"]
count = 0
for i in N:
    if i in KK0:
        count += 0
    elif i in KK1:
        count += 1
    elif i in KK2:
        count += 2
fo.write(str(count))
fi.close()
fo.close()
