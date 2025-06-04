import numpy as np
import matplotlib.pyplot as plt

lecturas_temp = np.array([21, 22.5, 28.6, 33.9, 22.6, 32.7])

print(f"Valor promedio: {np.mean(lecturas_temp):.2f}")
print(f"Valor maximo: {np.max(lecturas_temp)}")
print(f"Desv. Estandas: {np.std(lecturas_temp):.2f}")


# Simular visualización
horas = np.arange(0, 24, 0.5)
temperatura = 22 + 3 * np.sin(np.pi * horas / 12) + 0.5 * horas + np.random.normal(0, 0.3, len(horas))


# Visualizar.
plt.figure(figsize = (10, 6))
plt.plot(horas, temperatura, 'b', linewidth = 2, label = 'Temperatura')
plt.title(" Monitoreo de Temperatura por 24 hrs", fontsize = 14)
plt.xlabel("Tiempo en horas", fontsize = 12)
plt.ylabel('Temperatura en °C', fontsize = 12)
plt.legend()
plt.savefig('Temperatura_24h.png', dpi = 300)
plt.show()