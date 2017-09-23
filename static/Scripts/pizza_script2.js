//switch from main to login page

var indexClick = document.getElementsByClassName("pizza_image");

function pizzaClick () {
  indexClick.onlick = location.href = "login";
} 

var signClick = document.getElementsByClassName("btn-default");

function signupClick () {
  signClick.onlick = location.href = "signup";
} 