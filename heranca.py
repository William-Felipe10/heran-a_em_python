
class Animal:
    def __init__(self,nome):
        self.nome = nome
    
    def fazer_som(self):
        print(f"O {self.nome} faz algum som.")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca



    def fazer_som(self):
        print('O cachorro faz au au!')

if __name__== '__main__':
    # Criando uma instância da classe Animal
    animal_generico = Animal(input('Digite o nome de um Animal: '))
    cachorro1 = Cachorro('Rex','Labrador')


    # Acessando métodos das classes
    cachorro1.fazer_som()
    animal_generico.fazer_som()




