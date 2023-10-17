# Validador de Triângulo

x1 = float(input('digite um comprimento\n'))
x2 = float(input('digite um outro comprimento\n'))
x3 = float(input('digite um outro comprimento seu rapaz\n'))

if x1 < x2+x3 and x2 < x1+x3 and x3 < x1+x2:
    print(f'{x1},{x2} e {x3} formam um triangulo')
else:
    print(f'{x1},{x2} e {x3} não formam um triangulo')

def tipo_trian (x1,x2,x3):
    if x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1:
        if x1 == x2 == x3:
            return 'triangulo equilatero'
        elif x1 == x2 or x1 == x3 or x2 == x3:
            return 'triangulo isosceles'
        else:
            return 'triangulo escaleno'
    else:
        return 'não é um triangulo valido'

resultado = tipo_trian (x1,x2,x3)
print(resultado)

# eita breia ai sim seu pimenta
