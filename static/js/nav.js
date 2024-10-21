const recipesPage = document.getElementById("your-recipe");
const home = document.getElementById("home");
const use_recipe = document.getElementById("user-recipes");
const login = document.getElementById("log-in");
const signup = document.getElementById("sign-up");
const logout = document.getElementById("logout-button");

home.addEventListener("click", function () {
  window.location.href = "/";
});

use_recipe.addEventListener("click", function () {
  window.location.href = "/yourrecipes";
});

login.addEventListener("click", function () {
  window.location.href = "/login";
});
signup.addEventListener("click", function () {
  window.location.href = "/signup";
});

const userEmail = document.getElementById("user-email");
let localEmail = localStorage.getItem("email");

if (localEmail) {
  userEmail.textContent = "Welcome, " + localEmail;
  logout.style.display = "block";
  login.style.display = "none";
  signup.style.display = "none";
} else {
  userEmail.textContent = "";
  logout.style.display = "none";
  login.style.display = "block";
  signup.style.display = "block";
}

logout.addEventListener("click", function () {
  fetch("/logout", { method: "POST" }).then(() => {
    // After logging out, remove email form local storgae and  redirect to the login page
    localStorage.removeItem("email");
    window.location.href = "/";
  });
});
