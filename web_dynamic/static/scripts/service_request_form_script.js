// register_script.js

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('service-request-form').addEventListener('submit', function (event) {
        event.preventDefault();
        if (validateServiceRequestForm()) {
            // Use Fetch API for asynchronous form submission
            const form = document.querySelector('#service-request-form');
            const formData = new FormData(form);

            fetch('/service_request_form', {  // Update the URL to the actual endpoint
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response, e.g., show success message, redirect, etc.
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    // Function to validate the service request form
    function validateServiceRequestForm() {
        // Add your validation logic here
        // Return true if the form is valid, false otherwise
        return true;
    }
});
