import folium
from IPython.display import display

coordinates = [50.0755, 14.4378]
map = folium.Map(location=coordinates, zoom_start=10)

icon = folium.Icon(color='blue', icon='info-sign')
folium.Marker(location=coordinates, popup="Prague", icon = icon).add_to(map)

map.save("map.html")