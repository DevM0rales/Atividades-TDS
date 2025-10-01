# Módulo de Cálculo de Frete - Versão 1.0
def calcular_frete(distancia_km, peso_kg, tipo_entrega):
    """
    Calcula o custo do frete com base na distância, peso e tipo de entrega.
    Tipos de entrega:
    - Normal: 0 (padrão)
    - Expresso: 1
    - Urgente: 2
    """

    tabela_precos = [10.00, 15.50, 20.00]
    custo_base = 0
    
    if not 0 <= tipo_entrega <= 2:
        return "Erro: Tipo de entrega inválido."
 
    custo_base = distancia_km * tabela_precos[tipo_entrega]
    
    if peso_kg > 50:
        custo_peso = peso_kg * 0.20
    elif 10 < peso_kg <= 50:
        custo_peso = peso_kg * 0.10
    elif peso_kg > 0:
        custo_peso = 0.05
    
    custo_total = custo_base + custo_peso
    
    return custo_total
print(f"Cenário 1: {calcular_frete(50, 15, 0)}")
print(f"Cenário 2: {calcular_frete(20, 60, 2)}")
print(f"Cenário 3: {calcular_frete(150, 5, 1)}")
print(f"Cenário 4: {calcular_frete(30, 8, 0)}")

