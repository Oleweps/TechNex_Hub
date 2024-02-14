// static/js/services_marketplace_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to all "Select Service" buttons
    var selectButtons = document.querySelectorAll('.select-service-btn');
    
    selectButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Retrieve the service ID from the button's data attribute
            var serviceId = button.getAttribute('data-service-id');

            // You can now perform some action with the serviceId, for example,
            // make an AJAX request to request the service
            requestService(serviceId);
        });
    });

    function requestService(serviceId) {
        // Use Fetch API or XMLHttpRequest for asynchronous service request
        fetch('/request-service', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'service_id': serviceId,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response, e.g., show success message, update UI, etc.
            console.log(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
