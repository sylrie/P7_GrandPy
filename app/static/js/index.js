const valid = $("#user_request")[0];
var count = 0;

function grandpy(response) {
  
  let elt = $("#grandpy")[0];
  
  let papy_1 = response["papy_1"];
  let address = response["address"];
  let papy_2 = response["papy_2"];
  let story = response["story"];
  let fullurl = response["fullurl"];
  let lat = response["lat"];
  let lng = response["lng"];
  
  SearchingGif('stop');

  var newP = elt.appendChild(document.createElement('p'));
  newP.innerHTML += papy_1;
  
  if (address != "") {
    var newP = elt.appendChild(document.createElement('p'));
    var strong = newP.appendChild(document.createElement('STRONG'));
    strong.setAttribute('class', 'text-warning')
    strong.innerHTML = address;
    
    count++;
    let map = elt.appendChild(document.createElement('div'));
    map.id = "map" + count;
    map.setAttribute('class', 'map col-lg-7 justify-content-lg-center my-1');
  
    if (lat != "") {
      initMap(lat, lng, map);
    };
  };
  
  if (papy_2 != "") {
    var newP = elt.appendChild(document.createElement('p'));
    newP.innerHTML += papy_2;
  };
  if (story != "") {
    var newP = elt.appendChild(document.createElement('p'));
    newP.innerHTML += story;
  };
  if (fullurl != "") {
    var newP = elt.appendChild(document.createElement('p'));
    newP.innerHTML += (
      "Va demander à <a id='link' href=" + fullurl + " target=_blank>WikiPedia</a> si tu ne me crois pas!"
    );
  };
window.scrollTo(0,document.body.scrollHeight);
};


function initMap(lat, lng, map) {
  var pos = {lat: lat, lng: lng};
  var map = new google.maps.Map(map , {
    zoom: 10,
    center: pos
  });
  var marker = new google.maps.Marker({
    position: pos,
    map: map
  });
};

function SearchingGif(action){
  let elt = $("#grandpy")[0];
  if (action == "start"){
    
    var newA = elt.appendChild(document.createElement('a'));
    newA.id ='searching';
    newA.setAttribute("class", "row justify-content-lg-center");

    var newImg = newA.appendChild(document.createElement('img'));
    newImg.src = '../static/img/loader.gif';
  } else {
    let gif = $("#searching")[0];
    elt.removeChild(gif);
  }
};

// 
valid.addEventListener("submit", function(evt) {
  
  // user request
  var question = $("#question")[0].value;
  
  if (question.trim() != "") {
  
    //select element
    let elt = $('#grandpy')[0];
    
    // display the question
    let user = elt.appendChild(document.createElement('p'));
    user.id = 'user';
    user.setAttribute('class', 'text-success text-right')
    user.innerHTML = question;

    // reset form
    $("#question")[0].value = "";

    // display searching img
    SearchingGif('start');
    // run search
    $.ajax({url: "/grandpy/" + question, success: grandpy});
  };
  evt.preventDefault();
  
});

