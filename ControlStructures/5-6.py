###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0

# Calculate the sum of even numbers

#for i in range(1, N + 1):
#    if i % 2 == 0:
#        sum_even += i
count = 1
while count < N + 1:
    if count % 2 == 0:
        sum_even += count
    count += 1


print(f"The sum of even numbers from 1 to {N} is: {sum_even}")