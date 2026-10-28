# Orientação a Objetos: Paradigma de Programação

# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Getter
    def get_fabricante_e_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
        # return self.__fabricante

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    def get_num_registro(self):
        return self.__num_registro


class Carro(Veiculo):
    # Mét odo __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')


class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Sou uma motocicleta e corro muito!')


class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        super().__init__(fabricante, modelo)
        self.__cat = categoria

    def movimentar(self):
        print(f'Sou um avião e voo alto!')

    def get_categoria(self):
        return self.__cat


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabricante_e_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')
    # print(meu_veiculo.fabricante)
    # print(meu_veiculo.modelo)

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabricante_e_modelo()
    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabricante_e_modelo()

    moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fabricante_e_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabricante_e_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')
