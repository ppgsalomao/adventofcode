def read_input(file_name):
    tachyon_manifold = []

    with open(file_name, 'r') as file:
        tachyon_manifold = [line.strip() for line in file]

    return tachyon_manifold

def add_beam_to_position(tachyon_manifold, layer_number, column_number):
    if layer_number >= len(tachyon_manifold):
        return
    tachyon_manifold[layer_number] = tachyon_manifold[layer_number][:column_number] + '|' + tachyon_manifold[layer_number][column_number+1:]

def run_bean_to_empty_spaces(tachyon_manifold, layer_number):
    if layer_number >= len(tachyon_manifold):
        return
    
    for column in range(len(tachyon_manifold[layer_number])):
        is_free_space = tachyon_manifold[layer_number][column] == '.'
        has_beam_above = layer_number > 0 and (tachyon_manifold[layer_number - 1][column] == '|')
        is_starter_position_above = layer_number > 0 and (tachyon_manifold[layer_number - 1][column] == 'S')

        if is_free_space and (has_beam_above or is_starter_position_above):
            add_beam_to_position(tachyon_manifold, layer_number, column)

def split_bean(tachyon_manifold, layer_number):
    if layer_number >= len(tachyon_manifold):
        return 0
    
    beam_split_count = 0
    for column in range(len(tachyon_manifold[layer_number])):
        has_beam_above = layer_number > 0 and (tachyon_manifold[layer_number - 1][column] == '|')
        is_beam_splitter = tachyon_manifold[layer_number][column] == '^'
        is_previous_space_empty = column - 1 >= 0 and tachyon_manifold[layer_number][column - 1] == '.'
        is_next_space_empty = column + 1 < len(tachyon_manifold[layer_number]) and tachyon_manifold[layer_number][column + 1] == '.'

        if has_beam_above and is_beam_splitter:
            if is_previous_space_empty:
                add_beam_to_position(tachyon_manifold, layer_number, column - 1)
            if is_next_space_empty:
                add_beam_to_position(tachyon_manifold, layer_number, column + 1)
            beam_split_count += 1
    
    tachyon_manifold[layer_number] = tachyon_manifold[layer_number].replace('/', '|')

    return beam_split_count

def run_bean_through_manifold(tachyon_manifold):

    beam_split_count = 0

    for layer_number in range(len(tachyon_manifold)):
        print(f"Before layer {layer_number}:\n" + "\n".join(tachyon_manifold[layer_number-2:layer_number+1]) + "\n")

        run_bean_to_empty_spaces(tachyon_manifold, layer_number)
        split_count_in_layer = split_bean(tachyon_manifold, layer_number)
        beam_split_count += split_count_in_layer

        print(f"After layer {layer_number}:\n" + "\n".join(tachyon_manifold[layer_number-2:layer_number+1]) + "\n")
        print(f" - Split Count in Layer: {split_count_in_layer}\n")

    return beam_split_count

if __name__ == "__main__":
    tachyon_manifold = read_input('2025/day7/input.txt')

    beam_split_count = run_bean_through_manifold(tachyon_manifold)

    print(f"Total beam splits: {beam_split_count}")