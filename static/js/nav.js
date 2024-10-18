
const recipesPage =document.getElementById("your-recipe");
const home = document.getElementById("home");
const use_recipe = document.getElementById("user-recipes")


home.addEventListener("click", function() {
    window.location.href = "/home";


});


use_recipe.addEventListener("click", function() {
    window.location.href = "/yourrecipes";


});


const userEmail = document.getElementById("user-email"); 
let localEmail = localStorage.getItem("email"); 
if (localEmail) {
    userEmail.textContent = "Welcome, " + localEmail; 
} else {
    userEmail.textContent = "No email found"; 
}


const logout = document.getElementById("logout-button");

logout.addEventListener("click", function() {
    fetch("/logout", { method: "POST" })
        .then(() => {
            // After logging out, remove email form local storgae and  redirect to the login page
              localStorage.removeItem('email');
            window.location.href = "/";
        })
});




