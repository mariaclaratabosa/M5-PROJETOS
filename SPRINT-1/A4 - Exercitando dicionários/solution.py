d1 = {"nome": "Kenzinho", "cidade": "Curitiba", "modulo": "M5"}

print(d1["nome"])

print(d1["cidade"])

print(d1["modulo"])

print(d1.get("telefone", "a chave telefone não existe"))

print(d1.keys())

print(d1.values())

lista_1 = ["telefone", "casado", "idade"]
lista_2 = ["999-999-999", False, 28]

d2 = dict(zip(lista_1, lista_2))
print(d2)

d1.update(d2)
print(d1)

d1.pop("casado")

print(d1.pop("idade"))

d1.clear()
print(d1)
