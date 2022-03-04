# Calcula indice de masa corporal.

#Variables
#Peso 55
weight = float(input('escriba su peso en kg :'))
#Estatura 1,72
height = float(input('escriba su estatura en metros:'))

# 18,63456321 = 55 / (1,72)*2
IMC = weight  / (height**2)

#Imprimes por Consola.
print('IMC:', round(IMC,1))
#IMC: 18,6

#Condicional SI y SINO
#Condicional IF y ELSE

#IMC: 18,5
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