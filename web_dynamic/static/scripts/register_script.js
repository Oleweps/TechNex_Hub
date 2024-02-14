// register_script.js

// Validate the registration form fields
function validateForm() {
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const contactDetails = document.getElementById('contact_details').value.trim();

    // Add your validation logic here
    if (username === '' || email === '' || password === '' || contactDetails === '') {
        alert('All fields are required');
        return false;
    }

    // You can add more validation checks based on your requirements

    return true;
}

// Submit the registration form asynchronously
function submitForm() {
    if (validateForm()) {
        const form = document.querySelector('form');
        const formData = new FormData(form);

        // Use Fetch API for asynchronous form submission
        fetch(form.getAttribute('action'), {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response, e.g., show success message, redirect, etc.
            console.log(data);
            if (data.redirect_url) {
                window.location.href = data.redirect_url;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
