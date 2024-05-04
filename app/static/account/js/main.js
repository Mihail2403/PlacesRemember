var startPoint = [56.87333280052088, 60.492782592773445]
var map = L.map('map').setView(startPoint, 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var remembersElement = document.getElementById("data")
var remembers = JSON.parse(data.attributes.getNamedItem("data-json").value)
for (var i = 0; i < remembers.length; i++){
    var marker = L.marker([remembers[i][3], remembers[i][4]])
    marker.addTo(map).bindPopup(`<span onclick="document.location='/remember/${remembers[i][0]}'">${remembers[i][1]}<br>-------------------------<br>${remembers[i][2]}</span>`);
    
}