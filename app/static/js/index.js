const valid = document.getElementById("user_request");

function grandpy(response) {
  
  let elt = document.getElementById("grandpy");
  let newP = elt.appendChild(document.createElement('p'));
  
  let papy_1 = response["papy_1"];
  let address = response["address"];
  let papy_2 = response["papy_2"];
  let story = response["story"];
  let fullurl = response["fullurl"];
  let lat = response["lat"];
  let lng = response["lng"];
  
  newP.innerHTML += papy_1;
  if (address != "") {
    elt.innerHTML += (
      "<p><strong>" + address + "</strong></p>"
    );
  }
  if (lat == "") {
    stopSearching();
  } else {
    initMap(lat, lng);
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
      "<p>Va demander à <a id='link' href=" + fullurl + " target=_blank>WikiPedia</a> si tu ne me crois pas!</p>"
    );
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
    "<a class='row justify-content-lg-center'><img src='../static/img/loader.gif' alt='error'/></a>"
  );
};

function stopSearching(){
  let elt = document.getElementById("map");
  elt.innerHTML = ("");
};

// 
valid.addEventListener("submit", function(evt) {
  
  // user request
  var question = document.getElementById("question").value;
  
  if (question.trim() != "") {
  
    //select element
    let elt = document.getElementById("grandpy");
    
    // display the question
    let user = elt.appendChild(document.createElement('p'));
    user.id = 'user';

    user.innerHTML += question;
    
    // reset form
    document.getElementById("question").value = "";

    // display searching img
    searching();
    // run search
    $.ajax({url: "/grandpy/" + question, success: grandpy});
  };
  evt.preventDefault();
});

