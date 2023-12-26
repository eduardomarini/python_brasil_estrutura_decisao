turno = input("Em que turno você estuda? digite [M] - matutino, [V] - vespertino ou [N] - noturno: ").upper()
turno = str(turno)

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")

