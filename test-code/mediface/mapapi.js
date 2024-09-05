function fetchHospitals(lat, lon, radius) {
    var query = `[out:json];
        (
            node["amenity"="doctors"](around:${radius},${lat},${lon});
            node["amenity"="clinic"](around:${radius},${lat},${lon});
            node["amenity"="hospital"](around:${radius},${lat},${lon});
        );
        out;`;
    var overpassUrl = 'https://overpass-api.de/api/interpreter?data=' + encodeURIComponent(query);

    fetch(overpassUrl)
        .then(response => response.json())
        .then(data => {
            // 既存のマーカーを全てクリア
            clearMarkers();

            // 病院データの処理
            data.elements.forEach(hospital => {
                var marker = L.marker([hospital.lat, hospital.lon]).addTo(map);
                marker.bindPopup(`<b>${hospital.tags.name || 'Unknown Hospital'}</b>`);
                markers.push(marker);
            });
        })
        .catch(error => console.error('Error fetching hospital data:', error));
}

// 既存のマーカーを格納するリスト
var markers = [];

// マーカーをクリアする関数
function clearMarkers() {
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];
}