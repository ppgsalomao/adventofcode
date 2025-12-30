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