car_speed = int(input("Enter speed: "))
speed_limit_min = 40
speed_limit_max = 140

if not speed_limit_min <= car_speed <= speed_limit_max:
    print(f"Warning! Invalid car speed! ({car_speed})")