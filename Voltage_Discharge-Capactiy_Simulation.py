import matplotlib.pyplot as plt
import numpy as np

# Constants
q = 96485  # Coulombs
T = 298  # K
R = 8.314  # J/mol*K
Phi = 1e15  # Protons/m^2/s

# Lithium-ion battery parameters
C1 = 4.0  # Ah
C2 = 3.5  # Ah
R1 = 0.05  # ohm
R2 = 0.1  # ohm
K1 = 2.5e-4  # S/m
K2 = 1.5e-4  # S/m
D1 = 1.6e-10  # m^2/s
D2 = 1.2e-10  # m^2/s
sigma1 = 4000  # S/m^2
sigma2 = 3500  # S/m^2
epsilon1 = 0.3
epsilon2 = 0.2

# Silver-zinc battery parameters
C3 = 2.5  # Ah
C4 = 2.0  # Ah
R3 = 0.08  # ohm
R4 = 0.12  # ohm
K3 = 2.0e-4  # S/m
K4 = 1.0e-4  # S/m
D3 = 2.0e-10  # m^2/s
D4 = 1.5e-10  # m^2/s
sigma3 = 3500  # S/m^2
sigma4 = 3000  # S/m^2
epsilon3 = 0.25
epsilon4 = 0.15

# Nickel-hydrogen battery parameters
C5 = 3.5  # Ah
C6 = 3.0  # Ah
R5 = 0.06  # ohm
R6 = 0.08  # ohm
K5 = 1.5e-4  # S/m
K6 = 1.0e-4  # S/m
D5 = 1.8e-10  # m^2/s
D6 = 1.3e-10  # m^2/s
sigma5 = 3000  # S/m^2
sigma6 = 2500  # S/m^2
epsilon5 = 0.2
epsilon6 = 0.1

# Time
t = np.linspace(0, 3600, 1000)  # seconds

# Discharge capacity
Q1 = C1 * 3600  # Coulombs
Q2 = C2 * 3600  # Coulombs
Q3 = C3 * 3600  # Coulombs
Q4 = C4 * 3600  # Coulombs
Q5 = C5 * 3600  # Coulombs
Q6 = C6 * 3600  # Coulombs

# Irradiation function
def G(t):
    return Phi * t

# Voltage function for lithium-ion battery after irradiation
def V1(q1, t):
    n1 = q1 / Q1
    i1 = (C1 * n1) ** 0.5 / R1
    i2 = (C2 * (1 - n1)) ** 0.5 / R2
    c1 = i1 / (2 * K1 * epsilon1)
    c2 = i2 / (2 * K2 * epsilon2)
    dV1dt = -R * T / q1 * (c1 * sigma1 * D1 * epsilon1 + c2 * sigma2 * D2 * epsilon2)
    return -i1 * R1 - i2 * R2 - dV1dt

# Voltage function for silver-zinc battery after irradiation
def V2(q2, t):
    n2 = q2 / Q3
    i3 = (C3 * n2) ** 0.5 / R3
    i4 = (C4 * (1 - n2)) ** 0.5 / R4
    c3 = i3 / (2 * K3 * epsilon3)
    c4 = i4 / (2 * K4 * epsilon4)
    dV2dt = -R * T / q2 * (c3 * sigma3 * D3 * epsilon3 + c4 * sigma4 * D4 * epsilon4)
    return -i3 * R3 - i4 * R4 - dV2dt

# Voltage function for nickel-hydrogen battery after irradiation
def V3(q3, t):
    n3 = q3 / Q5
    i5 = (C5 * n3) ** 0.5 / R5
    i6 = (C6 * (1 - n3)) ** 0.5 / R6
    c5 = i5 / (2 * K5 * epsilon5)
    c6 = i6 / (2 * K6 * epsilon6)
    dV3dt = -R * T / (n3 * q) * (c5 * sigma5 * D5 * epsilon5 + c6 * sigma6 * D6 * epsilon6)
    return -i5 * R5 - i6 * R6 - dV3dt

# Plot the voltage as a function of the discharge capacity for each battery after irradiation
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))

q1 = np.linspace(0, Q1, 1000)
ax1.plot(q1/3600, V1(q1, t[-1]), label="Lithium-ion")
ax1.set_xlabel("Discharge Capacity (Ah)")
ax1.set_ylabel("Voltage (V)")
ax1.legend()

q2 = np.linspace(0, Q3, 1000)
ax2.plot(q2/3600, V2(q2, t[-1]), label="Silver-zinc")
ax2.set_xlabel("Discharge Capacity (Ah)")
ax2.set_ylabel("Voltage (V)")
ax2.legend()

q3 = np.linspace(0, Q5, 1000)
ax3.plot(q3/3600, V3(q3, t[-1]), label="Nickel-hydrogen")
ax3.set_xlabel("Discharge Capacity (Ah)")
ax3.set_ylabel("Voltage (V)")
ax3.legend()

plt.show()


