#!/usr/bin/env python3

print("Number (base-10) to binary (base-2) converter.")
user_num = int(input("Enter your number: "))

power_value = 0
power_argument = 1
powers = []


def pow_calc(power_multiplier, power_argument=1):
    # Set powers of number and add values to array.

    # Loop and update positional arguments.
    # power_multiplier decrements upon each loop to allow power calculation to occur.
    # power_argument is the resulting calculated power value.
    while power_multiplier > 0:
        power_argument = 2 * power_argument
        power_multiplier -= 1

    # Add power value to array
    if power_argument < user_num:
        powers.append(power_argument)

    return power_argument


# Loop while last set power value is less than users provided number.
power_multiplier = 0
while power_value < int(user_num):
    power_value = pow_calc(
        power_multiplier=power_multiplier)
    power_multiplier += 1

# Loop by subtracting power value from user number. If by subtracting value
# from user number it becomes negative, add 0 digit rather than 1 to binary
# string.
binary_calc = user_num
binary_string = ''
while len(powers) > 0:
    if (binary_calc - powers[-1]) >= 0:
        binary_calc = binary_calc - powers[-1]
        binary_string += "1"
    else:
        binary_string += "0"

    del powers[-1]


print(f"Binary representation: {binary_string}")
