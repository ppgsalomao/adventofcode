import json

def read_input(file_name):
    tachyon_manifold = []

    with open(file_name, 'r') as file:
        tachyon_manifold = [line.strip() for line in file]

    return tachyon_manifold

def convert_manifold(tachyon_manifold):
    if len(tachyon_manifold) == 0:
        return []

    converted_manifold = []
    for layer in tachyon_manifold:
        converted_manifold.append([{"space": space, "path_count": 0} for space in layer])

    return converted_manifold

def add_beam_to_position(tachyon_manifold, layer_number, column_number, origin_space_splitted_from=None):
    if layer_number >= len(tachyon_manifold):
        return

    above_space = None
    if layer_number > 0:
        above_space = tachyon_manifold[layer_number - 1][column_number]
    else:
        return

    if origin_space_splitted_from:
        # Splitted beam
        current_space_path_count = tachyon_manifold[layer_number][column_number]["path_count"]
        
        tachyon_manifold[layer_number][column_number]["space"] = '|'
        tachyon_manifold[layer_number][column_number]["path_count"] = current_space_path_count + origin_space_splitted_from["path_count"]

    else:
        # Beam coming straight down
        current_space_path_count = tachyon_manifold[layer_number][column_number]["path_count"]

        tachyon_manifold[layer_number][column_number]["space"] = '|'
        tachyon_manifold[layer_number][column_number]["path_count"] = current_space_path_count + above_space["path_count"]
        if above_space["space"] == 'S':
            tachyon_manifold[layer_number][column_number]["path_count"] += 1

def run_beam_to_empty_spaces(tachyon_manifold, layer_number):
    if layer_number >= len(tachyon_manifold):
        return
    
    for column in range(len(tachyon_manifold[layer_number])):
        is_free_space = tachyon_manifold[layer_number][column]["space"] == '.'
        has_beam_above = layer_number > 0 and (tachyon_manifold[layer_number - 1][column]["space"] == '|')
        is_starter_position_above = layer_number > 0 and (tachyon_manifold[layer_number - 1][column]["space"] == 'S')

        if is_free_space and (has_beam_above or is_starter_position_above):
            add_beam_to_position(tachyon_manifold, layer_number, column)

def split_beam(tachyon_manifold, layer_number):
    if layer_number >= len(tachyon_manifold):
        return 0
    
    for column in range(len(tachyon_manifold[layer_number])):
        has_beam_above = layer_number > 0 and (tachyon_manifold[layer_number - 1][column]["space"] == '|')
        is_beam_splitter = tachyon_manifold[layer_number][column]["space"] == '^'

        if has_beam_above and is_beam_splitter:
            add_beam_to_position(tachyon_manifold, layer_number, column - 1, tachyon_manifold[layer_number - 1][column])
            add_beam_to_position(tachyon_manifold, layer_number, column + 1, tachyon_manifold[layer_number - 1][column])

def run_beam_through_manifold(tachyon_manifold):
    for layer_number in range(len(tachyon_manifold)):
        run_beam_to_empty_spaces(tachyon_manifold, layer_number)
        split_beam(tachyon_manifold, layer_number)

if __name__ == "__main__":
    tachyon_manifold = read_input('2025/day7/input.txt')
 
    converted_manifold = convert_manifold(tachyon_manifold)
    run_beam_through_manifold(converted_manifold)

    total_path_count = sum([space["path_count"] for space in converted_manifold[-1]])
    print(f"Total path count: {total_path_count}")
   