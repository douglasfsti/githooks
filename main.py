from Triangulo import Triangulo


if __name__ == "__main__":
    casos_testes = [
        [7.0, 5.0, 7.0],
        [6.0, 6.0, 10.0],
        [6.0, 6.0, 6.0],
        [5.0, 7.0, 2.0],
        [6.0, 8.0, 10.0]
    ]
    t = Triangulo()

    for caso_teste in casos_testes:
        print(t.determinar_tipo(caso_teste[0], caso_teste[1], caso_teste[2]))
