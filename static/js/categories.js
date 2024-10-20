const categoryItem = document.querySelectorAll(".category-card");

categoryItem.forEach(function (item) {
  item.addEventListener("click", function () {
    // Get the data-id attribute value from the clicked item
    const categoryName = item.dataset.id;
    // Redirect the user to the recipe details page .
    window.location.href = "/home/" + categoryName;
  });
});

const recipeItems = document.querySelectorAll(".recipe-list-card");

recipeItems.forEach(function (item) {
  item.addEventListener("click", function () {
    // Get the data-id attribute value from the clicked item
    const recipeId = item.dataset.id;
    // Redirect the user to the recipe details page
    window.location.href = `/recipe-details/${recipeId}`;
  });
});

const newRecipeCard = document.getElementById("addRecipe_card");
newRecipeCard.addEventListener("click", function () {
  window.location.href = "/addrecipe";
});

const filterCard = document.getElementById("filter-card");
filterCard.addEventListener("click", function () {
  window.location.href = "/filter";
});
