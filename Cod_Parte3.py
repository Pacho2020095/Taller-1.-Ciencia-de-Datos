import pandas as pd
import matplotlib.pyplot as plt

# ============================
# Cargar dataset (Carga única)
# ============================
file_path = r"C:\Users\Alejandro\OneDrive - Universidad de los Andes\10. Asistente_202520\Datos\Taller1\hotel_bookings_modified.csv"
df = pd.read_csv(file_path)

# ============================
# Análisis 1: Cancelaciones en City Hotel
# ============================
city_cancellations = df[(df["hotel"] == "City Hotel") & (df["is_canceled"] == 1)].copy()

# 1.1: Cancelaciones por tipo de cliente
city_cancellations.loc[:, "client_group"] = city_cancellations["customer_type"].apply(
    lambda x: "Transient" if x == "Transient" else "Otros"
)
cancel_counts_client = city_cancellations["client_group"].value_counts()
print("Análisis 1.1: Cancelaciones en City Hotel por tipo de cliente")
print(cancel_counts_client)

# Gráfico 1.1
plt.figure(figsize=(6, 6))
ax1 = cancel_counts_client.plot(kind="bar", color=["teal", "orange"])
plt.title("Cancelaciones en City Hotel por tipo de cliente")
plt.ylabel("Número de cancelaciones")
plt.xlabel("Tipo de cliente")
plt.xticks(rotation=0)
for container in ax1.containers:
    ax1.bar_label(container, fmt="%d", label_type='edge', padding=3)
plt.tight_layout()
plt.show()

# 1.2: Cancelaciones entre semana vs. fin de semana
cancel_week = (city_cancellations["stays_in_week_nights"] > 0).sum()
cancel_weekend = (city_cancellations["stays_in_weekend_nights"] > 0).sum()
cancel_data = pd.Series({"Entre semana": cancel_week, "Fin de semana": cancel_weekend})
print("\nAnálisis 1.2: Comparación de cancelaciones por tipo de noche")
print(cancel_data)

# Gráfico 1.2
plt.figure(figsize=(6, 6))
ax2 = cancel_data.plot(kind="bar", color=["steelblue", "orange"])
plt.title("Cancelaciones en City Hotel\nComparación entre semana vs fin de semana")
plt.ylabel("Número de cancelaciones")
plt.xticks(rotation=0)
for container in ax2.containers:
    ax2.bar_label(container, fmt="%d", label_type='edge', padding=3)
plt.tight_layout()
plt.show()

# ============================
# Análisis 2: Cancelaciones de clientes Transient
# ============================
transient_cancellations = df[(df["customer_type"] == "Transient") & (df["is_canceled"] == 1)].copy()

# 2.1: Cancelaciones Transient entre semana
transient_week_counts = transient_cancellations[transient_cancellations["stays_in_week_nights"] > 0]["stays_in_week_nights"].value_counts().sort_index()
print("\nAnálisis 2.1: Cancelaciones de clientes Transient (Noches entre semana)")
print(transient_week_counts)

# Gráfico 2.1
plt.figure(figsize=(8, 6))
ax3 = transient_week_counts.plot(kind="bar", color="steelblue")
plt.title("Cancelaciones Transient\n(Noches entre semana)")
plt.xlabel("Número de noches entre semana")
plt.ylabel("Número de cancelaciones")
plt.xticks(rotation=0)
for container in ax3.containers:
    ax3.bar_label(container, fmt="%d", label_type='edge', padding=3)
plt.tight_layout()
plt.show()

# 2.2: Cancelaciones Transient fin de semana
transient_weekend_counts = transient_cancellations[transient_cancellations["stays_in_weekend_nights"] > 0]["stays_in_weekend_nights"].value_counts().sort_index()
print("\nAnálisis 2.2: Cancelaciones de clientes Transient (Noches fin de semana)")
print(transient_weekend_counts)

# Gráfico 2.2
plt.figure(figsize=(8, 6))
ax4 = transient_weekend_counts.plot(kind="bar", color="orange")
plt.title("Cancelaciones Transient\n(Noches fin de semana)")
plt.xlabel("Número de noches fin de semana")
plt.ylabel("Número de cancelaciones")
plt.xticks(rotation=0)
for container in ax4.containers:
    ax4.bar_label(container, fmt="%d", label_type='edge', padding=3)
plt.tight_layout()
plt.show()