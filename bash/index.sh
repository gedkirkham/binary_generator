#!/bin/bash

echo "Number (base-10) to binary (base-2) converter."
read -p "Enter your number: " user_num

powers=()
power_value=0

# Set powers of number and add values to array.
pow() {
    # Add positional argument $3.
    set $1 $2 1

    # Loop and update positional arguments.
    # $1 remains constant - 2.
    # $2 decrements upon each loop to allow power calculation to occur.
    # $3 is the resulting calculated power value.
    while [ $2 -gt 0 ]; do
        set $1 $(($2 - 1)) $(($1 * $3))
    done

    power_value=$3

    # Add power value to array.
    if [ $power_value -le $user_num ]; then
        powers+=($3)
    fi
}

# Loop while last set power value is less than users provided number.
power_multiplier=0
while [ $power_value -lt $user_num ]; do
    pow 2 $power_multiplier
    power_multiplier=$((power_multiplier + 1))
done

# Loop by subtracting power value from user number. If by subtracting value
# from user number it becomes negative, add 0 digit rather than 1 to binary 
# string.
binary_calc=$user_num
binary_string=''
while [ ${#powers[@]} -gt 0 ]; do
    last_index=$((${#powers[@]} - 1))

    if [ $((binary_calc - ${powers[last_index]})) -ge 0 ]; then
        binary_calc=$((binary_calc - ${powers[last_index]}))
        binary_string+=1
    else
        binary_string+=0
    fi

    unset powers[last_index]
done

echo Binary representation: $binary_string
