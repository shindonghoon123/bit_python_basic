a = [2 , 3 , 4 , 5, 10]
b = [4 , 5 , 6 , 7, 8]
set_a = set(a)
set_b = set(b)
c=list(set_a & set_b)
print(c)
c.sort()
print(c[len(c)-1])