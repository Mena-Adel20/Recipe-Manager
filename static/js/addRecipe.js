function addIngredient() {
  const ingredientsDiv = document.getElementById("ingredients");
  const newIngredientDiv = document.createElement("div");
  newIngredientDiv.classList.add("ingredient");
  newIngredientDiv.innerHTML = `
                <input type="text" name="ingredientName[]" placeholder="Ingredient Name" required>
                <input type="text" name="ingredientMeasurement[]" placeholder="Measurement" required>
                <button type="button" onclick="removeIngredient(this)">Remove</button>
            `;
  // Append the new ingredient div to the main container
  ingredientsDiv.appendChild(newIngredientDiv);
}

function removeIngredient(button) {
  // Remove the parent div of the clicked remove button

  button.parentNode.remove();
}
// Check if 'last_id' is already in local storage, if not, set the initial value
if (!localStorage.getItem("last_id")) {
  localStorage.setItem("last_id", "34042"); // Initialize 'last_id' with a starting value of 34042 the last id of static recipes in json
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
      window.location.href = "/"; // Redirect to home page after closing the modal box

      // After closing the modal, submit the form programmatically
      document.getElementById("recipeForm").submit();
    });
  });
