#!/usr/bin/env python3

print("Decimal (base-10) to binary (base-2) converter.")
user_num = int(input("Enter your number: "))

power_value = 0
powers = []


def pow_calc(power_multiplier):
    # Set powers of number and add values to array.

    # ans is the resulting calculated power value.
    ans = 2**power_multiplier

    # Add power value to array
    if ans < user_num:
        powers.append(ans)

    return ans


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
