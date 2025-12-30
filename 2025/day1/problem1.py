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
        if rotation[0] == 'L':
            current_position = (current_position - rotation[1]) % 100
        elif rotation[0] == 'R':
            current_position = (current_position + rotation[1]) % 100 

        if current_position == 0:
            password += 1

    return password

if __name__ == "__main__":
    rotations = read_input('2025/day1/input.txt')
    password = calculate_password(rotations)
    print("The password is %d" % password)
