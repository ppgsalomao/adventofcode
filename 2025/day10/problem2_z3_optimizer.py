import re
import z3

def read_input(filename):
    machine_data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            match = re.match(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$", line.strip())
            _, buttons, joltage_requirements = match.groups()
            buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split()]
            joltage_requirements = list(map(int, joltage_requirements.split(",")))

            machine_data.append({
                'buttons': buttons,
                'joltage_requirements': joltage_requirements
            })
   
    return machine_data

total = 0

def calculate_minimal_button_presses(machine):

    o = z3.Optimize()

    # Add the different variables that will form the equations to optimize.
    vars = z3.Ints(f"n{i}" for i in range(len(machine['buttons'])))

    # Create the base constraints (non-negative variables), as they represent button presses.
    for var in vars: o.add(var >= 0)

    # Build the equations based on the machine's joltage requirements.
    for i, joltage in enumerate(machine['joltage_requirements']):
        equation = 0
        for b, button in enumerate(machine['buttons']):
            if i in button:
                equation += vars[b]
        o.add(equation == joltage)

    # Add the optimization goal (minimize total button presses).
    o.minimize(sum(vars))

    # Solve the optimization problem and find the result.
    o.check()
    return o.model().eval(sum(vars)).as_long()

if __name__ == "__main__":
    machine_data = read_input('2025/day10/input.txt')

    total_clicks = 0
    for i, machine in enumerate(machine_data):
        min_clicks = calculate_minimal_button_presses(machine)
        total_clicks += min_clicks
        print(f"Machine {i + 1}: Minimum button presses = {min_clicks}")

    print(f"Total minimum button presses for all machines: {total_clicks}")