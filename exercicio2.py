turno = input("Qual é o seu Turno ? (N = Noturno, D = Diurno) ")
horasT = int(input("Quantas horas trabalhadas ? "))



if turno == "n" or turno == "N":
    sal = 45.00 * horasT
    print("Seu sálario é de = R$ %.2f" %(sal))
elif turno == "d" or turno == "D":
    sal  = 37.50 * horasT
    print("Seu sálario é de = R$ %.2f" %(sal))
else:
    print("ATENÇÃO! N = Noturno, D = Diurno \n ","(", turno,")", "Não é aceito! \nTente Novamente! " )





