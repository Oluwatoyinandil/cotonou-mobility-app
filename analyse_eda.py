import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Créer le dossier de sortie s'il n'existe pas
output_dir = 'outputs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Chargement des données
df = pd.read_csv('data_cotonou_mobility.csv')

# Configuration du style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 10))

# --- Graphique 1 : Distribution de la durée des trajets ---
plt.subplot(2, 2, 1)
sns.histplot(df['duree_min'], kde=True, color='blue')
plt.title('Distribution de la durée des trajets (min)')

# --- Graphique 2 : Impact de la météo sur la durée ---
plt.subplot(2, 2, 2)
sns.boxplot(x='meteo', y='duree_min', data=df)
plt.title('Impact de la météo sur le temps de trajet')

# --- Graphique 3 : Relation Heure / Indice de Trafic ---
plt.subplot(2, 2, 3)
sns.lineplot(x='heure_depart', y='indice_trafic', data=df, errorbar=None)
plt.axvspan(7, 9, color='red', alpha=0.1, label='Pointe Matin')
plt.axvspan(17, 19, color='red', alpha=0.1, label='Pointe Soir')
plt.title('Évolution du trafic selon l\'heure')
plt.legend()

# --- Graphique 4 : Sécurité par Moyen de Transport ---
plt.subplot(2, 2, 4)
sns.barplot(x='moyen_transport', y='prob_accident', hue='meteo', data=df)
plt.title('Risque d\'accident selon le transport et la météo')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'analyse_eda.png'), dpi=300, bbox_inches='tight')
print(f"Graphique sauvegardé dans '{output_dir}/analyse_eda.png'")