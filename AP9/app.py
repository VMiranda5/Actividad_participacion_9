from modelo.datos_meteorologicos import DatosMeteorologicos

datos = DatosMeteorologicos('datos.txt')
temperatura, humedad, presion, velocidad, direccion = datos.procesar_datos()

print(f'temperatura: {temperatura}')
print(f'humedad: {humedad}')
print(f'presion: {presion}')
print(f'velocidad: {velocidad}')
print(f'direccion: {direccion}')
