document.getElementById('filter-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const selectedCuisines = Array.from(document.querySelectorAll('input[name="cuisine"]:checked')).map(checkbox => checkbox.value);
    const selectedTimes = Array.from(document.querySelectorAll('input[name="time"]:checked')).map(checkbox => checkbox.value);

    const params = new URLSearchParams();
    selectedCuisines.forEach(cuisine => params.append('cuisine', cuisine));
    selectedTimes.forEach(time => params.append('time', time));

    // Redirect to the /filter route with the query parameters
    window.location.href = `/filter?${params.toString()}`;
});
