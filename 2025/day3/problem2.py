# --- Part Two ---
# The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.
# Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.
#
# --- Problem Description ---
# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.
# Consider again the example from before:
# - 987654321111111
# - 811111111111119
# - 234234234234278
# - 818181911112111
# Now, the joltages are much larger:
# - In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
# - In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
# - In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
# - In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
# The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.
# What is the new total output joltage?
#
# --- Correct Answer ---
# Your puzzle answer was 171419245422055.

import math

def read_input(file_name):
    battery_banks = []
    with open(file_name, 'r') as file:
        battery_banks = [line.strip() for line in file]
    return battery_banks

def find_max_joltage(battery_bank):
    highest_joltages = [0 for _ in range(12)]

    for i in range(len(battery_bank)):
        joltage = int(battery_bank[i])
        remaining_batteries = len(battery_bank) - i - 1

        for j in range(len(highest_joltages)):
            remaining_highest_joltage_slots = len(highest_joltages) - j - 1

            if remaining_batteries >= remaining_highest_joltage_slots and joltage > highest_joltages[j]:
                highest_joltages[j] = joltage
                highest_joltages[j+1:] = [0] * len(highest_joltages[j+1:])
                break

    return sum([int(joltage * math.pow(10, len(highest_joltages) - j - 1)) for j, joltage in enumerate(highest_joltages)])
    
if __name__ == "__main__":
    battery_banks = read_input('2025/day3/input.txt')

    total = 0
    for i in range(len(battery_banks)):
        total += find_max_joltage(battery_banks[i])

    print(f"Total sum of max joltage values: {total}")