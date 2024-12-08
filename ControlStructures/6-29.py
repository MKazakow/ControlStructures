N = int(input("Enter number you want to check if is prime: "))
is_prime = True

for i in range(1, N+1):
    if i != 1 and i != N and N % i == 0:
        is_prime = False

if is_prime: print(f"Number {N} is prime")
else: print(f"Number {N} is not prime")