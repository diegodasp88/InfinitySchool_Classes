# -------------------------------------------------------
# Programação Orietada a Objetos (POO)
# -------------------------------------------------------


# Classe: representação abstrata de um conjunto de coisas que possuem as mesmas características (atributos) e comportamentos (métodos)
class Carro:
    # Método Construtor
    def __init__(self, marca: str, modelo: str, placa: str, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ligado = False
    
    # Método Informação
    def info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Placa: {self.placa}')
        print(f'Cor: {self.cor}')
        print('-'*30)


# Criando o carro:
carro1 = Carro('Honda', 'Civic', 'CCC0C22', 'Vermelho')

# Acessando propriedades específicas.
print(f'Marca: {carro1.marca}')
print(f'Modelo: {carro1.modelo}')
print(f'Placa: {carro1.placa}')
print(f'Cor: {carro1.cor}')
print('-'*30)

# Chamando Métodos: acessando todas as propriedades do método.
carro2 = Carro('Chevrolet', 'Civic', 'CCC0C22', 'Vermelho')
carro2.info()

# O B J E T O: Se algo é um objeto: ele tem atributos e métodos.
# S E L F: referencia ao objeto que chama o método.