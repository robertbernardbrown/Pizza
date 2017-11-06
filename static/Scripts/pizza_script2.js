//switch from main to login page

var pizzaObj = document.getElementsByClassName("pizza_image");

console.log(pizzaObj);

document.addEventListener("click", pizzaClick (){
   console.log("hi");
})

var pizzaSignUpBtn = document.getElementsByClassName("btn-default");
function pizzaSignUpClick () {
  pizzaSignUpBtn.onlick = location.href = "signup";
}
