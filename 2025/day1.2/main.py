def calculate_password(file_path):
    with open(file_path, 'r') as file:
        current_position = 50
        password = 0

        rotations = [line.strip() for line in file]

        for rotation in rotations:
            steps = int(rotation[1:])
            new_position = current_position

            if rotation.startswith('L'):
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

            elif rotation.startswith('R'):
                new_position = (current_position + steps)
                passes_over_zero = (new_position // 100) - (current_position // 100)
                password += passes_over_zero

            current_position = new_position % 100 

        print("The password is %d" % password)

if __name__ == "__main__":
    calculate_password('2025/day1.2/input.example.txt')
    calculate_password('2025/day1.2/input.txt')