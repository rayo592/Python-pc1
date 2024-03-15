#Solicitamos el monto en consumo del cliente
consumo = input("Por favor, coloque el monto que consumió en total: " )
consumo = float(consumo)

#se pide solicitar porcentaje
percent = input("coloque solo el número de porcentaje del monto que consumió que desea dejar como propina: " )
percent = float(percent)

#mostrar monto de propina en dinero
propina = consumo * percent / 100
print (f"Usted dejará {propina} $ como propina")