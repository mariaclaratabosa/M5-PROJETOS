# Exercitando Exceptions
Crie um arquivo main.py e adicione o seguinte código. <br />
```
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
    div_by_zero()
    unexisting_key()
    unexisting_index()
    misterious_error()
```
<br />
Seu objetivo é capturar adequadamente cada uma das exceções, mostrando na tela uma mensagem indicando qual erro foi tratado. Utilize o tratamento na chamada das funções.