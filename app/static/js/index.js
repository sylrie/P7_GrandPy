const valid = document.getElementById("valid");

function grandpy(response) {
  let elt = document.getElementById("grandpy");
  let papy_1 = response["papy_1"];
  let address = response["address"];
  let papy_2 = response["papy_2"];
  let story = response["story"];
  let fullurl = response["fullurl"];
  let lat = response["lat"];
  let lng = response["lng"];
  
  elt.innerHTML += (
    "<p><br>" + papy_1 + "</p>"
    );
  if (address != "") {
    elt.innerHTML += (
      "<p><strong>" + address + "</strong></p>"
    );
  }
  if (papy_2 != "") {
    elt.innerHTML += (
      "<p>" + papy_2 + "</p>"
    );
  }
  if (story != "") {
    elt.innerHTML += (
      "<p>" + story + "</p>"
    );
  }
  if (fullurl != "") {
    elt.innerHTML += (
      "<p><a id='link' href=" + fullurl + " target=_blank>Tu veux en savoir plus ?</a></p>"
    );
  }
  if (lat == "") {
    stopSearching();
  } else {
    initMap(lat, lng);
  }
};

function initMap(lat, lng) {

  var pos = {lat: lat, lng: lng};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: pos
  });
  var marker = new google.maps.Marker({
    position: pos,
    map: map
  });
};

function searching(){
  let elt = document.getElementById("map");
  elt.innerHTML = (
    "<a id='searching'><img src='../static/img/searching.gif' alt='error'/></a>"
  );
};

function stopSearching(){
  let elt = document.getElementById("map");
  elt.innerHTML = ("");
};

// 
valid.addEventListener("click", function() {
  
  // user request
  var question = document.getElementById("question").value;
  
  //select element
  let elt = document.getElementById("grandpy");
  
  // display the question
  elt.innerHTML = (
    "<p id=user>" + question + "</p>"
    );

  // reset form
  document.getElementById("question").value = "";

  // display searching img
  searching();

  // run search
  $.ajax({url: "/grandpy/" + question, success: grandpy});
});

