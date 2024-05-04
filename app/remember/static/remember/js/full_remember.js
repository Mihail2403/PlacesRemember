var remember = JSON.parse(document.getElementById("json-remember").attributes.getNamedItem("data-json").value)
var startPoint = [remember[0][3], remember[0][4]]
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

var title = document.getElementById("id_title")
title.value = remember[0][1]
var desc = document.getElementById("id_description")
desc.value = remember[0][2]
function onMapClick(e) {
    mark
        .setLatLng(e.latlng)
    console.log(e)
    lat.value = e.latlng.lat
    lng.value = e.latlng.lng
}
map.on('click', onMapClick);
