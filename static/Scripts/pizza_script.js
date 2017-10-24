//switch from main to login page

var indexClick = document.getElementsByClassName("pizza_image");
var orderClick = document.getElementsByClassName("pizza_image2");

function pizzaClick () {
  indexClick.onlick = location.href = "/login";
}

function pizzaOrder () {
  orderClick.onclick = location.href = "/finally";
}
