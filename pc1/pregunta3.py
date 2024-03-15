#solicitamos cantidad de payasos
payasos = input("Por favor, coloque el número de payasos a entregar: " )
payasos = int(payasos)
#solicita cantidad de muñecas
munecas = input("por favor, coloque el número de muñecas a entregar: " )
munecas = int(munecas)
# se calcula peso total
peso_payasos = payasos*0.112
peso_munecas = munecas*0.075

peso_total = peso_payasos + peso_munecas
peso_total = float(peso_total)

#muestro peso total
print(f"El peso total del paquete es: {peso_total} kg ")