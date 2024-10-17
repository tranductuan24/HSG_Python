a = int(input())

def tinh(a):
    s = 0
    for i in range(1,a+1):
        temp = 1/(i*(i+2))
        s += temp
    return s
print(round(tinh(a), 1))
