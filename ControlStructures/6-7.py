#Write a program that asks the user for their age and then checks which age group they belong to:

#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

age = int(input("Input age: "))

if 0 <= age < 13:
    print(f"{age}, CHILD")
elif 13 <= age <= 19:
    print(f"{age}, TEEN")
elif 20 <= age <= 64:
    print(f"{age}, ADULT")
elif age > 64:
    print(f"{age}, SENIOR")