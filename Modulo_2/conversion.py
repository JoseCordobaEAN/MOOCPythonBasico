import datetime # Nos ayuda a trabajar con fechas

edad = input('¿Cual es tu edad? ')
ano = datetime.datetime.now().year
edad = int(edad)

ano_nacimiento = ano - edad

mensaje = 'Naciste el ' + str(ano_nacimiento)

print(mensaje)

print(float(ano_nacimiento))