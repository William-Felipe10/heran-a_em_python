class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print('O carro está acelerando.')

    def frear(self):
        print('O carro está freiando.')

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.ano = ano

    def abrir(self):
        print(f'A porta do {self.modelo} está abrindo.')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def empinar(self):
        print(f'O motoqueiro da moto {self.marca} está empinando.')

if __name__ == '__main__':
    veiculo_qualquer = Veiculo('Ford', 'Ford Mustang')
    carro1 = Carro('Ford', 'Mustang', 2023)
    moto1 = Moto('Honda', 'XRE-160', 'Rosa')

    veiculo_qualquer.acelerar()
    veiculo_qualquer.frear()

    carro1.abrir()

    moto1.empinar()
