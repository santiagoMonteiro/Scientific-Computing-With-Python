def arithmetic_arranger(problems, show_answers=False):
    end_arrange = []

    if len(problems) > 5:
        print("Error: Too many problems.")
        return

    for p in problems:
        if "+" in p:
            operator = "+"
        elif "-" in p:
            operator = "-"
        else:
            print("Error: Operator must be '+' or '-'.")
            return

        operands = [o.strip() for o in p.split(operator)]

        char_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for o in operands:
            if len(o) > 4:
                print("Error: Numbers cannot be more than four digits.")
                return
            for char in o:
                if char not in char_numbers:
                    print("Error: Numbers must only contain digits.")
                    return

        end_arrange.append(
            [
                operands[0],
                operands[1],
                (
                    int(operands[0]) + int(operands[1])
                    if operator == "+"
                    else int(operands[0]) - int(operands[1])
                ),
                operator,
                len(operands[0]),
                len(operands[1]),
            ]
        )

    print(end_arrange)

    ceil = f""
    floor = f""
    dashes = f""
    result = f""

    for i in range(len(end_arrange)):
        ceil_spaces = ""
        floor_spaces = ""
        difference = abs(end_arrange[i][4] - end_arrange[i][5])

        if end_arrange[i][4] > end_arrange[i][5]:
            floor_spaces += difference * " "
        elif end_arrange[i][4] < end_arrange[i][5]:
            ceil_spaces += difference * " "

        if i == 0:
            ceil += ceil_spaces + (2) * " " + end_arrange[i][0]
        else:
            ceil += ceil_spaces + (4 + 2) * " " + end_arrange[i][0]

    print(ceil)

    # return problems


# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
