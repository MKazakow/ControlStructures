og_amount = int(input("Enter the amunt in pln: "))
amount = og_amount

fives = og_amount // 5
amount -= fives*5

twos = amount // 2
amount -= twos*2

ones = amount 

print(f"The amount of  pln {og_amount} in coins:")
print(F"5 PLN coins: {fives}")
print(f"2 PLN coins: {twos}")
print(f"1 PLN coins: {ones}")