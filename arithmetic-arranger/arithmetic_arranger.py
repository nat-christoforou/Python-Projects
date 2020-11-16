"""An Arithmetic Arranger."""


def operators_and_operands(problems):
    """Find the operands and the operators of the problems."""
    first_operands = []
    second_operands = []
    operators = []

    for problem in problems:
        elements = problem.split()
        first_operands.append(elements[0])
        operators.append(elements[1])
        second_operands.append(elements[2])

    return first_operands, operators, second_operands


def calculate_answer(first_operands, operators, second_operands):
    """Find the solution of the problems."""
    solutions = []
    for elem in enumerate(operators):
        if operators[elem[0]] == '+':
            solutions.append(str(int(first_operands[elem[0]]) + int(second_operands[elem[0]])))
        elif operators[elem[0]] == '-':
            solutions.append(str(int(first_operands[elem[0]]) - int(second_operands[elem[0]])))
    return solutions


def arrange_first_operands(first_operands, number_of_dashes):
    """Arrange first operands in one line."""
    arranged_first_operands = ""
    for i, _ in enumerate(first_operands):
        if i < len(first_operands) - 1:
            arranged_first_operands += first_operands[i].rjust(number_of_dashes[i]) + '    '
        else:
            arranged_first_operands += first_operands[i].rjust(number_of_dashes[i]) + '\n'
    return arranged_first_operands


def arrange_second_operands(second_operands, operators, lengths_of_longest_numbers):
    """Arrange operators and second operands."""
    arranged_second_operands = ""
    for i, _ in enumerate(second_operands):
        if i < len(second_operands) - 1:
            arranged_second_operands += operators[i] + ' ' + second_operands[i].rjust(
                lengths_of_longest_numbers[i]) + '    '
        else:
            arranged_second_operands += operators[i] + ' ' + second_operands[i].rjust(
                lengths_of_longest_numbers[i]) + '\n'
    return arranged_second_operands


def arrange_dashes(number_of_dashes):
    """Arrange dashes."""
    dashes = ""
    for i, _ in enumerate(number_of_dashes):
        if i < len(number_of_dashes) - 1:
            dashes += '-' * number_of_dashes[i] + '    '
        else:
            dashes += '-' * number_of_dashes[i]
    return dashes


def arrange_solution(solutions, number_of_dashes):
    """Arrange solutions if answer is True."""
    arranged_solutions = "\n"
    for i, _ in enumerate(solutions):
        if i < len(solutions) - 1:
            arranged_solutions += solutions[i].rjust(number_of_dashes[i]) + '    '
        else:
            arranged_solutions += solutions[i].rjust(number_of_dashes[i])
    return arranged_solutions


def arithmetic_arranger(problems, answer=False):
    """Arrange the problems vertically and side-by-side."""
    first_operands, operators, second_operands = operators_and_operands(problems)

    if len(operators) > 5:
        return "Error: Too many problems."

    if not all(i in ['+', '-'] for i in operators):
        return "Error: Operator must be '+' or '-'."

    if not all(i.isdigit() for i in first_operands) or \
            not all(i.isdigit() for i in second_operands):
        return "Error: Numbers must only contain digits."

    if not all(len(i) <= 4 for i in first_operands) or \
            not all(len(i) <= 4 for i in second_operands):
        return "Error: Numbers cannot be more than four digits."

    if answer:
        solutions = calculate_answer(first_operands,
                                     operators, second_operands)

    lengths_of_longest_numbers = []
    number_of_dashes = []

    for i in range(len(problems)):
        if answer:
            lengths_of_longest_numbers.append(
                max(len(first_operands[i]), len(second_operands[i]),
                    len(str(abs(int(solutions[i]))))))
        else:
            lengths_of_longest_numbers.append(max(len(first_operands[i]),
                                                  len(second_operands[i])))
        number_of_dashes.append(lengths_of_longest_numbers[i] + 2)

    arranged_first_operands = arrange_first_operands(first_operands, number_of_dashes)
    arranged_second_operands = arrange_second_operands(second_operands, operators,
                                                       lengths_of_longest_numbers)
    dashes = arrange_dashes(number_of_dashes)

    # arrange solutions if answer is True
    if answer:
        arranged_solutions = arrange_solution(solutions, number_of_dashes)
        arranged_problems = arranged_first_operands + arranged_second_operands + \
                            dashes + arranged_solutions
    else:
        arranged_problems = arranged_first_operands + arranged_second_operands + dashes

    return arranged_problems
