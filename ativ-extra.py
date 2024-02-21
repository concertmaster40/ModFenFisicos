import numpy as np
import matplotlib.pyplot as plt

# Generate angulos from 0 to 180 degrees (in radians)
angulos = np.linspace(0, np.pi, 1250)

# Calculate x and y coordinates for the circle
x_circle = np.cos(angulos)
y_circle = np.sin(angulos)

# Calculate x and y coordinates for cosene, sene, and tangent lines
x_cos = np.cos(angulos)
y_cos = np.zeros_like(angulos)
x_sen = np.zeros_like(angulos)
y_sen = np.sin(angulos)
x_tan = np.cos(angulos)
y_tan = np.tan(angulos)

#Plotar o círculo
plt.figure(figsize=(15, 5))
plt.plot(x_circle, y_circle, label='Círculo')

#Plotar linha do Cosseno
plt.plot(x_cos, y_cos, label='Cosseno', linestyle='-')

#Plotar linha do Seno
plt.plot(x_sen, y_sen, label='Seno', linestyle='-')

#Plotar linha Tangente
plt.plot(x_tan[:400], y_tan[:400], label='Tangente', linestyle='-')


#Nome gráfico e Nome das Linhas
plt.title('Círculo trigonométrico')
plt.xlabel('x')
plt.ylabel('y')

#Setar proporção da tela
plt.gca().set_aspect('equal', adjustable='box')

#Mostrar Legenda
plt.legend()

#Mostrar linhas e círculo
plt.grid(True)
plt.show()
