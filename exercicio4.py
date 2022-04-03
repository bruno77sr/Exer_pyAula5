#usuário os valores de três contas de
#consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é
#suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
#insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas

agua =  float(input("Digite o valor da conta de água: "))
luz =  float(input("Digite o valor da conta de luz: "))
tel =  float(input("Digite o valor da conta de telefone: "))


sal =  float(input("Digite o valor do seu sálario: "))

calcContas = agua + luz + tel
resul =  sal - calcContas

if resul < 0:
    print("Valor insuficiente! ")
else:
    print("Valor suficiente! \n O valor restante é %.2f" %(resul))
