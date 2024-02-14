// Function to validate the login form
function validateLoginForm() {
    // Implement your form validation logic here
    // Return true if the form is valid, false otherwise
    return true;
}

// Function to submit the login form asynchronously
function submitLoginForm() {
    const form = document.querySelector('#login-form');
    const formData = new FormData(form);

    // Use Fetch API or XMLHttpRequest for asynchronous form submission
    fetch('/login', {  // Use the actual route instead of url_for
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response, e.g., show success message, redirect, etc.
        console.log(data);
        if (data.redirect_url) {
            window.location.href = data.redirect_url;
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Attach event listener to the login form
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('#login-form');
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Validate the form and submit it asynchronously
        if (validateLoginForm()) {
            submitLoginForm();
        }
    });
});
