compra = float(input("Digite o valor da compra: "))

if compra > 200:
    calc = compra - compra * 0.20
    print("O valor da Compra com desconto é R$ %.2f" %(calc))
else:
    print("O valor da Compra sem desconto é R$ %.2f" %(compra))