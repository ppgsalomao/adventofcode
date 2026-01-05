import re

def read_input(filename):
    machine_data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            match = re.match(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$", line.strip())
            target, buttons, _ = match.groups()
            buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split()]

            machine_data.append({
                'target': target,
                'buttons': buttons
            })
   
    return machine_data
    
def calculate_minimal_button_presses(machine):
    calculated_successful_states = set()

    def does_clicks_reach_target(previous_state, number_of_clicks):
        # Result cached, no need to calculate.
        if (previous_state, number_of_clicks) in calculated_successful_states:
            return True

        for button in machine['buttons']:
            new_state = previous_state
            for pos in button:
                new_state = new_state[:pos] + ('#' if new_state[pos] == '.' else '.') + new_state[pos + 1:]

            is_one_click_and_reached_target = number_of_clicks == 1 and new_state == machine['target']
            is_more_than_one_click_and_reaches_target = number_of_clicks > 1 and does_clicks_reach_target(new_state, number_of_clicks - 1)
            if is_one_click_and_reached_target or is_more_than_one_click_and_reaches_target:
                calculated_successful_states.add((previous_state, number_of_clicks))
                return True

        return False
        
    for clicks in range(1, len(machine['buttons']) + 1):
        if does_clicks_reach_target("." * len(machine['target']), clicks):
            return clicks

    return -1  # Not reachable

if __name__ == "__main__":
    machine_data = read_input('2025/day10/input.txt')

    total_clicks = 0
    for i, machine in enumerate(machine_data):
        min_clicks = calculate_minimal_button_presses(machine)
        total_clicks += min_clicks
        print(f"Machine {i + 1}: Minimum button presses = {min_clicks}")

    print(f"Total minimum button presses for all machines: {total_clicks}")