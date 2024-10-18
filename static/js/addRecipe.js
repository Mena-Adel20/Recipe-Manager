 function addIngredient() {
            const ingredientsDiv = document.getElementById('ingredients');
            const newIngredientDiv = document.createElement('div');
            newIngredientDiv.classList.add('ingredient');
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

