def read_input(file_name):
    problems = {}

    operand_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            line_items = [x for x in line.strip().split() if x]

            if len(line_items) == 0:
                continue
            
            if line_items[0] == "+" or line_items[0] == "*":
                for i in range(len(line_items)):
                    problems.setdefault(i, {"operands": [], "operator": None, "longest_operand_length": 0})["operator"] = line_items[i]
                break

            else:
                operand_lines.append(line.rstrip('\n'))
                for i in range(len(line_items)):
                    problems.setdefault(i, {"operands": [], "operator": None, "longest_operand_length": 0})
                    if len(line_items[i]) > problems.get(i)["longest_operand_length"]:
                        problems.get(i)["longest_operand_length"] = len(line_items[i])

    offset = 0
    for problem in problems.values():
        longest_length = problem["longest_operand_length"]

        for line in operand_lines:
            problem["operands"].append(line[offset:offset + longest_length])

        problem["operands"] = convert_operands(problem["operands"])

        offset += longest_length + 1 # +1 for the space

    return problems

def convert_operands(operands):
    if len(operands) == 0:
        return operands

    new_operands = { column: 0 for column in range(len(operands[0])) }
    for operand in operands:
        for i in range(len(operand)):
            if operand[i] != ' ':
                new_operands[i] = new_operands[i] * 10 + int(operand[i:i+1])

    return new_operands.values()

if __name__ == "__main__":
    problems = read_input('2025/day6/input.txt')

    problems_total = 0
    for index in range(len(problems)):
        problem = problems[index]
        operator = problem["operator"]
        operands = problem["operands"]

        result = None
        if operator == "+":
            result = sum(operands)
        elif operator == "*":
            result = 1
            for operand in operands:
                result *= operand

        problems_total += result

    print(f"Total of all problems: {problems_total}")