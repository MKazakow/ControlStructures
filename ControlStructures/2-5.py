###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))
quarter = 0

if month >= 10:
    quarter = 4
elif 7 <= month < 10:
    quarter = 3
elif 4 <= month < 7:
    quarter = 2
elif 1 <= month < 4:
    quarter = 1
else:
    print("Invalid month") 


print(f'Month {month} is in quarter {quarter}')