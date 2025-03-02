import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Para compatibilidad con Mac
import matplotlib.pyplot as plt

# Parámetros de degradación (valores típicos, se pueden ajustar)
k_h2o2 = 0.05  # H₂O₂ (rápida degradación)
k_cloro = 0.02  # Cloro (moderada degradación)
k_edta = 0.005  # EDTA (degradación lenta)

def simular_degradacion(k, concentracion_inicial, dt=0.1, t_max=100):
    """Simula la degradación de un compuesto en fase líquida."""
    tiempos = np.arange(0, t_max, dt)
    concentraciones = []
    C = concentracion_inicial
    for t in tiempos:
        dC = -k * C * dt
        C += dC
        concentraciones.append(C)
    return tiempos, concentraciones

# Condiciones iniciales (concentraciones en mol/L)
C_inicial = 1.0  # Concentración inicial para todos

# Simular degradación antes del blanqueado
t_h2o2, C_h2o2 = simular_degradacion(k_h2o2, C_inicial)
t_cloro, C_cloro = simular_degradacion(k_cloro, C_inicial)
t_edta, C_edta = simular_degradacion(k_edta, C_inicial)

# Simular degradación después del blanqueado (residuos en agua)
k_h2o2_residuo = 0.03  # Degradación más lenta en residuos
k_cloro_residuo = 0.015
k_edta_residuo = 0.002

t_h2o2_r, C_h2o2_r = simular_degradacion(k_h2o2_residuo, C_inicial)
t_cloro_r, C_cloro_r = simular_degradacion(k_cloro_residuo, C_inicial)
t_edta_r, C_edta_r = simular_degradacion(k_edta_residuo, C_inicial)

# Graficar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(t_h2o2, C_h2o2, 'b-', label="H₂O₂")
plt.plot(t_cloro, C_cloro, 'r--', label="Cloro")
plt.plot(t_edta, C_edta, 'g-.', label="EDTA")
plt.xlabel("Tiempo (s)")
plt.ylabel("Concentración (mol/L)")
plt.title("Degradación Antes del Blanqueado")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.subplot(1, 2, 2)
plt.plot(t_h2o2_r, C_h2o2_r, 'b-', label="H₂O₂ Residuo")
plt.plot(t_cloro_r, C_cloro_r, 'r--', label="Cloro Residuo")
plt.plot(t_edta_r, C_edta_r, 'g-.', label="EDTA Residuo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Concentración (mol/L)")
plt.title("Degradación Después del Blanqueado")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

# Ejecucion de entorno virtual : 
# source venv/bin/activate
# pip install numpy matplotlib
# python simulacion_blanqueadores.py

