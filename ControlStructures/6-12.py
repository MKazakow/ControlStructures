amount = int(input("Enter the number of purchased products: "))
price = int(input("Enter price for the product:  "))
total = 0

counter = 1
while counter <= amount:
    if counter <= 2:
        total += price
    else:
        total += (0.75*price)
    counter += 1

print(f"nr of purchased products: {amount}")
print(f"nprice for product: {price}")
print(f"total price for all products: {total}")