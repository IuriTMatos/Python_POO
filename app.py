from modelos.restaurante import Restaurante

restaurante_burger = Restaurante("burger", "hamburgueria")
restaurante_pizza = Restaurante("pizza", "pizzaria")
restaurante_sushi = Restaurante("sushi", "japonesa")

restaurante_burger.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
  