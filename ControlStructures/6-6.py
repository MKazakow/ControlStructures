#The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN
#Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

hours = int(input("Enter the number of hours of parking: "))

if 1 <= hours <= 2:
    print(f"After parking for {hours}h, you need to pay 5PLN")
elif 3 <= hours <= 6:
    print(f"After parking for {hours}h, you need to pay 15PLN")
elif hours > 6:
    print(f"After parking for {hours}h, you need to pay 20PLN")
else:
    print("Wrong input")
