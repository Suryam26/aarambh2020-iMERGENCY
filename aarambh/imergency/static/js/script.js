var url = $('#url').html();
var name = '';
var phn1 = '';
var phn2 = '';
var phn3 = '';


if (localStorage.getItem("i_Name")) {
  $("#name").attr("value", localStorage.getItem("i_Name"));
}

if (localStorage.getItem("i_phn1")) {
  $("#phone1").attr("value", localStorage.getItem("i_phn1"));
}

if (localStorage.getItem("i_phn2")) {
  $("#phone2").attr("value", localStorage.getItem("i_phn2"));
}

if (localStorage.getItem("i_phn3")) {
  $("#phone3").attr("value", localStorage.getItem("i_phn3"));
}


function save() {
  if (typeof(Storage) !== "undefined") {
    name = $("#name").val();
    phn1 = $("#phone1").val();
    phn2 = $("#phone2").val();
    phn3 = $("#phone3").val();
    localStorage.setItem("i_Name", name);
    localStorage.setItem("i_phn1", phn1);
    localStorage.setItem("i_phn2", phn2);
    localStorage.setItem("i_phn3", phn3);
  }
  else {
    document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
  }
}


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
