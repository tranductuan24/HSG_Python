fi = open("TAMGIAC.INP")
fo = open("TAMGIAC.OUT", "w")
a,b,c = map(int, fi.read().split())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
fo.write(str(S))
fi.close()
fo.close()
