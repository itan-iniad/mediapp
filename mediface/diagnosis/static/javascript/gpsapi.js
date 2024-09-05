navigator.geolocation.getCurrentPosition(function (position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;

    // カスタムアイコン（赤色マーカー）の作成
    var redIcon = L.icon({
        iconUrl: 'https://maps.google.co.jp/mapfiles/ms/icons/red-dot.png', // 赤色アイコンのURL
        iconSize: [25, 41], // アイコンのサイズ
        iconAnchor: [12, 41], // アイコンのアンカー位置
        popupAnchor: [1, -34], // ポップアップの位置
        shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png', // 影のURL
        shadowSize: [41, 41] // 影のサイズ
    });

    // 現在地を中心に地図を再設定
    map.setView([lat, lon], 13);

    // 現在地にカスタムマーカーを追加
    var marker = L.marker([lat, lon], { icon: redIcon }).addTo(map);
    marker.bindPopup('現在地！').openPopup();

    // 現在地近くの病院を取得してマーカーを表示
    fetchHospitals(lat, lon, getRadiusFromZoom(map.getZoom()));
}, function(error) {
    console.error('Error with geolocation:', error);
}, {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
});

// マップのズームレベルが変更されたときのイベントハンドラ
map.on('zoomend', function() {
    var center = map.getCenter();
    var radius = getRadiusFromZoom(map.getZoom());
    fetchHospitals(center.lat, center.lng, radius);
});

// ズームレベルに基づいて検索範囲を決定する関数
function getRadiusFromZoom(zoomLevel) {
    return Math.min(5000 * (13 / zoomLevel), 50000); // 例: ズームレベル13で半径5km、ズームアウトするほど半径が大きくなる
}