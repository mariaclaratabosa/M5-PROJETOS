# main.py
def div_by_zero():
    a = 1
    b = 0

    return a / b


def unexisting_key():
    my_dict = {"name": "Alex", "module": "M5"}

    return my_dict["address"]


def unexisting_index():
    my_list = [0, 1]

    return my_list[5]


def misterious_error():
    a = 5

    return a.capitalize()


if __name__ == "__main__":
    try:
        div_by_zero()
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    try:
        unexisting_key()
    except KeyError:
        print("Chave não encontrada")
    try:
        unexisting_index()
    except IndexError:
        print("Index não encontrado")
    try:
        misterious_error()
    except AttributeError:
        print("Atributo não é válido com números")
