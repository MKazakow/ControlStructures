n = 20
n1 = 0
n2 = 1

of = 0
print(n1)
count = 1
while count <= n:
    print(n2)
    of = n1 + n2
    n1 = n2
    n2 = of
    count += 1