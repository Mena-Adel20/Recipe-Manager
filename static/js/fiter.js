document
  .getElementById("filter-form")
  .addEventListener("submit", function (event) {
    // Prevents the default behavior of the form submission (i.e., stops the form from submitting and refreshing the page)
    event.preventDefault();
    // Get all the checkboxes with the name "time" that are checked, convert the NodeList to an array,
    // and then create an array of their values
    const selectedCuisines = Array.from(
      document.querySelectorAll('input[name="cuisine"]:checked')
    ).map((checkbox) => checkbox.value);

    const selectedTimes = Array.from(
      document.querySelectorAll('input[name="time"]:checked')
    ).map((checkbox) => checkbox.value);
    // Create an object to hold URL query parameters
    const params = new URLSearchParams();

    // Append each selected cuisine as a separate query parameter to the URL
    selectedCuisines.forEach((cuisine) => params.append("cuisine", cuisine));

    // Append each selected time as a separate query parameter to the URL
    selectedTimes.forEach((time) => params.append("time", time));

    // Redirect to the /filter route with the query parameters
    window.location.href = `/filter?${params.toString()}`;
  });
