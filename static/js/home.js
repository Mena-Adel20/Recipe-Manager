const categoryCard = document.getElementById("category-card");
const newRecipeCard = document.getElementById("addRecipe_card");
const filterCard = document.getElementById("filter-card");



// Redirect to category page when clicking on the element with id "categoryCard"
categoryCard.addEventListener("click", function() {
    window.location.href = "/category";
});

newRecipeCard.addEventListener("click", function() {
    window.location.href = "/addrecipe";
});


filterCard.addEventListener("click", function() {
    window.location.href = "/filter";
});
