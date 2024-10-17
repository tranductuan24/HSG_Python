#D = Vao
#W = Ra

n = int(input())
arr = []
for i in range(n):
    t = input()
    arr.append(t)
su = 0
for i in arr:
    if i[0] == "D":
        i = "+"+i[2:]
    elif i[0] == "W":
        i = "-"+i[2:]
    su += int(i)
print(su)
