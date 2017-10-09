//switch from main to login page

var pizzaImage = document.getElementsByClassName("pizza_image");
function pizzaClick () {
   pizzaImage.onlick = location.href = "login";
 }

var pizzaSignUpBtn = document.getElementsByClassName("btn-default");
function pizzaSignUpClick () {
  pizzaSignUpBtn.onlick = location.href = "signup";
}
