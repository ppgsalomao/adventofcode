def read_input(filename):
    present_shapes = {}
    regions = []
    with open(filename, 'r') as f:
        whole_file = f.read()
        file_sections = whole_file.strip().split("\n\n")

        for i in range(len(file_sections) - 1):
            shape = file_sections[i].splitlines()
            present_shapes[int(shape[0][:-1])] = [shape[i] for i in range(1, 4)]

        regions_section = file_sections[-1].splitlines()
        for region in regions_section:
            region_parts = region.split(":")
            region_width, region_height = map(int, region_parts[0].split("x"))
            present_shape_quantities = list(map(int, region_parts[1].strip().split()))
            regions.append((region_width, region_height, present_shape_quantities))

    return present_shapes, regions

if __name__ == "__main__":
    _, regions = read_input('2025/day12/input.txt')

    total_regions_that_fit = 0
    for region in regions:
        region_width, region_height, present_shape_quantities = region

        # Try to fit the presents side by side without rotations or overlaps.
        if ((region_width // 3) * (region_height // 3)) >= sum(present_shape_quantities):
            total_regions_that_fit += 1

    print(f"Total regions that can fit all presents: {total_regions_that_fit}")
