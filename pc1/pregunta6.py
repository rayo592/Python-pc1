#se le pide la edad al cliente
edad = int(input("Por favor coloque su edad: " ))

#calculamos datos
if edad < 4:
    entrada = 0
elif edad < 18:
    entrada = 5
else: 
    entrada = 10
#mostramos entrada según la edad
print(f"Para tu edad de {edad} años, tu precio de entrada es: $ {entrada}")