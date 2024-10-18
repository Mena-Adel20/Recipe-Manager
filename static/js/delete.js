document.addEventListener("DOMContentLoaded", function () {
  const deleteForms = document.querySelectorAll(
    'form[action^="/delete-recipe/"]'
  );
  const modal = document.getElementById("deleteModal");
  const confirmDelete = document.getElementById("confirmDelete");
  const cancelDelete = document.getElementById("cancelDelete");
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
      currentForm.submit();
    }
  });

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
