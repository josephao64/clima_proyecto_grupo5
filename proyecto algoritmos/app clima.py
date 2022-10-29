import tkinter as tk             
import requests
import time
 

def obtenerclima(canvas):
    ciudad = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid=8e8a715bfbe6b108a1b9e4e424be3142"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    presion = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    info_final = condition + "\n" + str(temp) + "°C" 
    datos_finales = "\n"+ "Temp Min: " + str(min_temp) + "°C" + "\n" + "Temp Max: " + str(max_temp) + "°C" +"\n" + "Presión: " + str(presion) + "\n" +"Humedad: " + str(humidity) + "\n" +"Velocidad del viento: " + str(wind) + "\n" + "Salida del sol: " + sunrise + "\n" + "Puesta de sol: " + sunset
    etiqueta1.config(text = info_final)
    etiqueta2.config(text = datos_finales)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', obtenerclima)

etiqueta1 = tk.Label(canvas, font=t)
etiqueta1.pack()
etiqueta2 = tk.Label(canvas, font=f)
etiqueta2.pack()
canvas.mainloop()