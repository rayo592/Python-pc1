#Mostrar hora
hora_actual = input("Coloque su hora: " )
hora_actual = hora_actual.lower().strip()
horas, minutos = hora_actual.split(':')
h = float(horas) + int(minutos)/60
#Se colocan las condiciones y se muestra las indicaciones según sea la hora
if 7<= h <= 8:
    print('Toca desayunar')
elif 12<= h <= 13:
    print('Toca almorzar')
elif 18<= h <= 19:
    print('Toca cenar')