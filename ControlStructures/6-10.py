age_in_human = int(input("Enter dogs age in human years: "))
age_in_dog = 0

for i in range(age_in_human):
    if i <=1:
        age_in_dog += 10.5
    else:
        age_in_dog += 4

print(f"Age of dog in human years: {age_in_human}, and in dog years: {age_in_dog}")