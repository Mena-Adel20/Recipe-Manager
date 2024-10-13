const categoryCard = document.getElementById("category-card");
const newRecipeCard = document.getElementById("addRecipe_card");



// Redirect to category page when clicking on the element with id "categoryCard"
categoryCard.addEventListener("click", function() {
    window.location.href = "/category";
});

newRecipeCard.addEventListener("click", function() {
    window.location.href = "/addrecipe";
});
