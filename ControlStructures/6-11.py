previous_price = 200
current_price = 100
discount = (previous_price - current_price)/previous_price

if discount >= 0.1:
    print(f"Buy the product! The priced reduced by {discount * 100}%")