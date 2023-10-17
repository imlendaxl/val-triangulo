n1 = float(input('\033[0;49;31mdigite um comprimento\n'))
n2 = float(input('\033[0;49;33mdigite um outro comprimento\n'))
n3 = float(input('\033[0;49;35mdigite um outro comprimento\n'))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('\033[0;49;34mForma um triangulo')
else:
    print('\033[0;49;39mNão forma um triangulo')

# eita breia ai sim seu dpimenta
