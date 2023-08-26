import requests
import pandas as pd
import matplotlib.pyplot as plt

# Definir la URL base de la API
base_url = "https://archive-api.open-meteo.com/v1/archive"

#Variables de los parametros
latitude =  19.9855
longitude = -102.2839
startDate = '2023-01-01'
endDate = '2023-01-02'

# Parámetros para la solicitud de pronóstico (puedes ajustar estos valores)
parameters = {
    'latitude': latitude,
    'longitude': longitude,
    'start_date': startDate,
    'end_date': endDate,
    'hourly': 'temperature_2m,relativehumidity_2m,precipitation,rain,windspeed_10m,soil_temperature_0_to_7cm,soil_moisture_0_to_7cm',
    'start': 'current'
}

# Realizar la solicitud a la API
response = requests.get(base_url, params=parameters)
data = response.json()

#UNIDADES DE LOS DATOS
temperature_unit = data['hourly_units']['temperature_2m']
humidity_unit = data['hourly_units']['relativehumidity_2m']
precipitation_unit = data['hourly_units']['precipitation']
rain_unit = data['hourly_units']['rain']
windspeed_unit = data['hourly_units']['windspeed_10m']
soiltemperature_unit = data['hourly_units']['soil_temperature_0_to_7cm']
soilmoisture_unit = data['hourly_units']['soil_moisture_0_to_7cm']

# Crear un DataFrame a partir de los datos
df = pd.DataFrame(data['hourly'])

#AQUI COMIENZAN LOS DATAFRAMES DE LOS DATOS
time = df['time']
temperatures = df['temperature_2m']
humidities = df['relativehumidity_2m']
precipitations = df['precipitation']
rain = df['rain']
windspeed = df['windspeed_10m']
soiltemperature = df['soil_temperature_0_to_7cm']
soilmoisture = df['soil_moisture_0_to_7cm']

# Mostrar el DataFrame en forma tabular
print(windspeed_unit)

# Graficar temperaturas
plt.figure(figsize=(10, 6))
plt.plot(time, temperatures, label='Temperatura '+ temperature_unit)
plt.xlabel('Hora')
plt.ylabel('Temperatura '+ temperature_unit)
plt.title('Temperaturas')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
