# Calcula indice de masa corporal.
#Variables
weight = float(input('escriba su peso en kg :'))
height = float(input('escriba su estatura en metros:'))

IMC = weight  / (height**2)
#Imprimes por Consola.
print('IMC:', round(IMC,1))

if IMC < 18.5:
    print('Underweight')

elif IMC >= 18.5 and IMC <25:
     print('Normal Weight')
     
elif IMC >= 25 and IMC <30:
    print('Overweight')

elif IMC >=30 and IMC <35:
    print('Obese')

else:
    print('Clinically Obese')