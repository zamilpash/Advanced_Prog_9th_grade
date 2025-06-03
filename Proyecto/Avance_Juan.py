import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Datos simulados
#se hace un diccionario con listas vacias 
data = {
    "tiempo": [],
    "vibracion": [],
    "corriente": [],
    "temperatura": [],
    "rpm": [],
    "torque" : []
}

start_time = time.time()
operacion = 50  # valor inicial

def simular_sensores(porcentaje): # funcion que recibe porcentaje de operacion del motor como argumento
    # establece valores iniciales
    base_rpm = 1200
    base_temp = 60
    base_corr = 1
    base_vib = 2
    base_tor = .1

    factor = porcentaje / 100.0 #se calcula un factor que es proporcional al porcentaje de carga de trabajo del motor

    rpm = base_rpm * factor + random.uniform(-20, 20) # toma el valor inicial, lo multiplica por el factor y le suma un digito aleatorio flotante en el rango -50 a 50
    temperatura = base_temp * factor + random.uniform(-2, 2) #aqui el rango del dato aleatorio es menor
    corriente = base_corr * factor + random.uniform(-0.05, 0.05)
    vibracion = base_vib * (factor ** 1.5) + random.uniform(-0.1, 0.1)
    torque = base_tor * factor + random.uniform(-10,10)

    return vibracion, corriente, temperatura, rpm, torque

def actualizar_grafico(i):
    global operacion #la variable se establece como global para no tener que crearla en diferentes funciones
    t = time.time() - start_time
    vibracion, corriente, temperatura, rpm, torque = simular_sensores(operacion)

    data["tiempo"].append(t) #el metodo data sirve para acceder a 
    data["vibracion"].append(vibracion)
    data["corriente"].append(corriente)
    data["temperatura"].append(temperatura)
    data["rpm"].append(rpm)
    data['torque'].append(torque)

    for key in data:
        if len(data[key]) > 100:     # esta condicion es para "normalizar" los valores obtenidos porque no debe de superar 100
            data[key] = data[key][-100:]

    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()

    ax1.plot(data["tiempo"], data["vibracion"], label="Vibración (mm/s)")
    ax2.plot(data["tiempo"], data["corriente"], label="Corriente (A)", color='orange')
    ax3.plot(data["tiempo"], data["temperatura"], label="Temperatura (°C)", color='red')
    ax4.plot(data["tiempo"], data["rpm"], label="RPM", color='green')
    ax5.plot(data['tiempo'], data['torque'], label = 'torque n * m', color = 'purple')

    for ax in [ax1, ax2, ax3, ax4, ax5]:
        ax.legend(loc="upper left")

    ax1.set_ylabel("Vibración")
    ax2.set_ylabel("Corriente")
    ax3.set_ylabel("Temperatura")
    ax4.set_ylabel("RPM")
    ax5.set_ylabel("Torque")
    ax5.set_xlabel("Tiempo (s)")


def actualizar_operacion(val):
    global operacion
    operacion = float(val)

# Crear ventana
ventana = tk.Tk()
ventana.title("Simulación de Sensores del Motor")

# Crear figura y subplots
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(7, 9), sharex=True)
plt.tight_layout()

# Integrar figura en Tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Slider de porcentaje de operación
frame_control = ttk.Frame(ventana)
frame_control.pack(pady=10)

label = ttk.Label(frame_control, text="Porcentaje de operación")
label.pack()

slider = ttk.Scale(frame_control, from_=0, to=100, orient="horizontal", command=actualizar_operacion)
slider.set(50)
slider.pack()

# Iniciar animación
ani = animation.FuncAnimation(fig, actualizar_grafico, interval=500, save_count=100)

# Ejecutar ventana
ventana.mainloop()