class DatosMeteorologicos:
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo = nombre_archivo


#.strip() para quitar el \n
    def procesar_datos(self) ->tuple[float, float, float, float, str]:
        suma_temperaturas = 0
        suma_humedad = 0
        suma_presion = 0
        suma_velocidad_viento = 0
        suma_direccion_viento = 0
        contador = 0
        abreviaciones_grados = {'N': 0,'NNE': 22.5,'NE': 45,'ENE': 67.5,'E': 90,'ESE': 112.5,'SE': 135,'SSE': 157.5,'S': 180,'SSW': 202.5,'SW': 225,'WSW': 247.5,'W': 270,'WNW': 292.5,'NW': 315,'NNW': 337.5}

        with open('datos.txt', 'r') as file:
            data = file.read()


        station_records = data.strip().split('\n\n')


        for station_record in station_records:
            lines = station_record.split('\n')
    
            temperatura = 0
            humedad = 0
            presion = 0
            velocidad_viento = 0
            direccion_viento = 0

            for line in lines:
                key, value = line.split(': ')
                if key == 'Temperatura':
                    temperatura = float(value)
                elif key == 'Humedad':
                    humedad = float(value)
                elif key == 'Presion':
                    presion = float(value)
                elif key == 'Viento':
                    velocidad_viento, direccion_viento = value.split(',')
                    velocidad_viento = float(velocidad_viento)
                    direccion_viento = float(abreviaciones_grados[direccion_viento])



            if temperatura is not None and humedad is not None and presion is not None:
                suma_temperaturas += temperatura
                suma_humedad += humedad
                suma_presion += presion
                suma_velocidad_viento += velocidad_viento
                suma_direccion_viento += direccion_viento
                contador += 1

        temperatura_promedio =  suma_temperaturas/ contador
        humedad_promedio = suma_humedad / contador
        presion_promedio = suma_presion / contador
        velocidad_viento_promedio = suma_velocidad_viento / contador
        direccion_viento_promedio = suma_direccion_viento/contador

        direccion_str = None
        closest_value = None

        for key, value in abreviaciones_grados.items():
            diff = abs(value - direccion_viento_promedio)

            if closest_value is None or diff < closest_value:
                direccion_str = key
                closest_value = diff

        return(temperatura_promedio,humedad_promedio,presion_promedio,velocidad_viento_promedio,direccion_str)