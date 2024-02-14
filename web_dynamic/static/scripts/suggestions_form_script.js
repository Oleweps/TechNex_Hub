// static/js/suggestions_form_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Submit Suggestion" button
    var submitButton = document.querySelector('.submit-suggestion-btn');
    submitButton.addEventListener('click', function (event) {
        // Prevent the default form submission
        event.preventDefault();

        // Perform client-side validation
        if (validateForm()) {
            // Use Fetch API or XMLHttpRequest for asynchronous suggestion submission
            fetch('/suggestions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams(new FormData(document.getElementById('suggestionForm'))),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the JSON response (e.g., show a success message)
                console.log(data.message);
            })
            .catch(error => {
                console.error('Error submitting suggestion:', error);
            });
        }
    });

    // Function to perform client-side validation
    function validateForm() {
        // Get form elements
        var titleInput = document.getElementById('title');
        var categorySelect = document.getElementById('category');
        var contentInput = document.getElementById('content');

        // Reset previous error messages
        titleInput.classList.remove('is-invalid');
        categorySelect.classList.remove('is-invalid');
        contentInput.classList.remove('is-invalid');

        // Check if title is empty
        if (titleInput.value.trim() === '') {
            titleInput.classList.add('is-invalid');
            alert('Please enter a title.');
            return false;
        }

        // Check if category is selected
        if (categorySelect.value === '') {
            categorySelect.classList.add('is-invalid');
            alert('Please select a category.');
            return false;
        }

        // Check if content is empty
        if (contentInput.value.trim() === '') {
            contentInput.classList.add('is-invalid');
            alert('Please enter content for your suggestion.');
            return false;
        }

        // Validation passed
        return true;
    }
});
