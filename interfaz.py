import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
FS = 44100  # Frecuencia de muestreo (Hz)
N = 1024  # Tamaño del buffer de datos (número de muestras)

# Inicializar la ventana principal
root = tk.Tk()
root.title("Melodic Spectre - Espectro Simulado")
root.geometry("800x600")
root.configure(bg="#2C3E50")

# Configuración de la figura de matplotlib
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_title("Espectro de Frecuencias Simulado en Tiempo Real", fontsize=14)
ax.set_xlabel("Frecuencia (Hz)", fontsize=12)
ax.set_ylabel("Amplitud", fontsize=12)
line, = ax.plot([], [], lw=2, color="cyan", label="Espectro")
ax.set_xlim(0, FS // 2)  # Frecuencias hasta la mitad del rango
ax.set_ylim(0, 1)  # Amplitud normalizada
ax.grid()
ax.legend(loc="upper right")

# Función para generar y actualizar el espectro
def actualizar_espectro():
    # Generar datos aleatorios simulando una señal
    señal_simulada = np.random.rand(N) - 0.5  # Ruido blanco centrado en 0

    # Calcular la FFT
    fft_data = np.abs(np.fft.rfft(señal_simulada))  # Magnitud de la FFT
    fft_freqs = np.fft.rfftfreq(N, 1 / FS)  # Frecuencias asociadas

    # Normalizar la amplitud
    fft_data = fft_data / np.max(fft_data) if np.max(fft_data) != 0 else fft_data

    # Actualizar el gráfico
    line.set_data(fft_freqs, fft_data)
    ax.set_xlim(0, FS // 2)  # Mantener rango de frecuencias
    ax.set_ylim(0, 1)  # Mantener rango de amplitud
    canvas.draw()

    # Volver a llamar a la función después de un tiempo corto
    root.after(100, actualizar_espectro)  # 100 ms para alta frecuencia de actualización

# Integrar la figura en Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(expand=True, fill=tk.BOTH)

# Iniciar la actualización del espectro
actualizar_espectro()

# Iniciar el bucle principal de Tkinter
root.mainloop()
