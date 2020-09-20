function getLocation() {
  if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          console.log(pos);
      });
    }
    else {
      console.error("Geolocation is not supported by this browser.");
    }
}
