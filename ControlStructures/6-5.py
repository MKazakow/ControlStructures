###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature > 35:
    print(f"It is {temperature} degrees Celsius. It is extermely hot")
elif temperature > 30:
    print(f"It is {temperature} degrees Celsius. It is hot")
elif temperature >= 15:
    print(f"It is {temperature} degrees Celsius. It is warm")
elif temperature >= 0:
    print(f"It is {temperature} degrees Celsius. It is cold")
elif temperature < 0:
    print(f"It is {temperature} degrees Celsius. WARNING, FROST.")
else:
    print("Wrong temperature")