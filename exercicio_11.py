salario = float(input("Digite o seu salário: "))

if salario <= 280:
    p = 20
    percentual =  20/100    
    
elif salario > 280 and salario <= 700:
    p = 15
    percentual =  15/100

elif salario > 700 and salario < 1500:
    p = 10
    percentual =  10/100
     
elif salario >= 1500:
    p = 5
    percentual =  5/100
    
percentual_aumento = percentual * salario
novo_salario = percentual_aumento + salario

print(f'O seu salário é de: R$ {salario:.2f}\n'
        f'O percentual de aumento é de {p}%,\n'
        f'O valor aplicado é de {percentual_aumento:.2f}\n'
        f'O seu novo salário é de: R$ {novo_salario:.2f}\n' )
    
    
    

    