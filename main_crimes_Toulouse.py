import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Crimes_files/crimes_haute_garonne.csv", sep=";")

if 'Index' in data.columns:
    data = data.drop('Index', axis=1)

data_long = pd.melt(data, id_vars=["libellé index"], var_name="Date", value_name="Nombre de crimes")
data_long["Date"] = pd.to_datetime(data_long["Date"], format="_%Y_%m")
total_crimes_by_type = data_long.groupby("libellé index")["Nombre de crimes"].sum().sort_values(ascending=False)

###########################################
"""top_fives_crimes = total_crimes_by_type.head(5).index

flg, axes = plt.subplots(nrows=5, ncols=1, figsize=(10, 20), sharex=True)

for i, crime_type in enumerate(top_fives_crimes):
    data_type = data_long[data_long["libellé index"] == crime_type]
    data_grouped = data_type.groupby("Date")["Nombre de crimes"].sum()

    data_grouped.plot(kind="line",marker="o", ax=axes[i])
    axes[i].set_title(f'{crime_type}', fontsize=12)
    axes[i].set_ylabel("Nombre de crrimes / délits", fontsize=10)
    axes[i].grid(True)

plt.xlabel("Date", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()"""
###########################################
"""top_ten_crimes = total_crimes_by_type.head(10)
plt.figure(figsize=(10,8))
top_ten_crimes.plot(kind="bar",color="lightblue")
plt.title("Fréquence totale des crimes par type en Haute-Garonne")
plt.xlabel("Type de crime")
plt.ylabel("Nombre total de Crimes")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

for crime_type in top_ten_crimes.index:
    data_type = data_long[data_long["libellé index"] == crime_type]
    monthly_data = data_type.groupby(data_type["Date"]).sum()

    plt.figure(figsize=(10, 6))
    monthly_data['Nombre de crimes'].plot(kind='line', marker='o')
    plt.title(f'Tendance de {crime_type} par Mois en Haute-Garonne')
    plt.xlabel('Mois')
    plt.ylabel('Nombre de Crimes')
    plt.grid(True)
    plt.show()"""
##################################################################
top_ten_crimes = total_crimes_by_type.nlargest(10)
top_ten_crimes_data = data_long[data_long['libellé index'].isin(top_ten_crimes.index)]

print(top_ten_crimes_data)

crime_data_pivot = top_ten_crimes_data.pivot_table(index="Date", columns="libellé index",
                                                   values="Nombre de crimes",
                                                   aggfunc="sum")

"""monthly_changes = crime_data_pivot.pct_change()

correlation_matrix = monthly_changes.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Corrélation entre les Types de Crimes")
plt.show()

crimes_biens_personnes = monthly_changes[["Autres vols simples contre des particuliers dans deslocaux privés", "Vols à "
                                                                                                               "la "
                                                                                                               "tire"]]
correlation_biens_personnes = crimes_biens_personnes.corr()
print(correlation_biens_personnes)"""
####################################################################################

from statsmodels.tsa.arima.model import ARIMA
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

crime_data_total = crime_data_pivot.sum(axis=1)

crime_data_total.index = pd.DatetimeIndex(crime_data_total.index.values, freq="MS")

model = ARIMA(crime_data_total, order=(1, 1, 1))
fitted_model = model.fit()

forecast = fitted_model.forecast(steps=12)
plt.figure(figsize=(14, 7))
plt.plot(crime_data_total, label="Historique des crimes")
plt.plot(forecast, label="Prévision des crimes", color="red")
plt.title("Prévisions des taux de criminalité future")
plt.xlabel("Date")
plt.ylabel("Nombre de crimes")
plt.legend()
plt.show()
