import numpy as np
import matplotlib.pyplot as plt

# Parameters of the CERN Proton Synchrotron beam
energy = 1000 # MeV
current = 0.8 # mA
dose_rate = 1.4e-5# Gy/s

# Parameters of the battery
irradiation_time = 36000 # 10 hour of irradiation
irradiation_dose = 100 # 100 Gy of irradiation dose
internal_resistance = 0.1 # 0.1 ohms of internal resistance
capacity = 2.5 # 2.5 Ah of capacity
initial_voltage = 3.7 # 3.7 V of initial voltage

# Calculate the total dose received by the battery
total_dose = dose_rate * irradiation_time

# Calculate the degradation of the battery's capacity due to irradiation
capacity_degradation = 1 - np.exp(-total_dose / capacity)

# Plot the battery's capacity over time
time = np.linspace(0, irradiation_time, num=100)
capacity_over_time = capacity * np.exp(-time * capacity_degradation / irradiation_time)

plt.plot(time, capacity_over_time)
plt.xlabel('Time (s)')
plt.ylabel('Capacity (Ah)')
plt.title('Battery Capacity over Time')
plt.show()




