fi = open("TACHSO.INP")
fo = open("TACHSO.OUT", "w")
def uc(a,b):
    arr = []
    if a < b:
        a,b = b, a
    for i in range(1,(a//2)+1):
        if a%i ==0 and b%i ==0:
            arr.append(i)
    return (arr)
N = int(fi.read())
count = 0                                                                                                 
for i in range(1, N):
    for j in range(1, N):
        ucl = uc(j, j)
        if ucl != [1]:
            for f in range(len(ucl)):
                if i + j + ucl[f] == N and ucl[f] > 1:
                    count += 1
fo.write(f"{count}")
fi.close()
fo.close()
