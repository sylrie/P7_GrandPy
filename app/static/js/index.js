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
  
  //elt.innerHTML = ""
  //for (key in dict) {
    //alert(dict[key])
    
    //elt.innerHTML += dict[key] + "<br>"; 
  //}};
  elt.innerHTML = (
    "<p>" + papy_1 + "</p>" +
    "<p><strong>" + address + "</strong></p>" +
    "<p>" + papy_2 + "</p>" +
    "<p>" + story + "</p>" +
    "<p>" + fullurl + "</p>"
    );
};

valid.addEventListener("click", function() {
  var question = document.getElementById("question").value;
  alert(question)
  $.ajax({url: "/grandpy/" + question, success: grandpy});
});

