num = int(input("Input number: "))
bin = []
while num != 0:
    bin.insert(0, num % 2)
    num = num // 2
print(bin)