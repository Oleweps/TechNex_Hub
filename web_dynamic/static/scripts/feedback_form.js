document.addEventListener('DOMContentLoaded', function() {
    const feedbackForm = document.getElementById('feedbackForm');

    feedbackForm.addEventListener('submit', function(event) {
        event.preventDefault();

        if (validateForm()) {
            const formData = new FormData(feedbackForm);

            // Use Fetch API or XMLHttpRequest for asynchronous form submission
            fetch('/feedback-form', {  // Replace with the actual route
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response, e.g., show success message, redirect, etc.
                console.log(data);
                if (data.success) {
                    // Redirect to the feedback success page or display a success message
                    window.location.href = '/feedback-success';  // Replace with the actual route
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    function validateForm() {
        // Get form elements
        const ratingInput = document.getElementById('ratings');
        const commentsInput = document.getElementById('comments');

        // Reset previous error messages
        resetErrorMessages();

        // Flag to track form validity
        let isValid = true;

        // Validate Rating (Example: must be between 1 and 5)
        if (parseInt(ratingInput.value) < 1 || parseInt(ratingInput.value) > 5) {
            displayErrorMessage(ratingInput, 'Rating must be between 1 and 5');
            isValid = false;
        }

        // Validate Comments (Example: must not be empty)
        if (commentsInput.value.trim() === '') {
            displayErrorMessage(commentsInput, 'Comments cannot be empty');
            isValid = false;
        }

        return isValid;
    }

    function resetErrorMessages() {
        // Reset error messages or styles if any
        // Example: remove error classes, hide error messages, etc.
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(element => element.remove());
    }

    function displayErrorMessage(element, message) {
        // Display error message next to the form element
        // Example: show an error message, add error classes, etc.
        const errorContainer = document.createElement('div');
        errorContainer.className = 'error-message';
        errorContainer.textContent = message;

        // Insert the error message after the form element
        element.parentNode.insertBefore(errorContainer, element.nextSibling);
    }
});
