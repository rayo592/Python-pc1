#creamos las matrices para asignar cada extensión con los MIMES
sufijos = {
    'gif':'image/gif',
    'jpg':'image/jpeg',
    'jpeg':'image/jpeg',
    'png':'image/png',
    'pdf':'application/pdf',
    'txt':'text/plain',
    'zip':'application/zip'
    }

# Pedimos los datos
archiv = input('coloque el nombre de su archivo: ')
archiv = archiv.lower().strip()

# separamos archivo de extension
k, suf = archiv.split('.')


# Obtendo valor MIME correspondiente de diccionario
if suf.lower() in sufijos.keys():
    x = sufijos.get(suf)
    print(x)
else:
    print("application/octet-stream")
