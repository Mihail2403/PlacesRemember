var lat = document.getElementById("lat-val").innerText
var lon = document.getElementById("lon-val").innerText

var map = L.map('map').setView([lat, lon], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var mark = L.marker([lat, lon]).addTo(map);


