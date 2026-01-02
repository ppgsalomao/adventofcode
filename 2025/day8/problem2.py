from math import sqrt

def read_input(file_name):
    junction_box_locations = []

    with open(file_name, 'r') as file:
        for line in file:
            line_coordinates = line.strip().split(',')
            junction_box_locations.append((int(line_coordinates[0]), int(line_coordinates[1]), int(line_coordinates[2])))

    return junction_box_locations

def straight_line_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def calculate_all_distances(junction_box_locations):
    distances = []
    for i, box1 in enumerate(junction_box_locations):
        for j, box2 in enumerate(junction_box_locations):
            if i < j: # Avoid calculating distance twice
                distances.append((straight_line_distance(box1, box2), box1, box2))

    return distances

def find_root(circuits, box):
    if circuits[box]["root"] != box:
        circuits[box]["root"] = find_root(circuits, circuits[box]["root"])
    return circuits[box]["root"]
    
def connect_circuits(circuits, box1, box2):
    box1_root = find_root(circuits, box1)
    box2_root = find_root(circuits, box2)

    if box1_root != box2_root:
        # Connect the smaller circuit to larger
        if circuits[box1_root]["size"] < circuits[box2_root]["size"]:
            circuits[box1_root]["root"] = box2_root
            circuits[box2_root]["size"] += circuits[box1_root]["size"]
        else:
            circuits[box2_root]["root"] = box1_root
            circuits[box1_root]["size"] += circuits[box2_root]["size"]
        return True
    return False

def assemble_network(junction_box_locations):
    distances = calculate_all_distances(junction_box_locations)
    distances.sort() # Getting shortest distances first

    circuits = { box : { "root": box, "size": 1 } for box in junction_box_locations }

    # Make connections
    last_connection = (None, None)
    for _, box1, box2 in distances:
        connection_made = connect_circuits(circuits, box1, box2)
        if connection_made:
            last_connection = (box1, box2)
    
    return circuits, last_connection

if __name__ == "__main__":
    junction_box_locations = read_input('2025/day8/input.txt')
    network, last_connection = assemble_network(junction_box_locations)

    print(f"Last connection made between boxes at locations: {last_connection}, resulting in distance: {last_connection[0][0] * last_connection[1][0]}")