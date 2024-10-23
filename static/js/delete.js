document.addEventListener("DOMContentLoaded", function () {
  const deleteForms = document.querySelectorAll(
    // Select all forms with an action that starts with '/delete-recipe/'
    'form[action^="/delete-recipe/"]'
  );
  const modal = document.getElementById("deleteModal");
  const confirmDelete = document.getElementById("confirmDelete");
  const cancelDelete = document.getElementById("cancelDelete");
  // Variable to keep track of the form to be deleted
  let currentForm = null;

  deleteForms.forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      currentForm = form;
      modal.style.display = "block";
    });
  });

  confirmDelete.addEventListener("click", function () {
    if (currentForm) {
      // Submit the form if the user confirms deletion

      currentForm.submit();
    }
  });
  // When the "Cancel" button is clicked
  // Hide the delete confirmation modal
  cancelDelete.addEventListener("click", function () {
    modal.style.display = "none";
  });

  // Close modal if clicked outside of it
  window.addEventListener("click", function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });
});
