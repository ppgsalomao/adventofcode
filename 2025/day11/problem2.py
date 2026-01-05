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
    if (origin, target_output) in memory:
        return memory[(origin, target_output)]
    
    total_paths = 0
    for output in devices.get(origin, []):
        if output == target_output:
            total_paths += 1
        else:
            total_paths += count_paths_to_output(devices, output, target_output)
    memory[(origin, target_output)] = total_paths

    return total_paths

if __name__ == "__main__":
    devices = read_input('2025/day11/input.txt')

    total_paths = ( \
        count_paths_to_output(devices, 'svr', 'dac') * \
        count_paths_to_output(devices, 'dac', 'fft') * \
        count_paths_to_output(devices, 'fft', 'out') \
    ) + ( \
        count_paths_to_output(devices, 'svr', 'fft') * \
        count_paths_to_output(devices, 'fft', 'dac') * \
        count_paths_to_output(devices, 'dac', 'out') 
    )

    print(f"Total paths from 'svr' to 'out': {total_paths}")