class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
       return f"{self._nome} | {self._categoria} "
    @classmethod

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return "aberto" if self._ativo else "fechado"

    
restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_pizza = Restaurante("pizza", "piza")

Restaurante.listar_restaurantes()

