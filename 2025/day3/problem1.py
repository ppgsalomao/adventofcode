def read_input(file_name):
    battery_banks = []
    with open(file_name, 'r') as file:
        battery_banks = [line.strip() for line in file]
    return battery_banks

def find_max_joltage(battery_bank):
    highest_joltage_1 = 0
    highest_joltage_2 = 0

    for i in range(len(battery_bank)):
        joltage = int(battery_bank[i])

        if i < len(battery_bank) - 1 and joltage > highest_joltage_1:
                highest_joltage_1 = joltage
                highest_joltage_2 = 0

        elif joltage > highest_joltage_2:
            highest_joltage_2 = joltage

    return highest_joltage_1 * 10 + highest_joltage_2

if __name__ == "__main__":
    battery_banks = read_input('2025/day3/input.txt')
    sum = 0
    for i in range(len(battery_banks)):
        sum += find_max_joltage(battery_banks[i])

    print(f"Total sum of max joltage values: {sum}")