horas = float(input("Digite o valor a cada hora trabalhada: "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = horas * quantidade_horas

if salario_bruto <= 900:
    p = 0
    desconto_ir = 0
    desconto_ir_desc = 'isento'

elif salario_bruto > 900 and salario_bruto <= 1500:
    p = 5
    desconto_ir = salario_bruto * (p/100)
    desconto_ir_desc = f'{p}%'

elif salario_bruto > 1500 and salario_bruto <= 2500:
    p = 10
    desconto_ir = salario_bruto * (p/100)
    desconto_ir_desc = f'{p}%'

elif salario_bruto > 2500:
    p = 20
    desconto_ir = salario_bruto * (p/100)
    desconto_ir_desc = f'{p}%'

desconto_inss = salario_bruto * (10/100)
desconto_sindicato = salario_bruto * (3/100)
desconto_fgts = salario_bruto * (11/100)

total_descontos = desconto_inss + desconto_sindicato + desconto_ir

espaco = 10 * " "
    
print(f'Salário bruto: ({horas} * {quantidade_horas}) {10*" "}:R$ {salario_bruto:.2f}\n'
      f'(-) IR ({desconto_ir_desc}){28*" "}:R$ {desconto_ir:.2f}\n'
      f'(-) INSS (10%){25*" "}:R$ {desconto_inss:.2f}\n'
      f'(-) SINDICATO (3%){21*" "}:R$ {desconto_sindicato:.2f}\n'
      f'FGTS (11%){29*" "}:R$ {desconto_fgts:.2f}\n'
      f'Total de descontos{21*" "}:R$ {total_descontos:.2f}\n'
      f'Salário Liquido{24*" "}:R$ {salario_bruto - total_descontos:.2f}')                                    