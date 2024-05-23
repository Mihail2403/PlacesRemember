var startPoint = [56.87333280052088, 60.492782592773445]
var map = L.map('map').setView(startPoint, 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var remembersElement = document.getElementById("data")
var remembers = JSON.parse(data.attributes.getNamedItem("data-json").value)
console.log(remembers)

for (var i = 0; i < remembers.length; i++){
    var rem = remembers[i].fields
    var marker = L.marker([rem.lat, rem.long])
    marker.addTo(map).bindPopup(`<span onclick="document.location='/remember/${remembers[i].pk}'">${rem.title}<br>-------------------------<br>${rem.description}</span>`);
}