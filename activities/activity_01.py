"""Exercício: O Desafio da Travessia

Um fazendeiro precisa levar um lobo,
uma cabra e um maço de couve para o outro lado do rio.
Ele tem um barco que só permite levar ele e mais um item.

**Regras:**
- Se o lobo ficar sozinho com a cabra, ele a come.
- Se a cabra ficar sozinha com a couve, ela a come."""

def validar_travessia():
    """
    Resolução:
    Primeiro o homem vai com a cabra para o lado b, depois volta sozinho
    em seguida pega o lobo e atravessa, pega a cabra e volta para o lado A
    deixa a cabra pega a couve e volta para o lado B, por fim volta sozinho
    para o lado A pega a cabra e finaliza a travessia.
    """

    lado_a = ["humano", "lobo", "cabra", "couve"]
    lado_b = []
    
    input_1 = input("Quem vai atravessar primeiro?\n")
    lado_a.remove(input_1)
    lado_a.remove("humano")
    lado_b.extend([input_1, "humano"])
    input_2 = input("O homem deve trazer alguém de volta?\n")
    input_3 = input("Quem será o proximo a atravessar?\n")
    input_4 = input("O homem deve trazer alguém de volta?\n")
    input_5 = input("Quem será o proximo a atravessar?\n")
    print(input_1)

if __name__ == "__main__":
    validar_travessia()