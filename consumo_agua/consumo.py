# Bloco 1: Entradas
opcao = input("Digite uma opcao (comercial, casa, apartamento): ")
consumo = float(input("Digite o consumo mensal em m3: "))

# Bloco 2: Verificação exibição da mensagem
match opcao:
    case "comercial":
        print("Tarifa comercial aplicada - consulte o pano corporativo.")
    case "casa" if consumo <= 10:
            print("Consumo econômico - excelente controlede água!")
    case "apartamento" | "casa" if consumo <= 25:
            print("Consumo moderado - dentro do padrão residêncial.")
    case "apartamento" | "casa":
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
    case _:
            print("Opção inválida. Tente novamente.")
                