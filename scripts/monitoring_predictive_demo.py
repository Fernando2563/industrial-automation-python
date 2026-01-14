Industrial Monitoring & Predictive Logic Demo
Author: Fernando Alves Cardoso

Simulação de monitoramento industrial com análise básica
e lógica preditiva simples usando Python.
"""

import pandas as pd
import numpy as np
import time


# -------------------------------
# Simulação de sensores
# -------------------------------
def read_sensors():
    """
    Simula leitura de sensores industriais
    """
    data = {
        "temperature": np.random.normal(70, 5),
        "current": np.random.normal(15, 2),
        "vibration": np.random.normal(0.8, 0.1),
        "timestamp": time.time()
    }
    return data


# -------------------------------
# Lógica preditiva simples
# -------------------------------
def predictive_check(sensor_data):
    alerts = []

    if sensor_data["temperature"] > 80:
        alerts.append("High temperature detected")

    if sensor_data["current"] > 20:
        alerts.append("Overcurrent condition")

    if sensor_data["vibration"] > 1.0:
        alerts.append("Abnormal vibration")

    return alerts


# -------------------------------
# Execução principal
# -------------------------------
if __name__ == "__main__":
    for _ in range(5):
        sensors = read_sensors()
        alerts = predictive_check(sensors)

        print("Sensors:", sensors)

        if alerts:
            print("ALERTS:", alerts)
        else:
            print("Status: OK")

        print("-" * 40)
        time.sleep(1)
