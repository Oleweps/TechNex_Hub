// static/js/equipment_details_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Contact Seller" button
    var contactButton = document.querySelector('.contact-seller-btn');
    contactButton.addEventListener('click', function () {
        // Retrieve the equipment ID from the button's data attribute
        var equipmentId = contactButton.getAttribute('data-equipment-id');

        // Use Fetch API or XMLHttpRequest for asynchronous contact request
        fetch('/contact-seller', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'equipment_id': equipmentId,
            }),
        })
        .then(response => response.json())
        .then(data => {
            // You can handle the response data, e.g., display a success message or update UI
            console.log(data);
        });
    });
});
