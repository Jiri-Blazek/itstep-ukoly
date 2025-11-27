from urllib import request
import json

json_path = (
    "C:/Users/blaze/OneDrive/Plocha/Programovani/PYTHON/36/pid_prodejni_mista.json"
)


def download_data():
    url = "https://data.pid.cz/pointsOfSale/json/pointsOfSale.json"

    with request.urlopen(url) as response:
        data = json.load(response)

    with open(
        json_path,
        mode="w",
        encoding="utf-8",
    ) as file:
        json.dump(data, file)


def read_data():
    with open(
        json_path,
        mode="r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


data = read_data()
print(data)


def generate_page(item):
    html = f"""
    <head>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
     integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
     crossorigin=""/>
     <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
     integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
     crossorigin=""></script> 
     <style>     
     #map {{ 
     height: 600px; 
     width: 600px"}}
     </style>
    </head>
        
    <h1>{item["name"]}</h1>
    <p><strong>Adresa: </strong>{item["address"]}</p>
    <p><strong>Typ: </strong>{item["type"]}</p>
    <p><strong>Oteviraci hodiny: </strong>{item["openingHours"]}</p>
    <p><strong>Id: </strong>{item[ "id"]}</p> 
    <h3>Zemepisna poloha:</h3>  
    <p>Zemepisna delka: {item["lat"]}</p>
    <p>Zemepisna sirka: {item["lon"]}</p>
    <div id="{item[ "id"]}";></div>
    <script>
   
        const map = L.map("{item[ "id"]}").setView([{item["lat"]},{item["lon"]}], 13);

        const tiles = L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }}).addTo(map);
        var marker = L.marker([{item["lat"]},{item["lon"]}]).addTo(map);
     </script>
    """
    with open(
        f'C:/Users/blaze/OneDrive/Plocha/Programovani/PYTHON/36/html-pages/xyz_{item["id"]}.html',
        mode="w",
        encoding="utf-8",
    ) as file:
        file.write(html)


def generate():
    data = read_data()

    for item in data:
        generate_page(item)


# generate()
generate_page(
    {
        "id": "dp2",
        "type": "ticketMachine",
        "name": "Grand Hotel International",
        "address": "Koulova 1501/15, Dejvice, Praha 6",
        "openingHours": [{"from": 0, "to": 6, "hours": "5:00-24:00"}],
        "lat": 50.1093445,
        "lon": 14.3935671,
        "services": 196608,
        "payMethods": 1,
    },
)
# pridat leaflet
# pridat css
