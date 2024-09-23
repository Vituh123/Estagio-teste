#Usei o json disponível no email como fonte dos dados do faturamento mensal!!

#Dias Ignorados como dito na descrição da questão03 por serem finais de semana ou feriados:
#("dia 4", 0.0),("dia 5", 0.0),("dia 7", 0.0),("dia 11", 0.0),("dia 12", 0.0),
#("dia 18", 0.0),("dia 19", 0.0),("dia 25", 0.0),("dia 26", 0.0),

def cal_fatu(faturamento):
    menor = float('inf')
    maior = float('-inf')
    total = 0
    dias = len(faturamento)
    maior_dia = ""
    menor_dia = ""

    for dia, valor in faturamento:
        if valor < menor:
            menor = valor
            menor_dia = dia
        if valor > maior:
            maior = valor
            maior_dia = dia
        total += valor

    media = total / dias if dias > 0 else 0

    acima_media = sum(1 for dia, valor in faturamento if valor > media)

    return menor, maior, acima_media, menor_dia, maior_dia

faturamento_diario = [
    ("dia 1", 22174.1664), ("dia 2", 24537.6698), ("dia 3", 26139.6134),
    ("dia 6", 26742.6612), ("dia 8", 42889.2258), ("dia 9", 46251.174),
    ("dia 10", 11191.4722), ("dia 13", 3847.4823), ("dia 14", 373.7838),
    ("dia 15", 2659.7563), ("dia 16", 48924.2448), ("dia 17", 18419.2614),
    ("dia 20", 35240.1826), ("dia 21", 43829.1667), ("dia 22", 18235.6852),
    ("dia 23", 4355.0662), ("dia 24", 13327.1025), ("dia 27", 25681.8318),
    ("dia 28", 1718.1221), ("dia 29", 13220.495), ("dia 30", 8414.61)]

menor, maior, acima_media, menor_dia, maior_dia = cal_fatu(faturamento_diario)

print("=============Faturamento do mês!===============")
print(f"O menor faturamento foi do {menor_dia}: R${menor:.2f}")
print(f"O maior faturamento foi do {maior_dia}: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média: {acima_media}")