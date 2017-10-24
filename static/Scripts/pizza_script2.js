//switch from main to login page

var aThing = document.getElementsByClassName("pizza_image");

console.log(aThing);

document.addEventListener("click", pizzaClick (){
   console.log("hi");
})

var pizzaSignUpBtn = document.getElementsByClassName("btn-default");
function pizzaSignUpClick () {
  pizzaSignUpBtn.onlick = location.href = "signup";
}
