var startPoint = [56.87333280052088, 60.492782592773445]
var map = L.map('map').setView(startPoint, 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var mark = L.marker(startPoint).addTo(map);

var lat = document.getElementById("id_lat")
lat.value = startPoint[0]
var lng = document.getElementById("id_long")
lng.value = startPoint[1]

function onMapClick(e) {
    mark
        .setLatLng(e.latlng)
    console.log(e)
    lat.value = e.latlng.lat
    lng.value = e.latlng.lng
}
map.on('click', onMapClick);
