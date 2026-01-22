
# Definición de utilidades y probabilidades para las decisiones
utilidad_sin_info = {"decisión_1": 100, "decisión_2": 150}
probabilidades_sin_info = {"decisión_1": 0.6, "decisión_2": 0.4}

utilidad_con_info = {"decisión_1": {"estado_1": 120, "estado_2": 80},
                     "decisión_2": {"estado_1": 160, "estado_2": 140}}
probabilidades_con_info = {"estado_1": 0.7, "estado_2": 0.3}

# Cálculo del valor esperado sin información
def valor_esperado_sin_info():
    return sum(utilidad_sin_info[dec] * probabilidades_sin_info[dec] for dec in utilidad_sin_info)

# Cálculo del valor esperado con información
def valor_esperado_con_info():
    valor = 0
    for estado, prob_estado in probabilidades_con_info.items():
        mejor_utilidad = max(utilidad_con_info[dec][estado] for dec in utilidad_con_info)
        valor += mejor_utilidad * prob_estado
    return valor

# Calcular el Valor de la Información (VI)
def calcular_valor_informacion():
    vi = valor_esperado_con_info() - valor_esperado_sin_info()
    return vi

# Ejemplo de uso
vi = calcular_valor_informacion()
print("Valor de la Información:", vi)
