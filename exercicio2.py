def main():
    fibonacci = []
    
    while(10 == 10):
        print("Verifique se um número pertence a sequencia fibonacci")
        numero_selecionado = int(input("Número a ser analisado: "))
    
        retornofibo = gera_fibonacci(numero_selecionado)
        
        fibonacci = retornofibo
        print(fibonacci)
        verifica_existencia_fibonacci(numero_selecionado,fibonacci)
def gera_fibonacci(numero_analisar):
    
    inicio1 = True
    fibonacci_temp = [0,1]
    #gerando sequencia fibonacci até o numero selecionado"
    for i in range(1, numero_analisar+10):
        #gera o elemento [2] para calcular o resto depois
        if inicio1 == True:
            
            fibonacci_temp.append(i+(i-1))
            inicio1 = False
            
        else:
            
            fibonacci_temp.append(fibonacci_temp[i]+fibonacci_temp[i-1])
    
    return fibonacci_temp

def verifica_existencia_fibonacci(numero_selecionado, fibonacci):
    continua = True
    #percorre o array verificando se nele se encontra o número
    for i in fibonacci:
        
        if numero_selecionado == i:
            
            print("Número", numero_selecionado, "pertence a sequência fibonacci")
            continua = False
            break
    if continua == True:
        print("Número", numero_selecionado,",não pertence a sequência fibonacci")
    return
        
    
main()
