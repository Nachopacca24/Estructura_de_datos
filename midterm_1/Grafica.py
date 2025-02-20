import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Datos
x = [1000,2000,3000,4000,5000]#n
y = [0.04,0.06,0.08,0.10,0.12]#searche
a=[0.03,0.032,0.03,0.037,0.038]#pop

# Crear la gráfica
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Search")
plt.plot(x, a, marker='s', linestyle='-', color='r', label="Pop")
# Formatear el eje X para mostrar valores en millones
formatter = mticker.FuncFormatter(lambda x, _: f'{x/1_000_000:.0f}M')


# Etiquetas
plt.xlabel("Cantidad de instrucciones ")
plt.ylabel("Tiempo(segundos)")
plt.title("Gráfica de tiempo")
plt.legend()

# Mostrar la gráfica
plt.show()