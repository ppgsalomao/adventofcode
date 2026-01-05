# While the solution below is technically correct, it is too inneficient to solve the problem in a reasonable time.
# Upon research, I found that this problem is an Integer Linear Programming problem and is actually at least an NP-Hard problem not easily solvable manually.
# A different implementation using the Z3 Theorem Prover is available in problem2_z3_optimizer.py, although it defeats the purpose of my participation in the Advent of Code challenge.

import re

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
    
def calculate_minimal_button_presses(machine):
    calculated_successful_states = set()

    def does_clicks_reach_target(previous_state, number_of_clicks):
        # Result cached, no need to calculate.
        if ("|".join(map(str, previous_state)), number_of_clicks) in calculated_successful_states:
            return True

        for button in machine['buttons']:
            new_state = previous_state.copy()
            for pos in button:
                new_state[pos] = new_state[pos] + 1
                if new_state[pos] > machine['joltage_requirements'][pos]:
                    return False

            is_one_click_and_reached_target = number_of_clicks == 1 and new_state == machine['joltage_requirements']
            is_more_than_one_click_and_reaches_target = number_of_clicks > 1 and does_clicks_reach_target(new_state, number_of_clicks - 1)
            if is_one_click_and_reached_target or is_more_than_one_click_and_reaches_target:
                calculated_successful_states.add(("|".join(map(str, previous_state)), number_of_clicks))
                return True

        return False
        
    for clicks in range(1, sum(machine['joltage_requirements'])):
        if does_clicks_reach_target([0 for _ in range(len(machine['joltage_requirements']))], clicks):
            return clicks

    return -1  # Not reachable

if __name__ == "__main__":
    machine_data = read_input('2025/day10/input.example.txt')

    total_clicks = 0
    for i, machine in enumerate(machine_data):
        min_clicks = calculate_minimal_button_presses(machine)
        total_clicks += min_clicks
        print(f"Machine {i + 1}: Minimum button presses = {min_clicks}")

    print(f"Total minimum button presses for all machines: {total_clicks}")