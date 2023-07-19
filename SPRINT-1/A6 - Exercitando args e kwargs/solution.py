def sum_numbers(*args):
    return sum(args)


def get_multiplied_amount(multiplier, *args):
    return sum(args) * multiplier


def word_concatenator(*args):
    return " ".join(args)


def inverted_word_factory(*args):
    return " ".join(args)[::-1]


def dictionary_separator(*kwargs):
    return (
        list(kwargs.keys()),
        list(kwargs.values())
    )
