edad = int(input('Introduce tu edad: '))
mes = int(input('Introduce tu mes de nacimiento: '))

if edad >= 18:
    print('Eres mayor de edad')
    if mes == 1:
        print('Naciste en enero')
    elif mes == 2:
        print('Naciste en febrero')
else:
    print('Eres menor de edad')
    if(mes == 3):
        print('Naciste en marzo')
