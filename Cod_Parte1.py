import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta en Windows
file_path = r"C:\Users\Alejandro\OneDrive - Universidad de los Andes\10. Asistente_202520\Datos\Taller1\hotel_bookings_modified.csv"

# Cargar dataset
df = pd.read_csv(file_path)

# Selección de atributos importantes
important_cols = ["hotel", "is_canceled", "lead_time", "stays_in_weekend_nights", "stays_in_week_nights"]

plt.style.use("seaborn-v0_8")

for col in important_cols:
    plt.figure(figsize=(10, 6))
    
    if col in ["hotel", "is_canceled"]:
        # Gráfico de barras para categóricas/binarias
        ax = sns.countplot(data=df, x=col, order=df[col].value_counts().index, palette="viridis")
        plt.title(f"Distribución de {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        
        # Etiquetas de frecuencia encima de cada barra
        for container in ax.containers:
            ax.bar_label(container, fmt='%d', label_type='edge', padding=3)
    
    elif col == "lead_time":
        # Histograma para lead_time
        ax = sns.histplot(df[col], bins=30, kde=False, color="steelblue")
        plt.title("Distribución de lead_time")
        plt.xlabel("Días de anticipación")
        plt.ylabel("Frecuencia")
    
    else:
        # Filtrar los datos para excluir el valor 0 de las estancias
        df_filtered = df[df[col] > 0]
        
        # Gráfico de barras para los valores secuenciales de estancias
        ax = sns.countplot(data=df_filtered, x=col, palette="viridis")
        plt.title(f"Distribución de {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        plt.xticks(rotation=45)
        
        # Etiquetas encima de cada barra
        for container in ax.containers:
            ax.bar_label(container, fmt='%d', label_type='edge', padding=3)

    plt.tight_layout()
    plt.show()

# ============================
# Número total de cancelaciones
# ============================
total_cancellations = df[df["is_canceled"] == 1].shape[0]

print(f"Número total de cancelaciones: {total_cancellations}")