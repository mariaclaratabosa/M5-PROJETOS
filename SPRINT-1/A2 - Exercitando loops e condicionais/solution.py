def corresponding_parenthesis(par: str):
    open = par.count("(")
    close = par.count(")")
    difference = open - close

    if difference > 0:
        return "(" * difference
    elif difference > 0:
        return ")" * (difference * -1)

    return ""


def remove_more_than_two_repetitions(text: str):
    result = ""
    prev_char = ""
    count = 0

    for char in text:
        if char == prev_char:
            count += 1
        else:
            count = 1
        if count <= 2:
            result += char

        prev_char = char

    return result
