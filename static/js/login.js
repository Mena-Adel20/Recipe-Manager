// Select form and inputs
const loginForm = document.getElementById("loginForm");
const loginEmail = document.getElementById("loginEmail");
const loginPassword = document.getElementById("loginPassword");

// Add event listener for form submission
loginForm.addEventListener("submit", (e) => {
    if (!validateLoginInputs()) {
        e.preventDefault(); // Prevent form submission if validation fails
    }

     
});

// Function to validate the login inputs
function validateLoginInputs() {
    let isValid = true; // Flag to track overall validity

    const emailValue = loginEmail.value.trim();
    const passwordValue = loginPassword.value.trim();

    // Validate email field
    if (emailValue === '') {
        setLoginError(loginEmail, "This field cannot be blank!");
        isValid = false;
    } else if (!isEmail(emailValue)) {
        setLoginError(loginEmail, "Check the email format!");
        isValid = false;
    } else {
        setLoginSuccess(loginEmail);
    }

    // Validate password field
    if (passwordValue === '') {
        setLoginError(loginPassword, "This field cannot be blank!");
        isValid = false;
    } else {
        setLoginSuccess(loginPassword);
    }

    return isValid; // Return the overall validity
}

// Function to set error message for login inputs
function setLoginError(input, msg) {
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");
    small.innerText = msg;
    formControl.className = "form-control error";
}

// Function to set success state for login inputs
function setLoginSuccess(input) {
    const formControl = input.parentElement;
    formControl.className = "form-control success";
}

// Email format validation function
function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}

const loginButton = document.getElementById("login");

  

loginButton.addEventListener("click", function() {
    const email = loginEmail.value; // Get the value of an input field with the id userEmail
    localStorage.setItem("email", email); // Save the email address in the browser's localStorage with the key "email"
    
});