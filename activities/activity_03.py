"""Exercício: Algoritmo de Navegação

Você está em sua localização atual e precisa chegar à
Estação de Metrô Novo Eldorado para não perder o horário da aula.

**Regras:**
- Se a distância for menor que 1km, vá a pé.
- Se estiver chovendo, utilize um transporte por aplicativo.
- O algoritmo só termina quando você atravessar a catraca da estação."""

def navegar_ate_metro():

    print(
        "=== Algoritmo de Navegação: até a Estação Novo Eldorado ===\n"
        "Regras:\n"
        "- Se a distância for menor que 1km, vá a pé.\n"
        "- Se estiver chovendo, utilize um transporte por aplicativo.\n"
        "- O algoritmo só termina quando você atravessar a catraca da estação.\n"
    )

    distance_km = float(input("Qual a distância até a estação (em km)? ").replace(",", "."))
    raining = input("Está chovendo? (s/n) ").strip().lower() == "s"

    if raining:
        transport = "app"
    elif distance_km < 1:
        transport = "a_pe"
    else:
        transport = "transporte_publico"

    print("\nDecisão tomada:")
    if transport == "app":
        print("- Está chovendo -> usar transporte por aplicativo.")
    elif transport == "a_pe":
        print("- Distância < 1km e não está chovendo -> ir a pé.")
    else:
        print("- Distância >= 1km e não está chovendo -> usar transporte público (ônibus/metrô).")

    at_station = False
    passed_turnstile = False

    while not passed_turnstile:
        if not at_station:
            print("\nEtapas do trajeto:")
            if transport == "a_pe":
                print("- Saia da sua localização atual.")
                print("- Caminhe seguindo o trajeto principal até a estação.")
                print("- Chegue na entrada da Estação Novo Eldorado.")
            elif transport == "app":
                print("- Abra o aplicativo de transporte.")
                print("- Confirme o local de embarque e o destino: Estação Novo Eldorado.")
                print("- Aguarde o motorista e embarque.")
                print("- Desembarque na entrada da estação.")
            else:
                print("- Vá até o ponto/terminal mais próximo.")
                print("- Pegue um transporte em direção à Estação Novo Eldorado.")
                print("- Desça próximo à estação e vá até a entrada.")

            at_station = True

        print("\nVocê chegou na estação.")
        ticket_ok = input("Você tem bilhete/cartão válido para entrar? (s/n) ").strip().lower()

        if ticket_ok != "s":
            print("Ação: resolver pagamento/recarga do bilhete antes de entrar.")
            continue

        passed = input("Você atravessou a catraca? (s/n) ").strip().lower()
        if passed == "s":
            passed_turnstile = True
            print("\nVocê chegou ao seu destino e não vai se atrasar para aula")
        else:
            print("Ainda não atravessou a catraca. Tente novamente.")

if __name__ == "__main__":
    navegar_ate_metro()