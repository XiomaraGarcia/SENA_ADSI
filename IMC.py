# Calcula indice de masa corporal.

weight = float(input('escriba su peso en kg:'))
height = float(input(' escriba su estatura en cm:'))

IMC = weight  / (height**2)
print('IMC:', round(IMC,1))
if IMC < 18.5:
    print('Bajo peso')
elif 18.5<= IMC and IMC <25:
     print('Normal')
elif 25<= IMC and IMC <30:
    print('Sobre peso')
elif IMC >=30:
    print('Obesidad')
print('IMC:' , IMC)

