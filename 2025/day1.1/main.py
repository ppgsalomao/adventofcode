with open('2025/day1.1/input.txt', 'r') as file:
    current_position = 50
    password = 0

    rotations = [line.strip() for line in file]

    for rotation in rotations:
        steps = int(rotation[1:])

        if rotation.startswith('L'):
            current_position = (current_position - steps) % 100
        elif rotation.startswith('R'):
            current_position = (current_position + steps) % 100 
    
        if current_position == 0:
            password += 1

    print("The password is %d" % password)