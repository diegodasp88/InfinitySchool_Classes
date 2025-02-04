# Exercício 2: Criem uma classe "Cachorro" que deve conter as propriedades:
# nome, raca, idade

# Essa classe também deve ter um metódo "latir()" que irá mostrar na tela:
# "O {nome do cachorro} está latindo"

# a. Crie um objeto da classe "Cachorro"
# b. Chame o metódo "latir()" para esse cachorro
# c. Crie outro objeto da classe "Cachorro"
# d. Chame o metódo "latir()" para esse outro cachorro.
# e. Crie um metódo "aniversario()" que toda vez que for chamado irá somar a propria idade do cachorro em +1

class Cachorro:
    def __init__(self, nome: str, raca: str, idade: int):
        self.__validar(nome, raca, idade) # Chamar a validação antes dos parâmetros
        self.nome = nome
        self.raca = raca
        self.idade = idade

    # Método para validar os parâmetros do construtor
    def __validar(self, nome: str, raca: str, idade: int):
        if not isinstance(nome, str):
            raise ValueError('O nome deve ser uma string.')
        if not isinstance(raca, str):
            raise ValueError('A raça deve ser uma string.')
        if not isinstance(idade, int):
            raise ValueError('A idade de ver um número inteiro.')

    def latir(self):
        print(f'O {self.nome} está latindo.')

    def aniversario(self):
        self.idade += 1
        print(f'{self.nome} agora tem {self.idade} anos')

# a. Crie um objeto da classe "Cachorro"
cachorro1 = Cachorro('Zeus', 'Pastor Alemão', 4)

# b. Chame o metódo "latir()" para esse cachorro
cachorro1.latir()

# c. Crie outro objeto da classe "Cachorro"
cachorro2 = Cachorro('Shake', 'RND', 9)

# d. Chame o metódo "latir()" para esse outro cachorro.
cachorro2.latir()

# e. Crie um metódo "aniversario()" que toda vez que for chamado irá somar a propria idade do cachorro em +1
print(cachorro1.idade)
cachorro1.aniversario()

print(cachorro2.idade)
cachorro2.aniversario()