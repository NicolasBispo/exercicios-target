import json

with open("dados.json", encoding="utf-8") as jsong_dados:
    dados = json.load(jsong_dados)



def main():

    print("1 - Menor faturamento ocorrido do mês\n2 - Maior faturamento ocorrido no mês\n3 - Ver numero de dias com faturamento superior a média")

    opcao = int(input("Opção: "))

    if opcao == 1:
        menor_faturamento()
    elif opcao == 2:
        maior_faturamento()
    elif opcao == 3:
        numero_dias()

def menor_faturamento():
    vetor_temp = []
    acumula_zero = [] #dias com zero
    j = 1
    for i in dados:
        vetor_temp.append(i["valor"])
        if i["valor"] == 0:
            acumula_zero.append(j)
        j = j + 1
    print("Menor valor de faturamento foi igual à",min(vetor_temp))
    print("Nos dias: ", acumula_zero)
    return

def maior_faturamento():
    vetor_temp = []
    for i in dados:
        vetor_temp.append(i["valor"])
    p = 0
    m_f = max(vetor_temp)
    for j in vetor_temp:

        if j == m_f:
            print("Maior faturamento no dia: ", p+1, "de", m_f,"reais")
            break
        p = p + 1
    

def numero_dias():
    contador_dias = 0
    media_mensal = 0
    armazena_num_dia = []
    for i in dados:
        media_mensal = media_mensal + i["valor"]
        contador_dias = contador_dias + 1
    
    media_mensal = media_mensal/contador_dias
    dias_media_maior = 0    
    for j in dados:
        if j["valor"] > media_mensal:
            dias_media_maior = dias_media_maior + 1
            armazena_num_dia.append(j["dia"])
    print("Media do mês", media_mensal)
    print("Quantidade de dias com faturamento maior que a média mensal:",dias_media_maior)
    print("Dias que passaram a média:",armazena_num_dia)
    
    return
main()
