def arithmetic_arranger(problems, show_answers=False):
    end_arrange = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for p in problems:
        if "+" in p:
            operator = "+"
        elif "-" in p:
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        operands = [o.strip() for o in p.split(operator)]

        char_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for o in operands:
            if len(o) > 4:
                return "Error: Numbers cannot be more than four digits."
            for char in o:
                if char not in char_numbers:
                    return "Error: Numbers must only contain digits."

        end_arrange.append(
            [
                operands[0],
                operands[1],
                (
                    str(int(operands[0]) + int(operands[1]))
                    if operator == "+"
                    else str(int(operands[0]) - int(operands[1]))
                ),
                operator,
                len(operands[0]),
                len(operands[1]),
            ]
        )

    ceil = f""
    floor = f""
    dashes = f""
    result = f""

    for i in range(len(end_arrange)):
        ceil_spaces = ""
        floor_spaces = ""
        difference = abs(end_arrange[i][4] - end_arrange[i][5])
        dash = ""

        if end_arrange[i][4] > end_arrange[i][5]:
            floor_spaces += difference * " "
            dash += (2 + end_arrange[i][4]) * "-"
        elif end_arrange[i][4] < end_arrange[i][5]:
            ceil_spaces += difference * " "
            dash = (2 + end_arrange[i][5]) * "-"
        else:
            dash = (2 + end_arrange[i][5]) * "-"

        if i == 0:
            ceil += ceil_spaces + (2) * " " + end_arrange[i][0]
            floor += end_arrange[i][3] + " " + floor_spaces + end_arrange[i][1]
            dashes += dash
            result += (len(dash) - len(end_arrange[i][2])) * " " + end_arrange[i][2]
        else:
            ceil += ceil_spaces + (4 + 2) * " " + end_arrange[i][0]
            floor += 4 * " " + end_arrange[i][3] + " " + floor_spaces + end_arrange[i][1]
            dashes += 4 * " " + dash
            result += 4 * " " + (len(dash) - len(end_arrange[i][2])) * " " + end_arrange[i][2]
        

    

    if show_answers:
        return f"{ceil}\n{floor}\n{dashes}\n{result}"
    else:
        return f"{ceil}\n{floor}\n{dashes}"

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))