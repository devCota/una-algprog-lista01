"""Exercício: Logística de E-commerce
Você decidiu comprar o novo iPhone 17 na Amazon,
mas precisa garantir que a compra seja segura,
econômica e bem-sucedida.

**Regras:**
- Verifique se o vendedor é "Amazon" ou "Loja Oficial Apple".
- O saldo no cartão deve ser validado antes de confirmar.
- Se o frete for grátis, selecione-o; caso contrário, avalie o prazo."""

def compra_iphone():

    products = [
        {"name": "iPhone 17 128GB", "seller": "Amazon", "price": 7499, "free_shipping": True,  "delivery_days": 5},
        {"name": "iPhone 17 256GB", "seller": "Amazon", "price": 7999, "free_shipping": False, "delivery_days": 7},
        {"name": "iPhone 17 Pro 256GB", "seller": "Loja Oficial Apple", "price": 9299, "free_shipping": True,  "delivery_days": 6},
        {"name": "iPhone 17 Pro Max 512GB", "seller": "Loja Oficial Apple", "price": 10999, "free_shipping": False, "delivery_days": 10},
        {"name": "iPhone 17 128GB (importado)", "seller": "TechImports", "price": 6899, "free_shipping": True, "delivery_days": 18},
        {"name": "iPhone 17 Pro 128GB", "seller": "Marketplace X", "price": 8999, "free_shipping": False, "delivery_days": 12},
    ]

    allowed_sellers = ["Amazon", "Loja Oficial Apple"]

    print(
        "=== Compra do iPhone 17 (simulação) ===\n"
        "Regras:\n"
        "- Vendedor deve ser Amazon ou Loja Oficial Apple\n"
        "- Validar saldo do cartão antes de confirmar\n"
        "- Se frete for grátis, selecionar; senão, avaliar prazo\n"
    )

    max_days = int(input("Qual o prazo máximo aceitável de entrega (em dias)? "))
    card_balance = float(input("Qual o saldo disponível no cartão (R$)? ").replace(",", "."))

    query = input("\nBuscar: ").strip().lower()

    terms = [t for t in query.split() if t]

    results = []
    for p in products:
        name = p["name"].lower()
        if all(term in name for term in terms):
            results.append(p)

    if not results:
        print("Nenhum produto encontrado para essa busca.")
    else:
        print("\nResultados encontrados:")
        for i, p in enumerate(results, start=1):
            frete_txt = "grátis" if p["free_shipping"] else "pago"
            print(f"{i}. {p['name']} | Vendedor: {p['seller']} | R$ {p['price']} | Frete: {frete_txt} | Prazo: {p['delivery_days']} dias")

        choice = int(input("\nEscolha o número do produto: "))
        if choice < 1 or choice > len(results):
            print("Escolha inválida.")
        else:
            selected = results[choice - 1]

            if selected["seller"] not in allowed_sellers:
                print("Compra cancelada: vendedor não permitido (não é Amazon nem Loja Oficial Apple).")

            elif (not selected["free_shipping"]) and (selected["delivery_days"] > max_days):
                print("Compra cancelada: frete não é grátis e o prazo está acima do aceitável.")

            elif card_balance < selected["price"]:
                print("Compra cancelada: saldo insuficiente no cartão.")

            else:
                print("\nCompra aprovada!")
                print(f"Produto: {selected['name']}")
                print(f"Vendedor: {selected['seller']}")
                print(f"Total: R$ {selected['price']}")

if __name__ == "__main__":
    compra_iphone()
