var url = $('#url').html();

function emergency() {

  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        var link = url + 'sms/' + pos.lat + '/' + pos.lng;
        window.open( link, '_self' );
    });
  }

  else {
    console.error("Geolocation is not supported by this browser.");
  }

}
