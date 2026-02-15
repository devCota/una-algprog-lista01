"""Exercício: O Desafio da Travessia

Um fazendeiro precisa levar um lobo,
uma cabra e um maço de couve para o outro lado do rio.
Ele tem um barco que só permite levar ele e mais um item.

**Regras:**
- Se o lobo ficar sozinho com a cabra, ele a come.
- Se a cabra ficar sozinha com a couve, ela a come."""

def validar_travessia():
    status = {
        "fazendeiro": "esquerda",
        "lobo": "esquerda",
        "cabra": "esquerda",
        "couve": "esquerda"
    }

    items = ["lobo", "cabra", "couve", "nada"]

    print(
        "=== Desafio da Travessia ===\n"
        "Um fazendeiro precisa atravessar um rio levando um lobo,\n"
        "uma cabra e uma couve. O barco comporta apenas o fazendeiro\n"
        "e mais um item por vez.\n\n"
        "Regras:\n"
        "- Se o lobo ficar sozinho com a cabra, ele a come.\n"
        "- Se a cabra ficar sozinha com a couve, ela a come.\n\n"
        "Leve: lobo, cabra, couve ou nada"
    )

    while True:
        print("\nEstado atual:", status)

        if all(status[item] == "direita" for item in status):
            print("Você venceu!")
            break

        choice = input("O que levar no barco? ").lower()

        if choice not in items:
            print("Escolha inválida")
            continue

        if choice != "nada" and status[choice] != status["fazendeiro"]:
            print("Esse item não está com o fazendeiro")
            continue

        new_side = "direita" if status["fazendeiro"] == "esquerda" else "esquerda"
        status["fazendeiro"] = new_side

        if choice != "nada":
            status[choice] = new_side

        if status["lobo"] == status["cabra"] and status["fazendeiro"] != status["lobo"]:
            print("O lobo comeu a cabra. Você perdeu!")
            break

        if status["cabra"] == status["couve"] and status["fazendeiro"] != status["cabra"]:
            print("A cabra comeu a couve. Você perdeu!")
            break

if __name__ == "__main__":
    validar_travessia()