class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.numero_de_exibicoes = 0

    def __str__(self):
        return f'<Filme: {self.titulo}>'

    def __len__(self, duracao):
        self.duracao = duracao

    def __call__(self):
        self.numero_de_exibicoes += 1
        return self.numero_de_exibicoes


jhon_wick = Filme("John Wick", 113)

print(jhon_wick)
print(len(jhon_wick))
print(vars(jhon_wick))
print(jhon_wick())
print(vars(jhon_wick))
