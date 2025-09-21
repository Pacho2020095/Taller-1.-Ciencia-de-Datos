import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Cargar dataset
# ============================

file_path = r"C:\Users\Alejandro\OneDrive - Universidad de los Andes\10. Asistente_202520\Datos\Taller1\hotel_bookings_modified.csv"
df = pd.read_csv(file_path)

# ============================
# 1. Pie chart - Cancelaciones por tipo de hotel
# ============================

cancel_rate_hotel = df.groupby("hotel")["is_canceled"].mean()

plt.figure(figsize=(6,6))
plt.pie(cancel_rate_hotel, 
        labels=cancel_rate_hotel.index, 
        autopct="%1.1f%%", 
        startangle=90, 
        colors=["#66b3ff","#99ff99"],
        wedgeprops={"edgecolor":"black"})
plt.title("Proporción de cancelaciones por tipo de hotel")
plt.show()

# ============================
# 2. Pie chart - Cancelaciones por tipo de cliente
# ============================

cancel_rate_client = df.groupby("customer_type")["is_canceled"].mean()

plt.figure(figsize=(7,7))
plt.pie(cancel_rate_client, 
        labels=cancel_rate_client.index, 
        autopct="%1.1f%%", 
        startangle=90, 
        colors=["#ff9999","#66b3ff","#99ff99","#ffcc99"],
        wedgeprops={"edgecolor":"black"})
plt.title("Proporción de cancelaciones por tipo de cliente")
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# ============================
# Cargar dataset
# ============================
file_path = r"C:\Users\Alejandro\OneDrive - Universidad de los Andes\10. Asistente_202520\Datos\Taller1\hotel_bookings_modified.csv"
df = pd.read_csv(file_path)

# ============================
# Filtrar stays_in_week_nights > 0
# ============================
df_filtered = df[df["stays_in_week_nights"] != 0]

import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Cargar dataset
# ============================

file_path = r"C:\Users\Alejandro\OneDrive - Universidad de los Andes\10. Asistente_202520\Datos\Taller1\hotel_bookings_modified.csv"
df = pd.read_csv(file_path)

import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Cargar dataset
# ============================

file_path = r"C:\Users\Alejandro\OneDrive - Universidad de los Andes\10. Asistente_202520\Datos\Taller1\hotel_bookings_modified.csv"
df = pd.read_csv(file_path)

# ============================
# Cancelaciones vs stays_in_week_nights
# ============================

# Filtrar los datos para excluir las estancias de 0 noches entre semana
df_filtered = df[df['stays_in_week_nights'] > 0]

# Calcular la tasa de cancelación con los datos filtrados
cancel_rate_stays = df_filtered.groupby("stays_in_week_nights")["is_canceled"].mean()

plt.figure(figsize=(10,6))

# Aumentar el espacio entre las barras reduciendo el ancho (width) de las mismas
ax = cancel_rate_stays.plot(kind="bar", color="steelblue", width=0.7)

plt.title("Proporción de cancelaciones según noches entre semana reservadas")
plt.xlabel("Número de noches entre semana")
plt.ylabel("Proporción de cancelaciones")

# Etiquetas encima de cada barra con dos cifras significativas
for i, bar in enumerate(ax.patches):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{height:.2f}", 
            ha='center', va='bottom', fontsize=9)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ============================
# Gráfico de Cancelaciones vs Noches de fin de semana
# ============================

# Filtrar los datos para excluir las estancias de 0 noches de fin de semana
df_filtered = df[df['stays_in_weekend_nights'] > 0]

# Calcular la tasa de cancelación (promedio de is_canceled) por número de noches de fin de semana
cancel_rate_stays_weekend = df_filtered.groupby("stays_in_weekend_nights")["is_canceled"].mean()

# Crear la figura y el eje del gráfico
plt.figure(figsize=(10,6))

# Aumentar el espacio entre las barras reduciendo su ancho
ax = cancel_rate_stays_weekend.plot(kind="bar", color="forestgreen", width=0.7)

# Configurar títulos y etiquetas
plt.title("Proporción de cancelaciones según noches de fin de semana reservadas")
plt.xlabel("Número de noches de fin de semana")
plt.ylabel("Proporción de cancelaciones")

# Etiquetas encima de cada barra con dos cifras significativas
for bar in ax.patches:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2, 
        height + 0.01, 
        f"{height:.2f}", 
        ha='center', 
        va='bottom', 
        fontsize=9
    )

# Rotar las etiquetas del eje X para mayor legibilidad y ajustar el layout
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()