import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Configuration de la page
st.set_page_config(page_title="Mobilité Cotonou SmartCity", layout="wide")

# 1. Chargement des ressources
@st.cache_resource
def load_assets():
    model_duree = joblib.load('model_duree.pkl')
    model_risque = joblib.load('model_risque.pkl')
    gdf = gpd.read_file("cotonou_points.geojson")
    return model_duree, model_risque, gdf

model_t, model_r, gdf_c = load_assets()

# 2. Interface utilisateur (Sidebar)
st.sidebar.header("📍 Paramètres du Trajet")
point_a = st.sidebar.selectbox("Point de départ", gdf_c['Quartier'].unique())
point_b = st.sidebar.selectbox("Destination", gdf_c['Quartier'].unique())
heure = st.sidebar.slider("Heure de départ", 0, 23, 8)
meteo = st.sidebar.selectbox("Météo", ['Ensoleillé', 'Pluie Légère', 'Forte Pluie'])
jour = st.sidebar.radio("Type de jour", ['Semaine', 'Weekend'])

# 3. Logique de Prédiction
def obtenir_predictions(pA, pB, h, met, j):
    # Simulation d'un calcul de distance simplifié pour le modèle
    dist_estimee = 7.5 # En situation réelle, calculé via GeoPandas
    trafic_estime = 2.5 if (7 <= h <= 9 or 17 <= h <= 19) else 1.2
    
    results = []
    for transport in ['Zem', 'Voiture', 'Bus']:
        input_data = pd.DataFrame({
            'point_A': [pA], 'point_B': [pB], 'heure_depart': [h],
            'jour_semaine': [j], 'meteo': [met], 'moyen_transport': [transport],
            'distance_km': [dist_estimee], 'indice_trafic': [trafic_estime]
        })
        duree = model_t.predict(input_data)[0]
        risque = model_r.predict(input_data)[0]
        results.append({'mode': transport, 'temps': duree, 'risque': risque})
    return results

# 4. Affichage des Résultats
st.title("🚖 Assistant de Mobilité Intelligente - Cotonou")

if point_a == point_b:
    st.warning("Veuillez choisir un point de départ et d'arrivée différents.")
else:
    res = obtenir_predictions(point_a, point_b, heure, meteo, jour)
    
    col1, col2, col3 = st.columns(3)
    for i, r in enumerate(res):
        with [col1, col2, col3][i]:
            st.metric(label=f"⏳ {r['mode']}", value=f"{int(r['temps'])} min")
            st.caption(f"Risque d'accident : {round(r['risque']*100, 1)}%")

    # 5. Carte Folium
    st.subheader("🗺️ Itinéraire suggéré")
    coords_a = gdf_c[gdf_c['Quartier'] == point_a].geometry.values[0]
    coords_b = gdf_c[gdf_c['Quartier'] == point_b].geometry.values[0]
    
    m = folium.Map(location=[6.365, 2.418], zoom_start=13, tiles="cartodbpositron")
    folium.Marker([coords_a.y, coords_a.x], popup=point_a, icon=folium.Icon(color='green')).add_to(m)
    folium.Marker([coords_b.y, coords_b.x], popup=point_b, icon=folium.Icon(color='red')).add_to(m)
    folium.PolyLine([[coords_a.y, coords_a.x], [coords_b.y, coords_b.x]], color="blue", weight=2.5).add_to(m)
    
    st_folium(m, width=900, height=450)