
const recipesPage =document.getElementById("your-recipe");
const home = document.getElementById("home");
const use_recipe = document.getElementById("user-recipes")


home.addEventListener("click", function() {
    window.location.href = "/home";


});


use_recipe.addEventListener("click", function() {
    window.location.href = "/yourrecipes";


});
