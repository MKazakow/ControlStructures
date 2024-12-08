enter_time = input("Enter time :  (hh:mm)")
time_other = ""

if int(enter_time[0:2]) > 12:
    time_other = str(int(enter_time[0:2])-12) + enter_time[2:] + "pm"
else:
    time_other = enter_time + "am"

print(time_other)