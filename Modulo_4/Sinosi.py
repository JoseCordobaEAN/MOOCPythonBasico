import datetime as d

hora = d.datetime.now().hour
print('son las', hora)

if hora < 13:
    print('Buenos días')
elif hora < 18:
    print('Buenas Tardes')
else:
    print('Buenas Noches')