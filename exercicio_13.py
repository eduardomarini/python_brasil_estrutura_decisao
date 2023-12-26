
n = str(input("Digite o número correspondente ao dia da semana [1] - [7]: "))

while (n != '1' and n != '2' and n != '3' and n != '4' and n != '5' and n != '6' and n != '7'):
    n = str(input("Número inválido, digite o número correspondente ao dia da semana [1] - [7]: "))

if n == '1':
    print ('1 - DOMINGO')
elif n == '2':
    print('2 - SEGUNDA')
elif n == '3':
    print('3 - TERÇA')
elif n  == '4':
    print('4 - QUARTA')
elif n == '5':
    print('5 - QUINTA')
elif n == '6':
    print('6 - SEXTA')
elif n == '7':
    print('7 - SABÁDO')
    