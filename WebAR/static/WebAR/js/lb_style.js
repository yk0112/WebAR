var MyLatLng = new google.maps.LatLng(35.60599520185924, 139.68327270794447);
var Options = {
  zoom: 15,      //地図の縮尺値
  center: MyLatLng,    //地図の中心座標
  mapTypeId: 'roadmap'   //地図の種類
};

var map = new google.maps.Map(document.getElementById('map'), Options);  
var marker = new google.maps.Marker({ 
   position: MyLatLng, 
   map: map 
});

google.maps.event.addListener(map, 'click', event => clickListener(event, map));

function clickListener(event, map) {
 marker.setMap(null);
 const lat = event.latLng.lat();
 const lng = event.latLng.lng();
 document.getElementById('latitude').value = lat;
 document.getElementById('longitude').value = lng;
 MyLatLng = new google.maps.LatLng(lat, lng);
 marker = new google.maps.Marker({
  position: MyLatLng,
  map: map
 });
}
 
document.querySelector('#latitude').addEventListener('change', function(){
  marker.setMap(null);
   const lat = document.getElementById('latitude').value;
   const lng = document.getElementById('longitude').value;
   if (isNaN(lat) || isNaN(lng)) {
           alert("Enter the correct latitude and longitude values.");
           return;
   }
   MyLatLng = new google.maps.LatLng(lat, lng);
   map.setCenter(MyLatLng);
   marker = new google.maps.Marker({
   position: MyLatLng,
   map: map
});
})

document.querySelector('#longitude').addEventListener('change', function(){
  marker.setMap(null);
   const lat = document.getElementById('latitude').value;
   const lng = document.getElementById('longitude').value;
   if (isNaN(lat) || isNaN(lng)) {
           alert("Enter the correct latitude and longitude values.");
           return;
    }
   MyLatLng = new google.maps.LatLng(lat, lng);
   map.setCenter(MyLatLng);
   marker = new google.maps.Marker({
   position: MyLatLng,
   map: map
});
})

document.querySelector('#form-range').addEventListener('change', function () {
  var p = document.getElementById('form-range').value;
  document.getElementById('scale_value').textContent = p;
})