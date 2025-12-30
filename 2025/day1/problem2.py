def read_input(file_name):
    rotations = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            rotations.append((line[0], int(line[1:])))

    return rotations

def calculate_password(rotations):
    current_position = 50
    password = 0

    for rotation in rotations:
        direction = rotation[0]
        steps = rotation[1]
        new_position = current_position

        if direction == 'L':
            new_position = (current_position - steps)
            passes_over_zero = (current_position // 100) - (new_position // 100)

            # Using the floor division operator with negative numbers above forces us to handle some edge cases manually:
            # Special edge case: When you start from zero and go left, you don't count that as passing over zero as it was counted in the previous step
            if current_position == 0:
                passes_over_zero -= 1
            # Special edge case: If you land exactly on zero, that should count as passing over zero
            if new_position % 100 == 0:
                passes_over_zero += 1

            password += passes_over_zero

        elif direction == 'R':
            new_position = (current_position + steps)
            passes_over_zero = (new_position // 100) - (current_position // 100)
            password += passes_over_zero

        current_position = new_position % 100 

    return password

if __name__ == "__main__":
    rotations = read_input('2025/day1/input.txt')
    password = calculate_password(rotations)
    print("The password is %d" % password)
