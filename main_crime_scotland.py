import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("recorded-crime.csv", sep=",")

data = data[data["Reference Area"] != "Scotland"]

regional_crime_data = data.groupby("Reference Area").sum()
print(regional_crime_data)

#############################
non_sexual_violence = regional_crime_data['Crimes: Group 1: Murder and culpable homicide']

sorted_non_sexual_violence = non_sexual_violence.sort_values(ascending=False)

print(sorted_non_sexual_violence)

"""sorted_non_sexual_violence.plot(kind="bar", color="lightblue")
plt.title("Comparaison des crimes et homicide par ville")
plt.xlabel("Ville de référence")
plt.ylabel("Nombre de crimes")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

"""
#############################

"""selected_crimes = regional_crime_data[[
    "All Group 1: Non-sexual crimes of violence",
    "All Group 2: Sexual crimes",
    "All Group 3: Crimes of dishonesty"
]]"""

"""selected_crimes.plot(kind="bar", figsize=(14,7))
plt.title("Comparaison des diffférents types de crimes par ville")
plt.xlabel("Ville de référence")
plt.ylabel("Nombre de crimes")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
"""

############################

import seaborn as sns

"""selected_crimes = regional_crime_data[[
    "All Group 1: Non-sexual crimes of violence",
    "All Group 2: Sexual crimes",
    "All Group 3: Crimes of dishonesty",
    "All Group 4: Damage and reckless behaviour",
    "All Group 5: Crimes against society",
    "All Group 6: Antisocial offences",
    "All Group 7: Miscellaneous offences",
    "All Group 8: Road traffic offences"
]]

correlation_matrix = selected_crimes.corr()
print(correlation_matrix)

# Créer une carte de chaleur pour visualiser les corrélations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Corrélation entre différents types de crimes par région')
plt.show()
"""
############################
regional_crime_data_percent = regional_crime_data.div(regional_crime_data["All Crimes"], axis=0) * 100

selected_crimes = [
    "All Group 1: Non-sexual crimes of violence",
    "All Group 2: Sexual crimes",
    "All Group 3: Crimes of dishonesty",
    "All Group 4: Damage and reckless behaviour",
    "All Group 5: Crimes against society",
    "All Group 6: Antisocial offences",
    "All Group 7: Miscellaneous offences",
    "All Group 8: Road traffic offences"
]

regional_crime_data_percent[selected_crimes].plot(kind="bar", stacked=True, figsize=(14, 7))
plt.title('Pourcentage de différents types de crimes par région')
plt.xlabel('Région')
plt.ylabel('Pourcentage du total des crimes')
plt.legend(title='Type de crime')
plt.xticks(rotation=45)
plt.show()
