const form = document.getElementById("form");
const username = document.getElementById("username");
const email = document.getElementById("email");
const password = document.getElementById("password");
const confirm = document.getElementById("confirm");

form.addEventListener("submit", (e) => {
    if (!checkInputs()) {
        e.preventDefault(); // Prevent form submission if validation fails
    }
});

function checkInputs() {
    let isValid = true; // Flag to track overall validity

    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const confirmValue = confirm.value.trim();

    if (usernameValue === '') {
        setError(username, "This field cannot be blank!");
        isValid = false; // Mark as invalid
    } else {
        setSuccess(username);
    }

    if (emailValue === '') {
        setError(email, "This field cannot be blank!");
        isValid = false;
    } else if (!isEmail(emailValue)) {
        setError(email, "Check the email format!");
        isValid = false;
    } else {
        setSuccess(email);
    }

    if (passwordValue === '') {
        setError(password, "This field cannot be blank!");
        isValid = false;
    } else if (passwordValue.length < 6) {
        setError(password, "Password is too small!");
        isValid = false;
    } else {
        setSuccess(password);
    }

    if (confirmValue === '') {
        setError(confirm, "This field cannot be blank!");
        isValid = false;
    } else if (passwordValue !== confirmValue) {
        setError(confirm, "Passwords do not match!");
        isValid = false;
    } else {
        setSuccess(confirm);
    }

    return isValid; // Return the overall validity
}

function setError(input, msg) {
    const formControl = input.parentElement;
    const small = formControl.querySelector("small");
    small.innerText = msg;
    formControl.className = "form-control error";
}

function setSuccess(input) {
    const formControl = input.parentElement;
    formControl.className = "form-control success";
}

function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
