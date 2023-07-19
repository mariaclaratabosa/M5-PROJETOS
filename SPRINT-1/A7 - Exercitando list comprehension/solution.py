def list_comprehension_exercise_1():
    return [number for number in range(11)]


def list_comprehension_exercise_2():
    return [
        number for number in range(22)
        if number % 2 == 0 or number % 3 == 0
    ]


def list_comprehension_exercise_3():
    return [
        number for number in range(-5, 32)
        if number % 2 == 0 and number % 5 == 0
    ]


def list_comprehension_exercise_4():
    return [number ** 2 for number in range(11)]


def list_comprehension_exercise_5(sentence: str):
    return [letter for letter in sentence if letter.isupper()]


def list_comprehension_exercise_6(sentence: str):
    return [
        word for word in sentence.split()
        if len(word) >= 4 and word[0] == "r"
        ]
