#pedimos colocar los números
num1 = int(input("Coloque el primer número: " ))
num2 = int(input("Coloque el segundo número: " ))


#Colocamos el calculo para las variables introducidas
suma = num1 + num2
resta = num1-num2
multi = num1*num2
print("""
Se tienen las siguientes opciones:
a) Mostrar una suma de los dos números
b) Mostrar una resta de los dos números (el primero menos el segundo)
c) Mostrar una multiplicación de los dos números 

""" )

opcion = str(input("Escriba de la opción que elige: " ))
opcion = opcion.lower()

if opcion == "a" :
  print(f"La suma de los números es : {suma}")
elif opcion == "b" :
  print(f"La resta de los números es : {resta}")
elif opcion == "c":
  print(f"la multiplicación de los números es {multi}")
else:
  print("la opción no es correcta")