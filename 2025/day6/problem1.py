def read_input(file_name):
    problems = {}

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            line_items = [x for x in line.split() if x]

            if len(line_items) == 0:
                continue

            
            if line_items[0] == "+" or line_items[0] == "*":
                for i in range(len(line_items)):
                    problems.setdefault(i, {"operands": [], "operator": None})["operator"] = line_items[i]
                break

            else:
                for i in range(len(line_items)):
                    problems.setdefault(i, {"operands": [], "operator": None})["operands"].append(int(line_items[i]))

    return problems

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

        print(f"Problem {index + 1}: {operator} of {operands} = {result}")

    print(f"Total of all problems: {problems_total}")