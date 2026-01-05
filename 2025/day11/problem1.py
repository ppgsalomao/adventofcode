def read_input(filename):
    devices = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            device, outputs = line.split(":")
            outputs = outputs.strip().split()
            devices[device] = outputs
   
    return devices

memory = {}
def count_paths_to_output(devices, origin, target_output):
    if origin in memory:
        return memory[origin]
    
    total_paths = 0
    for output in devices.get(origin, []):
        if output == target_output:
            total_paths += 1
        else:
            total_paths += count_paths_to_output(devices, output, target_output)
    memory[origin] = total_paths

    return total_paths

if __name__ == "__main__":
    devices = read_input('2025/day11/input.txt')

    total_paths = count_paths_to_output(devices, 'you', 'out')
    print(f"Total paths from 'you' to 'out': {total_paths}")