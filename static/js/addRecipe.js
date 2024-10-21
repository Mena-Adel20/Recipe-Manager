function addIngredient() {
  const ingredientsDiv = document.getElementById("ingredients");
  const newIngredientDiv = document.createElement("div");
  newIngredientDiv.classList.add("ingredient");
  newIngredientDiv.innerHTML = `
                <input type="text" name="ingredientName[]" placeholder="Ingredient Name" required>
                <input type="text" name="ingredientMeasurement[]" placeholder="Measurement" required>
                <button type="button" onclick="removeIngredient(this)">Remove</button>
            `;
  ingredientsDiv.appendChild(newIngredientDiv);
}

function removeIngredient(button) {
  button.parentNode.remove();
}
if (!localStorage.getItem("last_id")) {
  localStorage.setItem("last_id", "34036");
}

document
  .getElementById("recipeForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission for now
    // Increment and save ID
    let currentId = parseInt(localStorage.getItem("last_id"));
    let newId = currentId + 1;
    localStorage.setItem("last_id", newId.toString());

    // Set the ID in form
    document.getElementById("recipe_id").value = newId;

    // Show the modal box
    const modal = document.getElementById("submissionModal");
    modal.style.display = "block";

    // Handle the "OK" button click
    document.getElementById("okButton").addEventListener("click", function () {
      modal.style.display = "none";
      window.location.href = "/home"; // Redirect to home page after closing the modal

      // After closing the modal, submit the form programmatically
      document.getElementById("recipeForm").submit();
    });
  });
