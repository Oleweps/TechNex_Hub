document.addEventListener('DOMContentLoaded', function () {
    // Add an event listener for the logout form submission
    const logoutForm = document.getElementById('logoutForm');

    logoutForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // Get user ID and token from the form
        const userId = document.getElementById('user_id').value;
        const token = document.getElementById('token').value;

        // Perform AJAX request to the server for asynchronous logout
        fetch('/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId, token: token }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response, e.g., show success message, redirect, etc.
            console.log(data);
            // You can add further logic here based on the response
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
