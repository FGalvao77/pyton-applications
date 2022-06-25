# criando uma classe em Python com informações sobre pessoa

class Person:
    def __init__(self, name: str, age: int, weight: float):
        self.name = name        # nome
        self.age = age          # idade
        self.weight = weight    # peso

    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.weight)

    def get_older(self, years: int):
        self.age += years   #  adicionar ou subtrair da idade


# instanciando um objeto com a classe "Person"
p1 = Person('Fernando', 42, 82)
p1.print_info()     # imprimindo as informações

# com a função "get_older" iremos subtrair 06 anos da idade original
p1.get_older(-6)
p1.print_info()     # imprimindo as informações

# utilizando a biblioteca "pickle" para salvar o arquivo serializado
import pickle as pkl

# instanciando novo objeto
p2 = Person('kátia', 40, 70)

# realizando a gravação do arquivo
with open('katia.pkl', 'wb') as f:
    pkl.dump(p2, f)

# realizando a leitura do arquivo gravado e isntanciando no objeto "p2"
with open('katia.pkl', 'rb') as f:
    p2 = pkl.load(f)

# com a função "print_info()" da classe "Person" imprimindo as informações do objeto "p2"
p2.print_info()