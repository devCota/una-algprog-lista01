Exercício: O Desafio da Travessia

Um fazendeiro precisa levar um lobo,
uma cabra e um maço de couve para o outro lado do rio.
Ele tem um barco que só permite levar ele e mais um item.

**Regras:**
- Se o lobo ficar sozinho com a cabra, ele a come.
- Se a cabra ficar sozinha com a couve, ela a come.

def validar_travessia():
    lado_a = ["humano", "lobo", "cabra", "couve"]
    lado_b = []
    barco = []
    
    input_1 = input("Quem vai atravessar primeiro?")
    lado_a.pop("humano", input_1)